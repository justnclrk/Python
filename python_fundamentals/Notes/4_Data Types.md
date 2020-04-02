Data Types
Data type refers to how the computer knows to classify information. To determine data type, ask what category a value belongs to. Here's a list of the data types that you will surely be using in building web applications.

There are several general classifications for data we're interested in. Primitive data types are the basic building blocks of a language. Most languages have these in common. Here are the most common:

Boolean Values - Assesses the truth value of something. It has only two values: True and False
Numbers - Integers (whole numbers), floating point numbers (commonly known as decimal numbers), and complex numbers.
Strings - A text literal. Most pages in the web work with strings quite often.
Composite types are collections composed of the above primitive types.

Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values. Tuples can contain mixed data types.
Lists - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values.
We will cover these data types more in the following tabs.

In Python, (almost) everything is an object. We will touch on this later when we get into Object Oriented Programming(OOP).

Indentation & Line-Endings
One of the most important aspects of Python is indentation. Python has no brackets, braces, or keywords to indicate the start and end of certain code blocks such as functions, if statements, and loops. The only delimiter is the colon (:) and the indentation of the code itself. You'll see that indenting starts a new code block and un-indenting ends that block. Don't worry if these codes don't make sense right now; we'll go over function and if- statements later. Just take note of how the indentation looks.

# define a function that says hello to the name provided
# this starts a new block
def say_hello(name):
  #these lines are indented therefore part of the function
  if name:
   print 'Hello, ' + name + 'from inside the function'
  else:
   print 'No name'
# now we're unindented and have ended the previous block
print 'Outside of the function'


In the following tabs we'll show you how to use data types and execute logic using Python. Experimenting with new concepts is exactly what the Python shell is for. Try running the sample code snippets in Python shell to see immediate output. Make sure to copy and paste the whole snippet at once for it to run properly.