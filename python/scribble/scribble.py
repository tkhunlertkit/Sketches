"""
My Module
"""

def my_pow(num_list, ppp):
    """
    pow function
    """
    for j in num_list:
        yield j ** ppp

MY_GEN = [x for x in my_pow([1, 2, 3], 4)]
print(MY_GEN[0])
for i in MY_GEN:
    print(i)
for i in MY_GEN:
    print(i)
