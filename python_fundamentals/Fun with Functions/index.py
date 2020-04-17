# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000.
# As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.


def odd_even():
    for number in range(1, 2001):
        if number % 2 == 1:
            print("Number is {}. This is odd number.".format(number))
        else:
            print("Number is {}. This is an even number.".format(number))


odd_even()

# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.


def multiply(a, b):
    for x in range(len(a)):
        a[x] *= b
    return a


c = [2, 4, 10, 16]
d = multiply(c, 5)
print(d)

# Hacker Challenge:
# Write a function that takes the multiply function call as an argument.
# Your new function should return the multiplied list as a two-dimensional list.
# Each internal list should contain the 1's times the number in the original list


def layered_multiples(arr):
    parent_array = []
    for i in arr:
        child_array = []
        for num in range(i):
            num = 1
            child_array.append(num)
        parent_array.append(child_array)
    return parent_array


print(layered_multiples(multiply([2, 4, 5], 3)))
