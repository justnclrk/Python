import math

def gradingStudents(grades):
    result = [] # create empty array to store new integers
    for grade in grades: # run through items in grades array
        r = 5 * math.ceil(grade / 5) # define rounded up grade (rounded up to the multiple of 5)
        if grade < 38: # if grade is lower than 38 leave it since it is a failing grade
            result.append(grade) # append grade to our empty array
        elif r - grade < 3: # else if the difference of the rounded graded minus the actual grade is less than 3, append the rounded grade
            result.append(r)
        else:
            results.append(grade) # else if the difference of the rounded graded minus the actual grade is more than 3, append the grade
    return result #return result

print(gradingStudents([73, 67, 38, 33])) # print result of these grades

