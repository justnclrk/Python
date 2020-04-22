def simpleArraySum(ar):
    """Given an array of integers, find the sum of its elements."""
    sum = 0  # define sum as zero
    for i in ar:  # iterate of array
        sum += i  # go up the array list
    return sum  # return sum


print(simpleArraySum([4, 7, 10]))
