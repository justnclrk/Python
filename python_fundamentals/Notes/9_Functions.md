Functions
A function is a named block of code that we can execute to perform a specific task. More simply, a function is a list of instructions that you can run at any time. If you find something that you seem to be using over and over again, it might be best to have a way to streamline the process. A function can optionally take in parameters, perform a series of instructions, and optionally return something afterwards. Here's an example:

def add(a,b):
  x = a + b
  return x
# the return value gets assigned to the "result" variable
result = add(3,5)
print result # this should print 8
Think of the function as a factory. If we were building a new car we would:

Acquire raw materials (variables) needed for creating a car.
Send the raw materials(invoke and pass arguments) to a car manufacturing plant (function)
Do something (process) with the raw materials(parameters)
Drive the car (function's return value)


The factory has all the instructions to build a new car and will perform all the tasks. When you want a new car, all you have to do is call the factory to request a new car.

The advantages of using functions are:

Reducing the duplication of code
Breaking down complex problems into simpler pieces
Improving clarity of code
Syntax
Pay attention to a few details. The def keyword signifies the declaration of a function. This indicates that the following code is a function and assigns a name to that function, so we can call it later. Parameters are information we input into a function, and appear inside the parenthesis that follow the function name.

Here's a basic example of a function:

# we've named the function 'add' and we give it two parameters(inputs to the function)
def add(a,b):
  x = a + b
  return x  # we return something (more on this later)
We have declared a function with the def keyword, named it add, and it takes two inputs (parameters). An important thing to know is that the above code does not actually invoke the function; it just declares it. Once you've defined your function, we can execute it by invoking or calling it using () after the function name.

print add(3,5) #prints 8
Once invoked, a function can give us an output. Some functions take an input and some functions don't give us an output. Even if no output is produced, the code inside the function can alter the program - this is called a side effect. Based upon what we learned above, a function that doesn't return anything would produce no output!

Function Parameters
We define the input of functions using parameters. Like we've seen before, some functions do not have to take parameters. However, functions can optionally have one or more parameters.

We've defined the say_hi function with one parameter called name

# this function has one parameter(input)
def say_hi(name):
  print "Hi, " + name
Now, we can invoke this function by calling its name and passing in the correct number of arguments:

# invoking the function passing in one argument
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')
Wait, but what's the difference between a parameter and an argument? These two words get mixed up a lot in programming. In this example 'name' is a parameter while "Michael", "Andrew", and "Jay", are arguments. We define parameters. We pass in arguments into functions.

Here's the output:



Returning Values
So far none of our functions had any value that we could hold onto. In many cases, we would want our function to return some sort of value that we can use later in our program. The following concept is critical in understanding how to use functions correctly in your code:

It is very important to remember the following: a functional call is equal to whatever that function returns. This might not make sense until we see it in action.

Let's modify our original say_hi function and observe the differences:

def say_hi():
  return "Hi"
greeting = say_hi() #the returned value from say_hi function gets assigned to the 'greeting' variable
print greeting # this will output 'Hi'
Returning a value from a function allows us to store that value in a variable. In this example, we invoked the say_hi function and set it to the greeting variable. When we print greeting we see that it contains the returned value of the say_hi function - "Hi'

Going back to our add function, recall that it takes two parameters and returns the sum of the parameters.

def add(a, b):
  x = a + b
  return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2
What do you think the values of sum1, sum2, and sum3 would be?

If you guessed 10, 5, and 15, respectively, good job! sum1 was set to the return value of the add function invoked with 4 and 6 as arguments. Similarly, sum2 was set to the return value of invoking add with 1 and 4. The variable sum3 contains the sum of sum1 and sum2 which is 15. Storing these return values in variables allows us to use the results of our functions throughout the rest of our program.

In our examples you may have noticed that our functions were returning values of different data types. Functions can return any of the data types - strings, numbers, lists, tuples, dictionaries and even other functions!