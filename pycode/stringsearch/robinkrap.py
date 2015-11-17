def stringsearch(s, t):
    "Rabin Karp Algorithm for sub string search"
    n = len(s)
    m = len(t)
    indexlist = list()
    for i in range(n-m+1):
        if hash(s[i:i+m]) == hash(t):
            indexlist.append(i)
    return indexlist


def robin_karp2(s, t):
    "Rabin Karp Algorithm using base"
    n = len(s)
    m = len(t)
    indexlist = list()
    hs = rhash(s[0:m])


def rhash(s):
    n = len(s)
    hash_num = 0
    for i in range(n):
        hash_num = ord(s[i]) + (hash_num << 6) + (hash_num << 16) - hash_num
    return hash_num % 59
