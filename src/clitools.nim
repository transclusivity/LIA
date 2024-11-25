import std/strutils

let
    bold      = 1
    faint     = 2
    italic    = 3
    underline = 4
    inverse   = 7
    crossed   = 9

    black   = 30
    red     = 31
    green   = 32
    yellow  = 33
    blue    = 34
    magenta = 35
    cyan    = 36
    white   = 37

    normal = 0

proc set(codes: varargs[int]): string =
    return "\x1b[" & codes.join(";") & "m"

proc bright(color: int): int =
    return color + 60

proc background(color: int): int = 
    return color + 10

echo set(bold, italic, bright(background(blue))), "color!", set(normal), "boop"
