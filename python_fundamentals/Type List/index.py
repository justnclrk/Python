# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.
mixed = ["My ", 34, "cat's ", 50, "is ", "named ", 20, "Steve!"]
integer = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
string = ["You ", "are ", "hiding ", "a ", "child!"]


def identify_list_type(lst):
    new_string = ''
    total = 0

    for value in lst:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            new_string += value

    if new_string and total:
        print "The array you entered is of mixed type"
        print "String:", new_string
        print "Total:", total

    elif new_string:
        print "The array you entered is of string type"
        print "String:", new_string

    else:
        print "The array you entered is of number(float or int) type"
        print "Total:", total


print identify_list_type(mixed)
print identify_list_type(integer)
print identify_list_type(string)
