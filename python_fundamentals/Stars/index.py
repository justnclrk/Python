#Part I
#Create a function called draw_stars() that takes a list of numbers and prints out *.
x = [4, 6, 1, 3, 5, 7, 25]
def draw_stars(arr):
    for key in arr:
        my_line = ""
        for i in range(0,key):
            my_line += "*"
        print my_line
draw_stars(x)
#Part II
#Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.
x = [4, "Steve", 1, "Justin", 5, 7, "Sam"]
def draw_stars2(arr):
    for key in arr:
        my_line = ""
        if isinstance(key, str):
            vo = key[0]
            for v in range (0, len(key)):
                my_line += vo
        else:
            for i in range(0,key):
                my_line += "*"
        print my_line.lower()
draw_stars2(x)