def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# def fib2(n):
#     if n <= 2:
#         return 1
#     else:
#         a, b = 0, 1
#         while n-1:
#             a, b = b, a+b
#             n -= 1
#         return b
