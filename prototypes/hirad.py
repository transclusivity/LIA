"""
Implementation Notes:
========================
> is the only comparison operator needed, xor is the only logical operator needed, the rest can be boostrapped from them

Design Notes:
================
- Everything in the syntax of Hirad is an expression.
- Each expression is made of a actor, scalar, vector, or matrix.
- Actors are atom objects with a record, a type and a protocol
- Expressions represent a list of signal arguments sent to an object.
- There are two forms to expressions
    - parameter expressions have a target and parameter signature, ie (Type new int) or (num + 3).
    - keyword expressions have a target and a keyword signature, ie (target keywords)
- Each object has a protocol that describes what messages it understands.
- Accessors are unary messages.
- The symbol ; is the cascade operator, so where (obj a; d) -> ((obj . b) (obj . d))
- The symbol : is the cons operator, so where (a: b c: d) -> ((a . b) (c . d))

"""

from sys import argv as term_args
from dataclasses import dataclass as datacls, field
from enum import Enum, auto
from typing import Any




class TokenType(Enum):
    CHAIN = auto()
    CASCADE = auto()
    END = auto()
    SYMBOL = auto()
    NUMBER = auto()
    OPEN_BLOCK = auto()
    CLOSE_BLOCK = auto()
    OPEN_TYPE_BLOCK = auto()
    CLOSE_TYPE_BLOCK = auto()
    OPEN_SEQUENCE = auto()
    CLOSE_SEQUENCE = auto()


@datacls
class Token:
    src: str
    line: int
    position: int
    context: str
    literal: str
    type: TokenType


@datacls
class Lexer:
    tokens: list = field(default_factory=list)
    line: int = 0
    position: int = 0

    def scan(self, program):
        self.chars = program.split("\n")
        while self.chars:
            match self.current:
                case "," as token: self.add(token, TokenType.CHAIN)
                case ";" as token: self.add(token, TokenType.CASCADE)
                case "." as token: self.add(token, TokenType.END)
                case "{" as token: self.add(token, TokenType.OPEN_BLOCK)
                case "}" as token: self.add(token, TokenType.CLOSE_BLOCK)
                case "[" as token: self.add(token, TokenType.OPEN_TYPE_BLOCK)
                case "]" as token: self.add(token, TokenType.CLOSE_TYPE_BLOCK)
                case "(" as token: self.add(token, TokenType.OPEN_SEQUENCE)
                case ")" as token: self.add(token, TokenType.CLOSE_SEQUENCE)
                case " ": self.chars.pop(0)
                case _: self.add_symbol()
        return self.tokens

    @property
    def current(self):
        return self.chars[0]

    @property
    def next(self):
        return self.chars[1]

    def add(self, token, type):
        self.tokens.append(Token(token, type))
        self.chars.pop(0)

    def add_symbol(self):
        symbol = list()
        while self.chars and not self.current in ";,.(){}[] ":
            symbol.append(self.chars.pop(0))
        self.tokens.append(Token("".join(symbol), TokenType.SYMBOL))


@datacls
class Keyword:
    parameter: str
    argument: str


class MessageType(Enum):
    CASCADE = auto()
    CALL = auto()
    CHAIN = auto()


@datacls
class Actor:
    def send(self, *keywords) -> None:
        ...

    def cascade(self, *keywords) -> 'Actor':
        self.send(keywords)
        return self

    def chain(self, *keywords) -> Any:
        result = self.send(keywords)
        return result

    def protocol(self):
        ...


class Type(Actor):
    ...


class Context(Actor):
    ...


@datacls
class Scalar(Actor): # ref
    ...


@datacls
class Vector(Actor):
    ...


@datacls
class Matrix(Actor):
    ...


@datacls
class Answer(Scalar):
    def send(self, *keywords) -> None:
        print("answer recieved:", keywords)
    

@datacls
class Number(Scalar):
    def send(self, *keywords) -> None:
        print("number recieved:", keywords)


@datacls
class Letter(Scalar):
    def send(self, *keywords) -> None:
        print("rune recieved:", keywords)


@datacls
class Message:
    reciever: Actor
    keywords: list[Keyword]
    type: MessageType


@datacls
class Parser:
    syntax: list[Message] = field(default_factory=list)

    def message(self):
        reciever = self.tokens.pop(0)
        keywords = list()
        type = MessageType.CALL

        while self.tokens:
            token = self.tokens.pop(0)
            if token.literal.endswith(":"):
                keywords.append(Keyword(token.literal[:-1], self.tokens.pop(0)))
            if token.type == TokenType.CHAIN:
                return Message(reciever, keywords, MessageType.CHAIN)
            if token.type == TokenType.CASCADE: 
                return Message(reciever, keywords, MessageType.CASCADE)
            if token.type == TokenType.END_EXPRESSION:
                return Message(reciever, keywords, type)

    def process(self, tokens):
        self.tokens = tokens
        while self.tokens:
            match self.tokens[0].type:
                case TokenType.SYMBOL:
                    self.syntax.append(self.message())
                case TokenType.CASCADE: 
                        ...
                case TokenType.CHAIN: 
                        ...
        return self.syntax

@datacls
class Interpreter:
    def send(self, message):
        reciever = objects[message.reciever.literal]
        match message.type:
            case MessageType.CASCADE:
                return reciever.cascade(*message.keywords)
            case MessageType.CALL:
                reciever.send(*message.keywords)
            case MessageType.CHAIN:
                return reciever.chain(*message.keywords)

    def interpret(self, syntax):
        first, *rest = syntax
        reciever = self.send(message) 
        for message in rest:
            reciever = self.send(message)


@datacls
class Hirad:
    lexer: Lexer
    parser: Parser
    interpreter: Interpreter

    def main(self):
        match term_args:
            case [_, src]: self.run(src)
            case [_]: self.repl()
            case _: print("Usage: python hirad.py <Optional: Path to src file>")

    def execute(self, program):
        match program:
            case "quit": quit()
            case _:
                tokens = self.lexer.scan(program)
                syntax = self.parser.process(tokens)
                print(syntax)
                result = self.interpreter.run(syntax)

    def repl(self):
        while True:
            self.execute(input("Hirad :: "))

    def load(self, src):
        with open(src) as program:
            self.execute(program.readlines())


if __name__ == "__main__":
    hirad = Hirad(Lexer(), Parser(), Interpreter())
    hirad.main()



