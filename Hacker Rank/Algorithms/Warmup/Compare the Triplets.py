"""
Complete the function compareTriplets in the editor below. It must return an array of two integers, the first being Alice's score and the second being Bob's.

compareTriplets has the following parameter(s):

a: an array of integers representing Alice's challenge rating
b: an array of integers representing Bob's challenge rating
"""


def compareTriplets(a, b):
    points = [0, 0]  # define points array as zero
    arr = list(zip(a, b))  # combine a and b into a new array
    for i in arr:  # iterate over new array
        if i[0] > i[1]:  # compare first and second indexs of array
            points[0] += 1  # if first index (alice) is larger, give her a point
        elif i[1] > i[0]:  # compare second and first indexs of array
            points[1] += 1  # else if second index (bob) is larger, give him a point
        else:  # else pass
            pass
    return points  # return points


print(compareTriplets([4, 3, 1], [8, 6, 3]))
