Lists
A list, also known as an array in other programming languages, is a data type that allows you to hold groups of values. Think of a list like a dresser with multiple drawers in which each drawer stores some information. Lists are created with values inside of square brackets [], where each value is separated by a comma. After a list is created, it can still be updated by adding values and/or by deleting values. An empty list is simply [ ].

ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []
In Python, the elements of a list do not have to be of the same data type. A list can be a mixture of any Python data types, including, tuples, strings, numeric, and even a list itself (a list within a list). An example:



And if we run the code, the output would look like:



Accessing Values
Back to the dresser analogy, imagine that each drawer is numbered starting with 0. Say the first drawer( index of 0) has 'documents' inside, the second drawer (index 1) has 'envelopes' inside, and so on. Each drawer holds a number, also known as the index (which serves as the unique address that points to each of our items inside the drawer). You can access the items in the drawer like below:

drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print drawer[0]  #prints documents
#access the drawer with index of 1 and print value
print drawer[1] #prints envelopes
#access the drawer with index of 2 and print value
print drawer[2] #prints pens
Manipulating Lists
Here's a useful example of a method that we will use to manipulate lists:

<list>.append(<new_element>)

Appends a new item onto the end of the given list. You can pass any data type into this function.

x = [1,2,3,4,5]
x.append(99)
print x
#the output would be [1,2,3,4,5,99]
It's important to know that Python uses [ ] characters to return a copy of the list, constrained to the specified indices. This can be thought of as behaving like the slice function in JavaScript. The starting index and ending index should be separated by the ":" character.

x = [99,4,2,5,-3]
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];
For information on other available list methods, read the docs.

List Built-in Functions
Below is an example of a built-in function that deals with lists. The following functions can also be applied to all sequences, including tuples and strings. What do we mean when we say sequence? Think of a sequence as anything over which we can iterate. Here's one commonly used sequence function:

len(sequence): Returns the number of items in a sequence.

my_list = [1, 'Zen', 'hi']
print len(my_list)
# output
3
Some built-in functions for sequences:
enumerate(sequence) used in a for loop context to return two-item-tuple for each item in the list indicating the index followed by the value at that index.
map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
min(sequence) returns the lowest value in a sequence.
sorted(sequence) returns a sorted sequence
There are a few other useful built-in functions. Find them here.

List Built-in Methods
Below is an example of a built-in list method. These methods are specific to lists versus other sets, much like the string methods shown in the previous tab.

list.append(value)

my_list = [1,5,2,8,4]
my_list.append(7)
print my_list
# output:
# [1,5,2,8,4,7]
The following are some commonly used list methods:
list.extend(list2) adds all values from a second sequence to the end of the original sequence.
list.pop(index) remove a value at given position. if no parameter is passed, defaults to final value in the list.
list.index(value) returns the index position in a list for the given parameter.
These are just some of the things you can do to manipulate or extract information from a list. Click here to learn more about other built-in functions you can use with a list.