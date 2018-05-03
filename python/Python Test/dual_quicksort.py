import random
import cProfile

SIZE = 10000000
ITERATION = 1

# def shuffle(A):
#     for i in range(len(A) / 3):
#         f = random.randint(0, len(A))
#         s = random.randint(0, len(A))
#         temp = A[s]
#         A[s] = A[f]
#         A[f] = temp
#
def quicksort(A, left, right):
    # shuffle(A)
    p = A[right]
    i = left
    j = right - 1
    if i > j or i < 0 or j < 0 or j > len(A) - 1:
        return
    while i < j:
        while A[i] <= p and i < j:
            i += 1
        while A[j] >= p and j > i:
            j -= 1
        if i < j:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    if A[i] > p:
        A[right] = A[i]
        A[i] = p
    quicksort(A, left, i)
    quicksort(A, i+1, right)

if __name__ == '__main__':
    for i in range(ITERATION):
        A = []
        for i in range(SIZE):
            A.append(random.randint(0, SIZE * 20))

        B = list(A)

        cProfile.run('quicksort(A, 0, len(A) - 1)')

        if sorted(B) != A:
            print 'FAIL !!!!', i
    print 'DONE'
