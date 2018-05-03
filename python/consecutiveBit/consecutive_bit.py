def consecutiveBit(n):
    s=bin(n)
    for i,j in zip(s,s[1:]):
        if i == '1' and i == j:
            return True
    return False

print consecutiveBit(337)
