SELECT Basics
First, let's go over how we can SELECT data from a database. First, import the twitter.sql into your MySQL workbench. The twitter.sql file contains the SQL statements to create a database called twitter along with certain tables and pre-populated fields. 

Remember that you are learning a new language. Watch the videos once, then watch it a second time following along. Also, make sure you run all of the commands listed out in this tab. Even though you might understand it conceptually, it is important that we type the commands so we can retain our knowledge.


Import From twitter.sql
Go ahead and download the  twitter.sql file. Copy and paste what is in the .sql file into your MySQL Workbench editor. The ERD of the database is as follows:



users 
Let's see what's in the users table by running:

SELECT * 
FROM users;


faves
Let's see what's in the faves table by running:

SELECT * 
FROM faves;


follows
Let's see what's in the follows table by running:

SELECT *  
FROM follows;


tweets
Let's see what's in the tweets table by running:

SELECT *
FROM tweets;


Basics
What query would you run to get all of the users?

SELECT * 
FROM users;
What query would you run to only get the first names of all of the users?
SELECT first_name 
FROM users;
What query would you run to only get the first and last names of all of the users? 
SELECT first_name, last_name
FROM users;
SELECT w/ Conditionals
What query would you run to only get the first name of users with id of 2?

SELECT first_name
FROM users
WHERE id = 2;
What query would you run to get the last names of users with id of 2 or 3?

SELECT last_name
FROM users
WHERE id = 2 OR id = 3;
What query would you run to get all of the users with id greater than 2?
SELECT *
FROM users
WHERE id > 2;
What query would you run to get all of the users with id less than or equal to 3?
SELECT *
FROM users
WHERE id <= 3;
What query would you run to get all of the users with first names ending in "e"?
SELECT * 
FROM users
WHERE first_name LIKE "%e";
What query would you run to get all of the users with first names starting in "K"?
SELECT * 
FROM users
WHERE first_name LIKE "K%";
SELECT w/ Sorting
What query would you run to get all of the users with the youngest users at the top of the table?

SELECT *
FROM users
ORDER BY birthday DESC;
What query would you run to get all of the users with the oldest users at the top of the table?

SELECT *
FROM users
ORDER BY birthday ASC;
What query would you run to get all of the users with the first name that ends with "e" with the youngest users at the top of the table?

SELECT *
FROM users
WHERE first_name LIKE "%e"
ORDER BY birthday DESC;
copy
What query would you run to get only the first names of all of the users in alphabetical order?

SELECT first_name
FROM users
ORDER BY first_name;
The default for ORDER BY is ASC so we can leave that part out if we want the sorting to be ascending.

Note
Before moving on to the next tab, it will be best to go over the following tutorials on SQL Zoo:

SELECT Basics: http://sqlzoo.net/wiki/SQLZOO:SELECT_basics
SELECT name: http://sqlzoo.net/wiki/SELECT_names
SELECT from World: http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial