# rodcut.py

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def cut_rod(p, n):
    if n == 0:
        return 0

    q = -100
    for i in range(n):
        q = max(q, p[i] + cut_rod(p, n-i-1))

    return q
