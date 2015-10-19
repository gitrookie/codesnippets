def prob1():
    sum = 0
    for x in range(3, 1000):
        if ((x % 3) == 0 or (x % 5) == 0):
            sum = sum + x
    return sum

print(prob1())


def prob1_eff(n):
    target = 999
    p = target // n
    return (n * p * (p+1))/2

print(prob1_eff(3) + prob1_eff(5) - prob1_eff(15))
