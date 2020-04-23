"""
Given the names and grades for each student in a Physics class of N students, store them in a nested list
and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
"""

python_students = [['Harry', 37.21], ['Berry', 37.21],
                   ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]


new_list = [name for record in python_students for name in record]

print(new_list)
