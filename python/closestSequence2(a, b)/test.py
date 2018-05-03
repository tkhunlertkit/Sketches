def closestSequence2(a, b):
    if len(b) < len(a):
        a, b, = b, a
    diff = len(b) - len(a)
    d = [None] * len(b)
    for i in range(len(b) - 1, -1, -1):
        d[i] = [None] * len(a)
        for j in range(len(a) - 1, -1, -1):
            if not (j > i or i > j + diff):
                if i + 1 < len(b) and j + 1 < len(a):
                    add = d[i+1][j+1]
                else:
                    add = 0

                if i + 1 < len(b):
                    cmp = d[i+1][j]
                else:
                    cmp = None

                ab = abs(b[i] - a[j])
                c = compare(ab + add , cmp)
                d[i][j] = c
            else:
                d[i][j] = None
    for i in d:
        for a in i:
            print ' %5s ' % a,
        print

def compare(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a,b)

if __name__ == '__main__':
    a = [0, 1, 3, 2]
    b = [1, 0, 2, 6, 4]

    closestSequence2(a, b)
