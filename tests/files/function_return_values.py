import math
from typing import Optional


# TMN002 function returns too many values (5 > 3).
def f():
    return 1, 2, 3, 4, 5


# TMN002 function returns too many values (5 > 3).
def g():
    return [1, 2, 3, 4, 5]


# TMN002 function returns too many values (6 > 3).
async def h():
    return 1, 2, 3, 4, 5, 6


# A correct example.
def gt(a: float, b: float) -> Optional[bool]:
    if math.isnan(a) or math.isnan(b):
        return
    return a > b
