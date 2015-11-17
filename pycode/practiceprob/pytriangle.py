def triangle1(n):
    for i in range(1, n+1):
        # s = "{0}" * i
        # print(s.format(i))
        print(str(i) * i)


def triangle2(n):
    # lent = len(range(0, n))
    for i in range(0, n):
        fmt_str = "%{0}d".format(n - i) + " %d" * i
        print(fmt_str % ((i+1,) * (i+1)))


def triangle3(n):
    for i in range(1, n+1):
        print(*range(1, i+1))
        # s = "{}" * i
        # print(s.format(*range(1, i+1)))


def all_triangle_numbers(n):
    "Triangular number"
    for i in range(1, n + 1):
        print("n = {0}, triangle = {1}".format(i, (i ** 2 + i)//2))


def triangular_numbers(n):
    for i in range(1, n+1):
        print(i, sum(range(1, i+1)))


def triangle4(n, pattern="*"):
    for i in range(n):
        fmt_str = "%{}s".format(n-i) + "%s" * (i)
        patt_str = (pattern,) * (i+1)
        print(fmt_str % patt_str)


def triangle5(n):
    for i in range(n):
        fmt_str = "%{}d".format(n-i) + "%d" * (i*2)
        data = tuple(range(i+1, 1, -1)) + tuple(range(1, i+2, 1))
        print(fmt_str % data)

triangle5(10)
