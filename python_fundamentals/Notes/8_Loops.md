Loops
Imagine that you are in 1st grade and you got in trouble in class for talking too much (it happened to me a lot of times). Your teacher asks you to write "I will not talk in class" 1,000 times. Yikes! If you had learned to program in kindergarten, you might have thought to write a program that uses a loop to do it for you!

In Python, like many other programming languages, loops are the way of executing a set of code repeatedly for a certain amount of iterations or until we've reached a specific condition. This is because computers are great at doing things over and over again. This could be used for something as simple as a math program that counts from 1 to 1,000,000 or iterating through the items within a list! In this section, we will be talking about the for and while loops in Python. In essence, anything you can do with one loop type, you can do with the other, but let's see how they are different.

For Loop
We use the for loop when we know how many times we have to repeat our code. You will mostly be using for loops in your programs, particularly in Python. A for loop looks like this:



with an output that looks like this:



Python's for statement iterates over the items of any sequence(list or string), in the order they appear in the sequence. In the above example, we iterated through the range from 0 to 5 (exclusive) and printed out a 'looping - ' item in the sequence. Notice how we use count as a counter/variable to refer to the current item in our loop.

More generally, here's the basic syntax of a for loop:

for <counter> in <sequence or range>:
  # do something
Looping Through a List
Often you'll find yourself wanting to loop through a list.



Here's a quick example of how you do that. If we execute this program, you'll see each value in our list printed.

4
dog
99
['list', 'inside', 'another']
hello world!
While Loops
While loops are often used when we don't know how many times we have to repeat a block of code but we know we have to do it until a certain condition is met.

Remember this for loop?



We can rewrite it as a while loop:



The basic syntax for a while loop looks like this:

while <expression>:
  # do something
Loop Control
We were introduced to control flow in the previous tabs with if and else statements. Loops, breaks and continues are all a part of control flow as well. Control flow is the cornerstone of most programming languages.

When you want finer control over your loops, use the following statements to do so.

Break


The break statement exits the current loop prematurely, resuming execution at the first post-loop statement, just like the traditional break found in C or JavaScript.

The most common use for the break is when some external condition is triggered, requiring a hasty exit from a loop. The break statement can be used in both while and for loop. When loops are nested, a break will only exit from the innermost loop.

for val in "string":
  if val == "i":
    break
  print val
The result of the sample above would be:

s
t
r
Continue


The continue statement returns the control to the beginning of the loop. The continue statement rejects -- or skips -- all the remaining statements in the current iteration of the loop, and continues normal execution at the top of the loop. The continue statement is very useful when you want to skip one or more loop iterations, but keep looping to the end.

for val in "string":
  if val == "i":
    continue
  print val
In this case, the result should be:

s
t
r
n
g
Pass
The pass statement is used when a statement is required syntactically but you do not want any command or code to execute.

class EmptyClass:
  pass
for val in my_string:
  pass
The pass statement is a null operation; nothing happens when it executes. The pass is almost never seen in final production, but can be useful in places where your code has not been completed yet.

Else
There are certain conditions that we give for every loop that we have, but what if the condition was not met and we still would like to do something if that happens? We can then use else. Yes, that is right, else in a loop.

x = 3
y = x
while y > 0:
  print y
  y = y - 1
else:
  print "Final else statement"
The output would be:

3
2
1
Final else statement
Note that this else code section is only executed if the while loop runs normally and its conditional is false (whether we never entered the while loop, or we did but eventually the conditional changed from true to false). If instead our while loop is exited prematurely because of a break or return statement, then the else code section will never be executed.

x = 3
y = x
while y > 0:
  print y
  y = y - 1
  if y == 0:
    break
else:
 print "Final else statement"
Because of the break, the above code will output the following:

3
2
1