def diagonalDifference(arr):
    difference = 0
    arr_length = len(arr)
    for i in range(arr_length):
        difference += arr[i][i]
        difference -= arr[i][arr_length-i-1]
    return abs(difference);
print(diagonalDifference())