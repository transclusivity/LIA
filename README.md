# Hirad

- Everything in the syntax of Hirad is an expression.
- Each expression is made of a actor, scalar, vector, or matrix.
- Actors are atom objects with a record, a type and a protocol
- Expressions represent a list of signal arguments sent to an object.
- There are two forms to expressions:
    - parameter expressions have a target and parameter signature, ie `(<object> <operator> <Optional: Operand>)`.
    - keyword expressions have a target and a keyword signature, ie `(<object> <keyword>: <value>)`.
- Each object has a protocol that describes what messages it understands.
- Accessors are unary messages.

---


## Principles

- "make the simple things very simple, and the complex things very possible" -- Alan Kay
- automation over specification. The implementation should deal with all it can so you dont have too, including formatting, documentation, tests, imports, types/inference, ownership/memory, etc
- zero cost abstraction. there should be very little between you and the computer if possible, and the syntax of the language should map to the underlying hardware or at least to lower level concepts in an intuitive way
- where there is one, there is many. an operation I can apply to a scalar value should at least be possible to define/apply to a vector or matrix as well, without any explicit iteration
- verifiable. strongly statically typed with first class tests and errors as values
- simplicity and consistency in the core language. no special case syntax quirks, no weird edge case, no sugar for things used in one way one time. everything should have a clearly defined purpose, flexibility and expressiveness in the fulfilment of that purpose, and consistent use in all contexts
- fully featured. a batteries includes approach will stop people from having to reimplement the basic tooling found in other languages, and keeps softwares focus on the business needs and behavior instead of writing a set implementation

---

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

---

## Syntax

```st
{ ... } block of statements
[ ... ] list of type parameters
( ... ) sequence of expressions
| ... | temporary variables inside a block
^... return statement)
```

---

## Inspirations

- Oberon2
- Modula
- Algo68
- Pascal
- Smalltalk
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

---

## Resources

### General
- [Catalog: Norayr's papers](https://norayr.am/papers/)
- [Catalog: Soc's papers](https://soc.me/)

### Agda
- [Impl?](https://plfa.github.io/)

### Oberon
- [Impl: Oberon+](https://oberon-lang.github.io/)
- [Paper: Oberon-2, a hi-performance alternative to C++](https://haugwarb.folk.ntnu.no/Programming/Oberon/oberon_vs_cpp_II.htm) 
- [Paper: Oberon - the overlooked jewel](https://dcreager.net/pdf/Franz2000.pdf)
- [Catalog: Texts to learn Oberon07](https://oberon07.com/texts.xhtml)
- [Catalog: Resources related with Oberon](https://oberon.org/en)
- [Book: Object-oriented programming in Oberon-2](http://norayr.am/papers/oop_in_oberon-2_book.pdf)

### Modula
- [Impl: ADW Modula-2](https://www.modula2.org/)
- [Catalog: Modula 3 Resource Page (Unmaintained)](https://www.modula3.org/)
- [Catalog: Wirth languages, Pascal, UCSD, Turbo, Delphi, Freepascal, Oberon](http://pascal.hansotten.com/)

### Lisp
- [Paper: The First Lisp Compiler](https://texdraft.github.io/lisp-compiler/internals.html)

### Fortran
- [Book: Systems manual for 704 Fortran and 709 Fortran](https://archive.computerhistory.org/resources/text/Fortran/102653992.05.01.acc.pdf) ??

### Algol
- [Paper: Algol-58 – The International Algebraic Language](https://datatron.blogspot.com/2018/07/algol-58-international-algebraic.html?m=1)
- [Paper: The Dijkstra-Zonneveld ALGOL 60 compiler for the Electrologica X1](https://ir.cwi.nl/pub/4155)
- [Paper: A comparison between the ALGOL 60 implementations on the Electrologica X1 and the Electrologica X8](https://ir.cwi.nl/pub/13677)
- [Paper: An ALGOL 60 compiler in ALGOL 60 : text of the MC-compiler for the EL-X8](https://ir.cwi.nl/pub/13069)
- [Book: ALGOL 60 implementation](https://www.softwarepreservation.org/projects/ALGOL/book/Randell_ALGOL_60_Implementation_1964.pdf)

### To Be Sorted

- [Paper: Types for delimited control operators](https://www.khoury.northeastern.edu/home/amal/course/7480-s12/delim-control-notes.pdf)
- [Documentation tests in Rust](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html#attributes)
- [...](https://philarchive.org/archive/AUGTGS-3)
- [...](https://homepage.divms.uiowa.edu/~slonnegr/plf/Book/Chapter4.pdf)
- [...](https://homepages.cwi.nl/~steven/vw.html)
- [...](https://en.algorithmica.org/hpc/simd/masking/)
- [...](https://bookdown.org/ndphillips/YaRrr/logical-indexing.html)
- [...](https://docs.julialang.org/en/v1/manual/arrays/#Logical-indexing)
- [...](https://www.mathworks.com/help/matlab/math/array-indexing.html)
- [...](https://homepages.cwi.nl/~steven/pascal/book/pascalimplementation.html)
- [...](https://academic.oup.com/comjnl/article-pdf/21/4/316/1021498/210316.pdf)
- [...](https://arxiv.org/abs/1606.06379)
- [...](https://docs.racket-lang.org/reference/cont.html#(def._((quote._~23~25kernel)._continuation-prompt-tag~3f)))
- [...](https://en.m.wikipedia.org/wiki/Substructural_type_system)
- [...](https://wiki.alopex.li/WirthEvolution)
- [...](https://mitpress.mit.edu/9780262535519/the-reasoned-schemer/)
- [...](https://cliplab.org/logalg/doc/The_Art_of_Prolog.pdf)
- [...](http://www.de-nivelle.de/appendixB.pdf)
- [...](https://webperso.info.ucl.ac.be/~pvr/implementation.html)
- [...](https://www.cs.nmsu.edu/~epontell/adventure/paper.html)
- [...](https://fredrikj.net/calcium/)
- [...](https://www.cs.cmu.edu/~crary/819-f09/Landin66.pdf)
- [...](https://en.wikipedia.org/wiki/Unum_(number_format))
- [...](https://github.com/milahu/awesome-transpilers)
- [...](https://www.microsoft.com/en-us/research/uploads/prod/2021/06/perceus-pldi21.pdf)
- [...](https://dl.acm.org/doi/pdf/10.1145/3607840)
- [...](https://dl.acm.org/doi/pdf/10.1145/3656398)
- [...](https://learn.microsoft.com/en-us/shows/seth-juarez/anders-hejlsberg-on-modern-compiler-construction)
- [...](https://github.com/ollef/rock)
- [...](https://ollef.github.io/blog/posts/query-based-compilers.html)
- [...](https://existentialtype.wordpress.com/2012/08/25/polarity-in-type-theory/)
- [...](https://bracha.org/mirrors.pdf)
- [...](https://dreamsongs.com/Files/ECOOP.pdf)
- [...](https://engineering.purdue.edu/RVL/Publications/Kersten93ATutorial.pdf)
- [...](https://courses.cs.umbc.edu/331/resources/lisp/onLisp/25objectOrientedLisp.pdf)
- [...](https://dl.acm.org/doi/pdf/10.1145/3386324)
- [...](https://docs.racket-lang.org/guide/index.html)
- [...](https://accu.org/journals/overload/26/148/james_2586/)
- [...](https://www.youtube.com/watch?v=-TJGhGa04F8)

---

## Credits
- Alan C. Kay
- Niklaus E. Wirth

