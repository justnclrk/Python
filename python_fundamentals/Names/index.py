# Write the following function.
# Part I
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
# Create a program that outputs:
# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel
for x in students:
    print(x["first_name"], x["last_name"])
# Part II
# Now, given the following dictionary:
users = {
    'Students': [
        {'first_name':  'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
}
# Create a program that prints the following format (including number of characters in each combined name):
# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13
for key in users:
    print(key)
    count = 1
    for each_dict in users[key]:
        total_len = len(each_dict["first_name"]) + len(each_dict["last_name"])
        print("{} - {} {} - {}".format(count,
                                       each_dict["first_name"], each_dict["last_name"], total_len))
        count += 1
