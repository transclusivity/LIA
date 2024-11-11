from typing import Any
from dataclasses import dataclass as datacls

@datacls
class Cell:
    car: Any = None
    cdr: Any = None

def find(symbol, lookup):
    if not lookup: panic("Symbol value not found.")
    elif lookup.car.car == symbol: return lookup.car.cdr 
    else: return find(symbol, lookup.cdr)

def define(symbol, value, lookup):
    if isinstance(symbol, Cell) and isinstance(value, Cell):
        ...
    elif isinstance(symbol, Atom) and isinstance(value, Atom):
        ...

val = find("a", Cell(Cell("b", 10), Cell(Cell("a", 11))))
print(val)
env = Cell()
define(Cell("a"), Cell(10), env)


# template

def main():
    expr = Cell(1, Cell(2, Cell(Cell(1, Cell(2)))))
    pretty_expr = write_expr(expr)
    print(pretty_expr)

def write_expr(properls):
    ...
        
def read_expr():
    ...

if __name__ == "__main__":
    run_b()
