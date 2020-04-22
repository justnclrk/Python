"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
"""


def miniMaxSum(arr):
    sum = 0  # define sum
    for i in range(len(arr)):  # iterate over the length of the array
        sum += arr[i]  # add each value of the array to sum
    print(sum-max(arr), sum-min(arr))
    # print the sum minus the max of the array, which will give the minimum value
    # print the sum minus the min of the array, which will give the maximum value


miniMaxSum([1, 2, 3, 4, 5])
