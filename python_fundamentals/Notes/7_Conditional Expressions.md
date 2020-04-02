Conditional Expressions
Conditional statements or expressions in Python can be done using if (and else) just like in other programming languages. We use these conditional statements with logic operators to control the flow of our programs. 

# if statement:
if <condition>:
  # do something
# if-else statement:
elif <condition>:
  # do something
else:
  # do this instead
Say, for example, you were driving home and there was some construction on the road in front of you. You notice a detour sign and decide to take that way back instead. Although it was practically a subconscious decision, this illustrates how we use control flow and conditionals in everyday life to determine what we would do based on certain conditions. Our if-else statement would look like this:

If there is construction
{ 
     use detour 
}
else
{
     take the normal route
}

Here's another example but now written out in python code:

age = 15
if age >= 18:
  print 'Legal age'
else:
  print 'You are so young!'
The if and if-else statements in Python are straightforward and are very much like the if statements in other languages. The only difference with Python's if statement is, when you have another condition, you write it using elif.

if age >= 18:
  print 'Legal age'
elif age == 17:
  print 'You are seventeen.'
else:
  print 'You are so young!'
elif is just like else if or elsif from other languages.

Comparison and Logic Operators
Here is a table of the comparison operators you can use in your Python programs.

Operator	Description	Example
-------
==	| Checks if the value of two operands are equal or not, if yes then condition becomes true.	| (1 == 2) is not true. (1 == 1) is true. 
-------
!= |	Checks if the value of two operands are equal or not, if values are not equal then condition becomes true. |	(1 != 2) is true.
-------
<> |	Checks if the value of two operands are equal or not, if values are not equal then condition becomes true. |	(1 <> 2) is true. This is similar to != operator.*
-------
>	| Checks if the value of left operand is greater than the value of right operand, if yes then condition becomes true.	| (1 > 2) is not true.
-------
< |	Checks if the value of left operand is less than the value of right operand, if yes then condition becomes true. |	(1 < 2) is true.
-------
>= |	Checks if the value of left operand is greater than or equal to the value of right operand, if yes then condition becomes true. |	(1 >= 2) is not true.
-------
<= | Checks if the value of left operand is less than or equal to the value of right operand, if yes then condition becomes true.	| (1 <= 2) is true.
-------
and | Checks each expression on the left and right. If both are true then this evaluates true. If either or both expressions are false then this is false	(1 <= 2 and 2 <= 3) is true. |
(1 <= 2 and 2 >= 3) is false. 
(1 >= 2 and 2 >= 3) is false. 
-------
or | Checks each expression on the left and right. If either of the expressions are true then this evaluates true. If both expressions are false then this is false. |	(1 <= 2 or 2 >= 3) is true. 
(1 <= 2 or 2 <= 3) is true. 
(1 >= 2 or 2 >= 3) is false. 
-------
not | Reverses the true-false value of the operand	not(true) is false. |
not(false) is true. 
not(1 >= 2) is true. 
not(1 <= 2) is false. 
not(1 <= 2 and 2 <= 3) is false. 
not(1 >= 2 or 2 >= 3) is true. 
-------
*Note: != can also be written <>, but this is an obsolete usage kept for backwards compatibility only. New code should always use !=.  Documentation can be found here.