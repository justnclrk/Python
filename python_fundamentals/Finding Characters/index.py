# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.
word_list = ["My", "cat's", "name", "is", "Steve!"]
char = "e"


def letterCheck(my_list, subString):
    new_list = []
    for element in range(0, len(word_list)):
        if word_list[element].find(char) != -1:
            new_list.append(word_list[element])
    print(new_list)


letterCheck(word_list, char)
