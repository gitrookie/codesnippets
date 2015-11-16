# pycallbacks.py
# Python Callbacks and Idioms
# sorted built in function sorts the items lexographically i.e. alphabetic
# preceded by length comparison

l = ['bacd', 'a', 'dk', 'efg', 'acrf']
m = ["abcde", "abcd"]
print(sorted(m))
print(sorted(l, key=len, reverse=True))


def my_key(mylist, key):
    ''' Implements the function sort in which we can give
    give the required keys. Actual Objects never themselves
    compared. That is important detail to semantics of providing key
    to function'''

    aux = [(key(v), j, v) for j, v in enumerate (mylist)]
    print(aux)
    aux.sort()
    return [v for k, j, v in aux]
