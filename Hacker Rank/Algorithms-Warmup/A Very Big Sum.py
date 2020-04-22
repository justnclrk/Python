def aVeryBigSum(ar):
    """Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large."""
    sum = 0  # define sum as zero
    for i in ar:  # iterate over array
        sum += i  # add each item together in sum
    return sum  # return sum


print(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))
