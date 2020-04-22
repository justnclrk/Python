
def diagonalDifference(arr):
    """Given a square matrix, calculate the absolute difference between the sums of its diagonals."""
    difference = 0
    arr_length = len(arr)
    for i in range(arr_length):
        difference += arr[i][i]
        difference -= arr[i][arr_length-i-1]
    return abs(difference)


print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
