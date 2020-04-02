Dictionaries
A Dictionary is another mutable set type that can store any number of Python objects, including other set types. Dictionaries consist of pairs (called items) of keys and their corresponding values. While this data structure is known as a dictionary in Python, you'll see the same structure referred to as an associative array or hash table in other languages. In general, hash table is the most generic term.

The following is a general summary of the characteristics of a Python dictionary:

A dictionary is an unordered collection of objects.
Values are accessed using a key.
A dictionary can shrink or grow as needed.
The contents of dictionaries can be modified.
Dictionaries can be nested.
Sequence operations such as slice cannot be used with dictionaries.
Creating Dictionaries
Creating a dictionary in Python is a little bit like creating any other set. There are 3 types of sets in Python. You've already learned about lists and tuples. While lists are enclosed by brackets – [], and tuples are enclosed by parenthesis – (), dictionaries are enclosed by braces – {} and use keys to track position rather than an index. Below are a couple of techniques you'll find useful when building dictionaries.

weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
In the example above, we created two dictionaries in two different ways:

Using literal notation. The key-value pairs are enclosed by curly brackets. The pairs are separated by commas. The first value of a pair is a key, which is followed by a colon character and a value. The "Sun" string is a key and the "Sunday" string is a value.
Creating empty dictionary and adding some values. The keys are inside the square brackets, the values are located on the right side of the assignment.
Each key in a dictionary must be unique. If you make an assignment using an existing key as the index, the old value associated with that key is overwritten by the new value. You can use this characteristic to an advantage in order to modify an existing value for an existing key.

Accessing Values
To access the values of a dictionary, you can use the familiar square brackets along with the key to obtain its value.

print weekend["Sun"]
print capitals["svk"]
Or use the for loop to access all keys and values.

#to print all keys
for data in capitals:
     print data
#another way to print all keys
for key in capitals.iterkeys():
     print key
#to print the values
for val in capitals.itervalues():
     print val
#to print all keys and values
for key,data in capitals.iteritems():
     print key, " = ", data
Built-in Functions and Methods
Python includes the following standalone functions for dictionaries:

cmp(dict1, dict2) - Compares two dictionaries. The comparison process starts with the length of each dictionary, followed by key names, followed by values. The function returns 0 if the two dicts are equal, -1 if dict1 > dict2, 1 if dict1 < dict2.
len() - give the total length of the dictionary.
str() - produces a string representation of a dictionary.
type() - returns the type of the passed variable. If passed variable is a dictionary, it will then return a dict type.
Python includes the following dictionary methods:
(either dict.method(yourDictionary) or yourDictionary.method() will work)

.clear() - removes all elements from the dictionary
.copy() - returns a shallow copy dictionary
.fromkeys(sequence, [value] ) - create a new dictionary with keys from sequence and values set to value.
.get(key, default=None) - For key key, returns value or default if key is not in dictionary.
.has_key(key) - returns true if a given key is available in the dictionary, otherwise it returns false.
.items() - returns a list of dictionary's (key, value) tuple pairs.
.keys() - return a list of dictionary keys.
.setdefault(key, default=None) - similar to get(), but will set dict[key]=default if key is not already in dictionary.
.update(dict2) = adds dictionary dict2's key-values pairs to an existing dictionary.
.values() - returns list of dictionary values.
Nested Dictionaries
Nesting is also allowed in dictionaries. Dictionaries may contain lists and tuples.

context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }
To iterate the values, we can use the nested for loop:

for key, data in context.items():
     #print data
     for value in data:
          print "Question #", value["id"], ": ", value["content"]
          print "----"
The result is like this...

Question # 1 :  Why is there a light in the fridge and not in the freezer?
----
Question # 2 :  Why don't sheep shrink when it rains?
----
Question # 3 :  Why are they called apartments when they are all stuck together?
----
Question # 4 :  Why do cars drive on the parkway and park on the driveway?
----
Lists from Dictionary
It's possible to create lists from dictionaries by using the methods items(), keys() and values(). As the name implies the method keys() creates a list, which consists solely of the keys of the dictionary. While values() produces a list consisting of the values. items() can be used to create a list consisting of 2-tuples of (key, value)-pairs:

data ={"house":"Haus","cat":"Katze","red":"rot"}
print data.items()
#[('house', 'Haus'), ('cat', 'Katze'), ('red', 'rot')]
print data.keys()
#['house', 'cat', 'red']
print data.values()
#['Haus', 'Katze', 'rot']
Dictionaries from Lists
For example, we have two lists, one containing the dishes and the other, the corresponding countries:

dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
Now we will create a dictionary, which assigns a dish to a country (of course according to the common prejudices). For this purpose, we need the function zip(). The name zip was well chosen because the two lists get combined like a zipper.

country_specialities = zip(countries, dishes)
print country_specialities
#Result is...
#[('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]
The variable country_specialities now contains the "dictionary" in the 2-tuple list form. This form can be easily transformed into a real dictionary with the function dict().

country_specialities_dict = dict(country_specialities)
print country_specialities_dict
#Result is...
#{'Germany': 'sauerkraut', 'Spain': 'paella', 'Italy': 'pizza', 'USA': 'hamburger'}
There is still one question concerning the function zip(). What happens, if one of the two argument lists contains more elements than the other one? It's easy: The superfluous elements will not be used, whether the extras are keys or values:

countries = ["Italy", "Germany", "Spain", "USA", "Switzerland"]
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
country_specialities = zip(countries,dishes)
print country_specialities
#Result is...
#[('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]
copy
Notice Switzerland is dropped from the set of keys.