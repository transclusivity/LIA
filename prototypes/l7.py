"""
A lisp with 9 primitives,
- eq
- car
- cdr
- cons
- quote
- if
- lambda
- read
- write
"""

from dataclasses import dataclass as data

@data
class Atom:
    type: str
    value: str | float

@data
class Cell:
    car: Atom = None
    cdr: Atom = None

def pairlis(x, y, alist):
    return add(alist, Cell(x, y))

def assoc(x, alist):
    if alist == None:
        return panic(f"{x} was not found")
    elif alist.car.car == x:
        return alist.car.cdr
    return assoc(x, alist.cdr)

def evaluate(expr, alist):
    if isinstance(expr, Cell):
        if isinstance(expr.car, Atom):
            if expr.car.type == "procedure":
                return apply(expr.car, expr.cdr, alist)
            return expr.car
        if isinstance(expr.car, Cell):
            panic() # ????
    elif isinstance(expr, Atom):
        match expr.type:
            case "symbol": return assoc(expr.value, alist)
            case "number": return expr

def apply(proc, args, alist):
    print(args)
    return assoc(proc.value, alist)(*(evaluate(arg, alist) for arg in iterate(args)))

def iterate(cell):
    if cell.cdr.cdr != None:
        return (cell.car, *iterate(cell.cdr))
    return (cell.car, cell.cdr.car)

def add(cell, value):
    if cell.car == None:
        cell.car = value
        return cell
    match cell.cdr:
        case None:
            cell.cdr = Cell(value)
        case Cell():
            add(cell.cdr, value)
        case _:
            panic()
    return cell

def panic(message):
    print(message)
    quit()

def display(cell):
    print("({" ".join(i.value for i in iterate(cell))})")

def build(e):
    ast = Cell()
    for n in e.replace(")", " ) ").replace("(", " ( ").split():
        ...
    

print(build("(1 2 3 4)"))

