def birthdayCakeCandles(ar):
    """
    You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age.
    When she blows out the candles, she’ll only be able to blow out the tallest ones.
    Your task is to find out how many candles she can successfully blow out.
    """
    count = 0  # define the count
    Max = max(ar)  # define max (tallest candle) int of array
    for i in range(len(ar)):  # iterate over length of array
        if(ar[i] == Max):  # if item in array is equal to max (tallest candle)
            count += 1  # add 1 to the count
    return count  # return count


print(birthdayCakeCandles([3, 2, 1, 3]))
