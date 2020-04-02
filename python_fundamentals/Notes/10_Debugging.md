Debugging in Python
Debugging is an important skill in any language. We're going to reiterate a few principles your instructor may have already spoken about. It's important to be able to understand what is happening when your code runs.

You'll go a long way when debugging your code using just print statements. Although print statements will be especially key as you learn to code, they're going to be an important tool for the rest of your coding career. Without some way of visualizing your code, it's easy to lose track of what's going on. Try running the code examples below to get the most out of this lesson. Let's take a look at some code we've tried for the multiply section of the previous assignment:

def multiply(arr,num):
    for x in arr:
        x *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
>>>[2,4,10,16]
You might have discovered this problem yourself and had to work it out. Without some more information you might have had a hard time tracking down where the problem was occurring. We can get information by using print statements to display that data in the terminal.

The first thing to do is to step through your code in the order it runs and try to figure out if there are any unknowns. Let's step through the example code. What runs first? The first line is a function, so the interpreter runs in this order:

  def multiply(arr,num): #don't go inside the function until the function is called
  a = [2,4,10,16]
  b = multiply(a,5) # now our function executes; what is a function call equal to?
  print b # and the resulting value is printed
So far, we don't have too many questions. Here's what happened, in order:

declare a function
instantiate a variable whose value is a list containing integers
print the output of that function by calling it after a print statement
Now comes the first unknown. Ask yourself what is your input, and what do you expect as output. If you get unexpected results, you should work to eliminate all unknowns. Try inserting a print statement as the first line. Sometimes it's useful to insert a print just to be sure code is executing when we think it is, but more often we can get more information by displaying some data we've passed into our function. Our code should now look like this:

def multiply(arr,num):
    print arr, num
    for x in arr:
        x *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
>>>[2,4,10,16] 5
>>>[2,4,10,16]
Our output confirms that our code is doing everything we've tested for so far. Now to prove that our next line runs as expected. This line: for x in arr: indicates the start of a for loop. Let's confirm we're entering the loop, and that "x" contains the value we expect. Now our code looks like this:

def multiply(arr,num):
    print arr, num
    for x in arr:
        print x
        x *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
>>>[2, 4, 10, 16] 5
>>>2
>>>[2, 4, 10, 16]
>>>4
>>>[2, 4, 10, 16]
>>>10
>>>[2, 4, 10, 16]
>>>16
>>>[2, 4, 10, 16]
>>>[2, 4, 10, 16]
Now we know the loop is completing as expected and that, as our loop runs, x is equal to every value in the list in sequence. Now it gets a little more complicated. What should we ask ourselves next? Knowing what is the most useful thing to print is a skill you will acquire over time. Next, let's check if we're successfully changing our x value.

def multiply(arr,num):
    print arr, num # output should be [2,4,10,16] 5
    for x in arr:
        print x
        x *= num
        print x
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
>>>[2,4,10,16] 5
>>>2
>>>10
>>>4
>>>20
>>>10
>>>50
>>>16
>>>80
>>>[2, 4, 10, 16]
Now, we've learned that our loop is, indeed changing the x value. So far, so good. Next, let's ask if our array is changing when we expect it to. Our code should look like this:

def multiply(arr,num):
    print arr, num # output should be [2,4,10,16] 5
    for x in arr:
        print x
        x *= num
        print arr
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
>>>[2,4,10,16] 5
>>>2
>>>4
>>>10
>>>16
>>>[2,4,10,16]
>>>[2,4,10,16]
>>>[2,4,10,16]
>>>[2,4,10,16]
Aha! Here's some unexpected output. Now we know how to use print statements to find out where a problem is occurring. Once we've discovered that, we can make an educated guess as to what we should be searching. Formulating a good search is a skill best learned by trial and error. Try searching "unable to modify list value in for loop python"

Learning to search effectively is a skill that's built over time. Don't forget to always specify the programming language you're working with. Over time Google will learn that you're a developer, but until then, you may even have to specify that you're looking for information on the Python programming language, not trying to purchase a pet snake!

Your search will lead you to the discovery that the x in our for loop is just a pointer, and once changed, does not change the value in the array itself. How can you solve this problem?

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
>>>[10,20,50,80]
Learning to use print statements to their greatest advantage and how to correctly search for answers are not one-time skills. You can't just do this assignment and move on, or assume that we'll tell you when you need to use these skills. What we've introduced here is a skill set you'll use for every assignment in all of your code forever. Now is the time to start practicing, because the better you get, the more self-sufficient you become.

If you ever need help figuring out what to search, try collaborating with your neighbor or asking an instructor to help you out. Always remember the 20 minute rule!