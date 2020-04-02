Strings
Strings are any sequence of characters (letters, numerals, ~($/}\#, etc.) enclosed in single or double quotes. You can display a string like this:

print "this is a sample string"
Printing Strings using Variables
There are multiple ways that you can print a string containing data from variables.

The first is by adding a comma after the string, followed by the variable. Note that the comma is outside the closing quotation mark of the string. Print inserts a space between elements separated by a comma.

name = "Zen"
print "My name is", name
The second is by concatenating the contents into a new string, with the help of +.

name = "Zen"
print "My name is " + name
There is one other difference between concatenating using a plus and using a comma, can you find out what it is?

Hint: try concatenating a string with an integer using each method.

Lastly, you can use curly brackets - {} - and the string .format() method to inject variables into your string - this is known as string interpolation.

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)
Above the string "Zen" is inserted where the first curly bracket is and the string "Coder" where the second curly bracket is. There should be a corresponding number of curly brackets and arguments passed to the .format() function

As you read other people's code, you may see a different method of string interpolation. It is a lesser-used and soon-to-be deprecated method that you should know about, but will not need to use.

hw = "hello %s" % 'world'
print hw
# the output would be:
# hello world
There are several variations and tricks with each method, which have changed according to the Python version you are using. The developers of Python have yet to decide on how best to implement string interpolation for Python. Exciting stuff. Stay tuned. Python 3.6 is set to implement a new string interpolation method.

Built-In String Methods
String methods are functions that we can run on a string. We already showed you one above, the .format() method. Here's how to use these methods:

x = "Hello World"
print x.upper()
# output:
"HELLO WORLD"
The following is a list of commonly used string methods:
string.count(substring): returns number of occurrences of substring in string.
string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.
string.find(substring): returns the index of the start of the first occurrence of substring within string.
string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
string.split(): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
It's important to know that there are built-in methods for every data type, and to have a general idea of what they can do. Try experimenting with them in the shell to see what they can do. Don't spend time trying to memorize them, though. You can always look up whatever you need to use.

Click here for a list of Python's built-in string methods.