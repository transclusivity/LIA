from dataclasses import dataclass as datacls
from sys import argv as arguments
import operator
import math

@datacls
class Token:
    src: str
    line: int
    position: int
    context: str
    value: str

@datacls
class Atom:
    type: str
    value: str | float


class Mlp:
    def __init__(self):
        self.env = standard_environment()

    def main(self, arguments):
        match arguments:
            case [_]: self.repl()
            case [_, path]: self.run(path)
            case _: print("Usage: python mlp <Optional: Path to program.>")

    def repl(self):
        self.src = "ReplContext"
        while True:
            match input("mini-list-processor :: "):
                case "exit": return
                case expr: self.execute(expr)

    def run(self, src):
        self.src = src
        with open(src) as file:
            program = file.read()
        self.execute(program)

    def execute(src, program, env):
        interpret(parse(lex(scan(program))))

    def scan(src, program):
        return src, (enumerate(program
            .replace("(", " ( ")
            .replace(")", " ) ")
            .split("\n")))

def lex(data):
    src, lines = data
    return [Token(src, line + 1, position + 1, value)
        for line, content in lines
        for position, value in enumerate(content.split())]

def panic(src, line, position, value, type, message):
    with open(src, "r") as file:
        context = file.read()[line]
    print(f"""Error in {src} (ln {line}, pos {position})

    {context}
    {" " * position}^ here

{type}: {message}.
    """)
    exit()

def parse(tokens):
    ast = list()
    while tokens:
        token = tokens[0]
        match token.value:
            case "(":
                ast.append(extract_expr_from(line))
            case ")":
                panic(token.line, token.position, token.value, "Syntactic Error", "Ended expression when none was open", tokens)
            case other:
                ast.append(extract_atom_from(line))
    return ast
    
def extract_expr_from(line):
    expr = list()
    line.content.pop(0)
    while line.content[0].value != ")":
        match line.content[0].value:
            case "(":
                expr.append(extract_expr_from(line))
            case _:
                expr.append(extract_atom_from(line))
    line.content.pop(0)
    return expr

def extract_atom_from(line):
    token = line.content.pop(0)
    try:
        return Atom("number", float(token.value))
    except ValueError:
        return Atom("symbol", token.value)

def evaluate(expression: Atom | list[Atom, ...], environment: dict):
    match expression:
        case [Atom(value="if"), test, conseq, alt]:
            return evaluate((conseq if evaluate(test, environment) else alt), environment)
        case [Atom(value="define"), symbol, expr]:
            environment[symbol.value] = evaluate(expr, environment)
        case [name, *exprs]:
            function = evaluate(name, environment)
            arguments = [evaluate(expr, environment).value if isinstance(expr, Atom) else evaluate(expr, environment) for expr in exprs]
            return function(*arguments)
        case Atom() as atom:
            match atom.type:
                case "symbol":
                    if atom.value.startswith("'"):
                        return atom
                    return environment[expression.value]
                case _: return expression

def interpret(ast, env):
    for expr in ast:
        evaluate(expr, env)

def standard_environment():
    return {
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
    

if __name__ == "__main__":
    mlp = Mlp()
    mlp.main(arguments)

