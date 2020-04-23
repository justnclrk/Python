"""
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros.
Print the decimal value of each fraction on a new line.
"""


def plusMinus(arr):

    positive = 0  # define positive count
    negative = 0  # define negaive count
    zero = 0  # define zero count
    for i in range(len(arr)):  # iterate over length of array
        if(arr[i] > 0):  # if the index of array in larger than zero
            positive += 1  # add a point to positive count
        elif(arr[i] == 0):  # else if the index of array in equal to zero
            zero += 1  # add a point to zero count
        else:  # else the index of array has to a negative
            negative += 1  # add a point to negative count
    print(positive/len(arr))  # print postive count divided by length of array to find fraction of postives
    # print negative count divided by length of array to find fraction of negatives
    print(negative/len(arr))
    print(zero/len(arr))  # print zero count divided by length of array to find fraction of zeros


plusMinus([-4, 3, -9, 0, 4, 1])
