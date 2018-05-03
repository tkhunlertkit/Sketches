def removeDigits(n, k):
    s = str(n)
    mi = float('inf')
    ma = 0
    for i,j in zip(range(len(s)), range(k, len(s) + 1)):
        a = int(s[i:j])
        if a < mi:
            mi = a
        if a > ma:
            ma = a
    return [mi, ma]

print removeDigits(15243,  2)
