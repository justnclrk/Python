Tuples
A Tuple is a container for a fixed sequence of data objects. The name comes from the Latin suffix for multiples: double, triple, quadruple, quintuple. Tuples are sequences, just like lists. The only difference is that tuples can't be changed -- that is, tuples are immutable. Also, while lists are defined using square brackets, tuples use parentheses. Creating a tuple is as simple as declaring different comma-separated values. Optionally you can put these values between parentheses.

For example:

tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"
A tuple can be used to group any number of items into a single compound value. Syntactically, a tuple is a comma-separated sequence of values. Although it is not necessary, it is conventional to enclose tuples in parentheses.

Another example:

dog = ("Canis Familiaris", "dog", "carnivore", 12)
Tuples are useful for representing what other languages often call records — some related information that belongs together, like your student record. There is no description of what each of these fields means, but we can guess. A tuple lets us “chunk” together related information and use it as a single thing. In the example above, we may want to store some records on animal species, where we can rely on specific positions containing a certain piece of information.

We can print the data from a tuple via an index. The index operator selects an element from a tuple.

print dog[2]
#result is: carnivore
To print all values inside a tuple, we can iterate through it using the for loop:

for data in dog:
     print data
If we try to use item assignment to modify one of the elements of the tuple, we get an error:

dog[0] = "X"
#TypeError: 'tuple' object does not support item assignment
Like strings, tuples are immutable. Once Python has created a tuple in memory, it cannot be changed. But we can add and slice tuples. See example below:

dog = dog + ("domestic",)
#result is...
#("Canis Familiaris", "Dog", "carnivore", 12, "domestic")
dog = dog[:3] + ("man's best friend",) + dog[4:]
#result is...
#("Canis Familiaris", "Dog", "carnivore", "man's best friend", "domestic")
Built-in Tuple Functions
Here are a few of the most commonly used tuple functions. You'll recognize many of these functions and methods from the list tab. Tuples are just sequences with slightly different characteristics from lists.

len(sequence): Returns the length of the given tuple.

x = (1,5,6,9,2)
print len(x)
# output:
# 5
You may recognize some of these built-in functions for sequences:
max(sequence) returns the largest value in the sequence
sum(sequence) return the sum of all values in sequence
enumerate(sequence) used in a for-loop context to return two-item-tuple for each item in the sequence indicating the index followed by the value at that index.
map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
min(sequence) returns the lowest value in a sequence.
sorted(sequence) returns a sorted sequence
You'll find that many of the built-in functions that work with lists can also work with tuples. Find the built-in tuple methods here.

Tuple as return Values
Functions can always only return a single value, but by making that value a tuple, we can effectively group together as many values as we like, and return them together. This is very useful — we often want to know some highest and lowest score, or we want to find the mean and the standard deviation, or we want to know the year, the month, and the day.

For example, we could write a function that returns both the circumference and the area of a circle of radius r:

def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)
Why tuples?
The following is a little extra information on tuples. Read on if you wish.

It's okay if you don't understand use cases for tuples at this point. Most students finish this tab wondering "Why would I ever want to use a tuple? It's like a list but less flexible!" At first glance, tuples might seem like they're more trouble than they're worth.

In reality, tuples can store grouped information in such a way that any consumer of your code, i.e. other developers, can't modify sets of data that should be kept constant. Let's take an example.

I've written a code base called "Anna's Cool Python Language Library", and included in my library is a function, that, when invoked, returns all the translations of a word in 3 different languages. My code will return the word in 3 different languages, English, Spanish, and French. English will always be at index 0, French at index 1, and Spanish at index 2. My results might look like so:

import language
print language.translate(dog)
# output would look something like: ("dog", "chien", "perro")
With a tuple, I can write the rest of my library with the assumption that each language will be found at its original position. This guards against errors and is an understood communication to the developer that order and number of entries are important and should not be modified. Understanding when to use tuples is an advanced concept. It's good to know and important to be able to recognize why another developer might have chosen to use it in their code. You may not find a use case yourself while you're still learning the basics.