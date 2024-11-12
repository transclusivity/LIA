"""
Damas-Hindley-Milner type inference  
"""

from dataclasses import dataclass as datacls

@datacls
class MonoType:
    pass

@datacls
class TypeVariable(MonoType):
    name: str

@datacls
class TypeConstructor(MonoType):
    name: str
    args: list[Monotype]

@datacls
class TypeScheme:
    variables: list[TypeVariable]
    type: MonoType

Integer = TypeConstructor("Int", list())
Boolean = TypeConstructor("Bool", list())

def list_type(type: MonoType) -> MonoType:
    return TypeConstructor("List", [type])

def function_type(argument: MonoType, result: MonoType) -> MonoType:
    return TypeConstructor("->", [argument, result])

Substitution = dict[str, MonoType]
Context = dict[str, TypeScheme]

def compose(new: Substitution, old: Substition) -> Substitition:
     T, *rest = new.values()
     return {key: T for key in new.update(old)}

def apply_type(type: MonoType, substitution: Substitution) -> MonoType:
    if isinstance(type, TypeVariable):
        return substitution.get(type.name, type)
    if isinstance(type, TypeConstructor):
        return TypeConstructor(type.name, [apply_type(argument, substitution) for argument in type.args])
    raise TypeError(f"Unknown Type: {type}")

def apply_context(context: Context, substitution: Substitution) -> Context:
    ...

def unify(type1: MonoType, type2: MonoType) -> Substitution:
    if isinstance(type1, TypeVariable):
        ...

def infer(expression: Object, context: Context) -> tuple[Substitution, MonoType]:
    ...


"""
Version 2
"""

from dataclasses import dataclass as data, field
new = lambda constructor: field(default_factory=constructor)

@data
class TypeVariable:
    name: int

@data
class TypeConstructor:
    name: str
    generics: list[Monotype] = new(list)

substitution = list()
def unify(type1, type2):
    match (type1, type2):
        case (TypeConstructor(name1, generics1), TypeConstructor(name2, generics2)):
            assert name1 == name2
            assert len(generics1) == len(generics2)
            for generic1, generic2 in zip(generics1, generics2):
                unify(generic1, generic2)
        case (TypeVariable(i), TypeVariable(j)):
            if i == j: pass
        case (TypeVariable(i), _) if substitution[i] != TypeVariable(i):
            unify(substitution[i], type2)
        case (_, TypeVariable(i)) if substitution[i] != TypeVariable(i):
            unify(type1, substitution[i])
        case (TypeVariable(i), _):
            assert not occurs_in(i, type2)
            substitution[i] = type2
        case (_, TypeVariable(i)):
            assert not occurs_in(i, type1)
            substitution[i] = type1

def occurs_in(index, type):
    match type:
        case TypeVariable(i) if substitution[i] != TypeVariable(i):
            occurs_in(index, substitution[1])
        case TypeVariable(i):
            i == index


