import eulerhelp
import sys
# num = sys.argv[1]
from eulerhelp import x
from functools import reduce


def prob1():
    sum = 0
    for x in range(3, 1000):
        if ((x % 3) == 0 or (x % 5) == 0):
            sum = sum + x
    return sum

# print(prob1())


def prob1_eff(n):
    target = 999
    p = target // n
    return (n * p * (p+1))/2

# print(prob1_eff(3) + prob1_eff(5) - prob1_eff(15))


# Problem2
def fib():
    '''Computes the even valued Fibbonacci
    whose value donot exceed four million'''

    sum = 2
    a, b = 1, 2
    while b <= 4000000:
        a, b = b, a+b
        if b % 2 == 0:
            sum += b
    return sum

# Problem 3
prime_factors = []


def largest_prime_factor(n):
    if eulerhelp.is_prime(n):
        # prime_factors.append(n)
        return n, prime_factors
    if n % 2 == 0:
        # prime_factors.append(2)
        return largest_prime_factor(n // 2)
    i = 3
    while True:
        if n % i == 0:
            # prime_factors.append(i)
            return largest_prime_factor(n // i)
        else:
            i += 2


# Problem 4
def palndromic_number():

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    num_list = []
    index = 0
    for i in range(999, 100, -1):
        if i < index:
            return num_list[1]
        for j in range(999, 100, -1):
            number = i * j
            if is_palindrome(number):
                index = j
                if not num_list:
                    num_list.append(j)
                    num_list.append(number)
                    break
                elif number > num_list[1]:
                    num_list[0] = j
                    num_list[1] = number
                    break


# Problem 5
def smallest_number(n):
    product = 1
    for i in range(1, n+1):
        if product % i != 0:
            product = eulerhelp.elcm(i, product)

    return product

# Problem 6
def square_diff(n):
    ans = 0
    for i in range(n, 0, -1):
        ans += i * int((i * i - i) / 2)
    return ans * 2

# Problem 7
def nth_prime(n):
    i = 1
    number = 3
    while True:
        if eulerhelp.is_prime(number):
            i += 1
            if i == n:
                return n, number
        number += 2

# Problem 8
def great_product(s, index):
    ans = None
    for i in range(1000-index):
        product = reduce(lambda a, b: int(a) * int(b), s[i:index+i])
        if ans is None:
            ans = product
        else:
            if product > ans:
                ans = product
    return ans

# print(great_product(x, 4))


# Problem 9
def three_product():
    for a in range(1000):
        for b in range(a+1, 1000):
            if a ** 2 + b ** 2 == (1000 - a - b) ** 2 and b < (1000 - b):
                return a*b*(1000-a-b)



def sum_primes(n):
    sum = 2
    i = 3
    while(i < n):
        if eulerhelp.is_prime(i):
            sum += i
        i += 2
    return sum

print(sum_primes(2000000))
