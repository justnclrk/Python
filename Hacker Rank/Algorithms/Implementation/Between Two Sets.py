"""
You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered

The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.
"""


def getTotalX(a, b):
    count = 0
    for y in range(len(a)):
        for z in range(len(b)):
            if(a[y] % 2 == 0):
                count += 1
            if(b[z] % 2 == 0):
                count += 1
    return count / 4


print(getTotalX([2, 4], [16, 32, 96]))
