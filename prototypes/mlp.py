"""
Mini List Processor.
"""

from dataclasses import dataclass as datacls
from sys import argv as arguments
import operator
import math


class Mlp:
    def __init__(self):
        self.environment = standard_environment()
        self.src = list()

    def main(self, arguments):
        match arguments:
            case [_]: self.repl()
            case [_, path]: self.run(path)
            case _: print("Usage: python mlp <Optional: Path to program.>")

    def repl(self):
        self.src.append("Repl")
        while True:
            match input("mlp :: "):
                case "exit": return
                case expr:
                    result = self.execute(expr)
                    if result:
                        print(result[0] if result[0] != None else "")
        self.src.pop()

    def run(self, src):
        self.src.append(src)
        with open(src) as file:
            program = file.read()
        self.execute(program)
        self.src.pop()

    def execute(self, program):
        return [self.evaluate(expression) for expression in self.parse(self.lex(self.scan(program)))]

    def scan(self, program):
        return (enumerate(program
            .replace("(", " ( ")
            .replace(")", " ) ")
            .split("\n")))

    def lex(self, lines):
        return [Token(line + 1, position + 1, value)
            for line, content in lines
            for position, value in enumerate(content.split())]

    def parse(self, tokens):
        ast = list()
        while tokens:
            token = tokens[0]
            match token.value:
                case "(":
                    ast.append(self.extract_expr_from(tokens))
                case ")":
                    self.panic(token, "Syntactic Error", "Unexpected \")\". Possibly caused by an extra parentheses")
                case other:
                    self.panic(token, "Syntactic Error", f"The expression \"{other}\" must be enclosed in paretheses")
        return ast

    def extract_expr_from(self, tokens):
        expr = list()
        tokens.pop(0)
        while tokens[0].value != ")":
            match tokens[0].value:
                case "(":
                    expr.append(self.extract_expr_from(tokens))
                case _:
                    expr.append(self.extract_atom_from(tokens.pop(0)))
        tokens.pop(0)
        return expr

    def extract_atom_from(self, token):
        try:
            return Atom("number", float(token.value), token.line, token.position)
        except ValueError:
            return Atom("symbol", token.value, token.line, token.position)

    def evaluate(self, expression):
        match expression:
            case [Atom(value="if"), test, conseq, alt]:
                return self.evaluate((conseq if self.evaluate(test) else alt))
            case [Atom(value="define"), symbol, expr]:
                self.environment[symbol.value] = self.evaluate(expr)
            case [Atom(value="import"), path]:
                self.run(f"{path.value}.lisp")
                return list()
            case [name, *exprs]:
                if not isinstance(name, list) and not name.type == "symbol":
                    return self.panic(name, "Invalid Procedure", f"The expression \"{name.value}\" is not a valid procedure")
                function = self.evaluate(name)
                arguments = [self.evaluate(expr).value if isinstance(expr, Atom) else self.evaluate(expr) for expr in exprs]
                return function.value(*arguments)
            case Atom() as atom:
                match atom.type:
                    case "symbol":
                        if atom.value.startswith("'"):
                            return atom
                        return self.environment[expression.value]
                    case _: return expression

    def panic(self, token, type, message):
        print(f"---\n{type}: {message}.\n---\nSrc: {self.src[-1]}\tLn: {token.line} Pos: {token.position}\n")
        exit()


@datacls
class Token:
    line: int
    position: int
    value: str


@datacls
class Atom:
    type: str
    value: str | float
    line: int
    position: int


def standard_environment():
    environment = {
        # Execution
        "apply": lambda f, *x: f(*x),
        "begin": lambda *x: x[-1],

        # IO
        "read": input,
        "write": print,

        # Lists
        "car": lambda x: x[0],
        "cdr": lambda x: x[1:],
        "cons": lambda x, y: [x] + y,
        "list": lambda *x: list(x),
        "len": len,

        # Typing
        "procedure?": callable,
        "symbol?": lambda x: isinstance(x, str),
        "number?": lambda x: isinstance(x, float),
        "list?": lambda x: isinstance(x, list),
        "null?": lambda x: x == [],

        # Math/logic
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        ">": operator.gt,
        "<": operator.lt,
        ">=": operator.ge,
        "<=": operator.le,
        "=": operator.eq,
        "equal?": operator.eq,
        "eq?": operator.is_,
        "not": operator.not_,
        "abs": abs,
    }
    for key in environment:
        environment[key] = Atom("procedure", environment[key], -1, -1)
    return environment


if __name__ == "__main__":
    mlp = Mlp()
    mlp.main(arguments)

