# A correct example
def f(a, b, c, d, e, f, _):
    pass


# TMN001 function has too many arguments (7 > 6).
async def g(a, b, c, d, e, f, g=None):
    pass


# TMN001 function has too many arguments (7 > 6).
lambda a, b, c, d, e, f, g: None
