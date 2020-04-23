"""
Given Maria's scores for a season, find and print the number of times she breaks her
records for most and least points scored during the season.
"""


def breakingRecords(scores):
    maxi = scores[0]  # create an empty array for max scores
    mini = scores[0]  # create an empty array for min scores
    maxcount = 0  # create max count
    mincount = 0  # create min count
    for i in range(len(scores)):  # for loop through length of scores array
        if(scores[i] > maxi):  # if score is greater than a max in the max scores array
            maxi = scores[i]  # add that score to the max scores array
            maxcount += 1  # add 1 if the record is broken
        if(scores[i] < mini):  # if score is lesser than a min in the min scores array
            mini = scores[i]  # add that score to the min scores array
            mincount += 1  # add 1 if the record is broken
    return [maxcount, mincount]  # return the number of times Maria broke the max and min records


print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))
