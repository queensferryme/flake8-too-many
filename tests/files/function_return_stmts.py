# TMN003 function has too many return statements (6 > 3).
def is_even(x: int) -> bool:
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x == 3:
        return False
    elif x == 4:
        return True
    elif x == 5:
        return False
    else:
        return x % 2 == 0
