# Hirad
*An object/array oriented programming language for scientific computing and systems programming, in the tradition of Smalltalk and APL.* 

## Why Hirad?
TODO...

## Installation
TODO...

## Usage
TODO...

## License
This project is licensed under the [MIT License](LICENSE).

## Contributing
TODO...

## Principles
- "make the simple things very simple, and the complex things very possible" -- Alan Kay
- automation over specification. The implementation should deal with all it can so you dont have too, including formatting, documentation, tests, imports, types/inference, ownership/memory, etc
- zero cost abstraction. there should be very little between you and the computer if possible, and the syntax of the language should map to the underlying hardware or at least to lower level concepts in an intuitive way
- where there is one, there is many. an operation I can apply to a scalar value should at least be possible to define/apply to a vector or matrix as well, without any explicit iteration
- verifiable. strongly statically typed with first class tests and errors as values
- simplicity and consistency in the core language. no special case syntax quirks, no weird edge case, no sugar for things used in one way one time. everything should have a clearly defined purpose, flexibility and expressiveness in the fulfilment of that purpose, and consistent use in all contexts
- fully featured. a batteries includes approach will stop people from having to reimplement the basic tooling found in other languages, and keeps softwares focus on the business needs and behavior instead of writing a set implementation

## Features
- build system, repl, package manager
- literate tests, documentation, and programming with support for md and asciidoc
- web, cli, tui, and gui tooling
- 3d graphics, CAD, and animation functionality
- math and science libs with heavy support for molecular dynamics and other simulation software
- parser combinators, regex, and other advanced text manipulation
- databases, iterators, and collections
- {i, u, f, vector}8/16/32/64/128/256/arbitrary(leb128)
- fused multiply add

## Syntax
*Subject to change*

```ocaml
Example: class
ex := Example obj

Example print := [|
    IO ~write self
]
ex display

Example incr := [ x: Int |
    IO ~write x + 1
]
ex incr 10

Example ~from ~to := [ x: Int y: Int |
    ^from + to
]
ex ~from 10 ~to 20

```

## Inspirations

- Smalltalk
- Apl
- Oberon2
- Modula
- Algo68
- Pascal
- Ml/ocaml
- Nim
- Haskell
- Lisp
- Rust
- Erlang
- Javascript
- Apl
- Prolog
- Hylo?
- Austral?
- Roc?
- Val?
- Clu?
- Vau/kernel?

# Credits
- Prof. Alan C. Kay
- Prof. Niklaus E. Wirth

