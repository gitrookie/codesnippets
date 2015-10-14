# Adding thousand separator in a number
def f2(n):
    r = []
    for i, c in enumerate(reversed(str(n))):
        if i and (not (i % 3)):
            r.insert(0, ',')
        r.insert(0, c)
    return "".join(r)

print(f2(1234567))

# Using str's format method
def f1(n):
    return "{0:,}".format(n)
    