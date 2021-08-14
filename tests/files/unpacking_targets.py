a, b, c, d, e, f, g = 1, 2, 3, 4, 5, 6, 7

for a, b, c, d, e in (range(n, n + 5) for n in range(5)):
    print(a + b + c + d + e)
