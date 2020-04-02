Comments
Comments are useful because they allow you to explain what your code is doing. Every language has a way of ensuring that some lines will not be executed at run time.

You're a developer now, and one of the most important jobs of a developer is writing re-usable code. By explaining what our code does in comments, we make it easier for ourselves and others to edit our code later on. In addition, comments can be helpful for writing pseudo-code when you're trying to work out a tough problem.

In Python, there are two ways to write comments:

#

# commenting a single line
# we can even comment out code
# print "this will not print!"
This is handy because we can comment out lines that may be causing problems while we're debugging our code.

"""  """  OR  '''  '''

print "read below for more on multi-line comments in python!" #this would execute
# This line and below would not execute
'''
Triple quotations allow us to comment across multiple lines as long as
the triple quoted comment is not the first thing in your file.
You can use double or single quotes!
'''