# sortingalgos.py


def insertsort(l):
    length = len(l) - 1
    for i in range(length):
        j = i + 1
        num = l[j]
        while j > 0 and l[j-1] > num:
            l[j] = l[j-1]
            j -= 1
        l[j] = num
