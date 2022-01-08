# TMN004 unpacking has too many targets (7 > 3).
a, b, c, d, e, f, g = 1, 2, 3, 4, 5, 6, 7

# A correct example.
a = b = 1
c, _, e, _, g = 2, 3, 4, 5, 6

# TMN004 unpacking has too many targets (6 > 3).
for h, i, j, k, l, m in (range(n, n + 6) for n in range(5)):
    print(h + i + j + k + l + m)

# A correct example.
for x in range(10):
    print(x ** 2)
