MySQL Communication
You are all familiar with writing queries. You should be proud! Writing queries is the hard part. Displaying the information to the page is fairly easy. You will still be writing queries the exact same way that you already have been, but we will be adding a few additional steps so that you'll be set up to communicate with the database via your Python.

Let's create a very simple webpage where we can track all of our friends! We will implement the functionality to add friends and view friends through the website. All friends will be stored in the database. For this application, we won't have login/registration.

First, create your database using the following sql file: friends.sql

And consider the following ERD:

Screen-Shot-2015-08-24-at-3.20.17-PM

Now let's start creating our sample application.

As always we will start with our server.py file. Let's first make the app work with hard coded data and then we will add the back end.

For your file structure make sure that, in addition to your server.py file, you have the mysqlconnection.py file and a templates folder with an index.html file.

Call your project "friends".

/friends/server.py
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/friends', methods=['POST'])
def create():
    # add a friend to the database!
    return redirect('/')
app.run(debug=True)
And now for our Index.html

/friends/templates/index.html
<html>
<head>
  <title>Friends</title>
</head>
<body>
  <h1>These are all my friends!</h1>
  <p>First Name: Jay</p>
  <p>Last Name: Patel</p>
  <p>Occupation: Instructor</p>
  <hr>
  <p>First Name: Jimmy</p>
  <p>Last Name: Jun</p>
  <p>Occupation: Instructor</p>
  <hr>
  <h2>Add a Friend</h2>
  <form action='/friends' method='POST'>
    <label for="first_name">First Name:<input type="text" name="first_name" id="first_name"></label>
    <label for="last_name">Last Name:<input type="text" name="last_name" id="last_name"></label>
    <label for="occupation">Occupation:<input type="text" name="occupation" id="occupation"></label>
    <input type="submit" value="Add">
  </form>
</body>
</html>
Note that for now, we have just hard coded our friends and submitting our form will just redirect us to the page we are already on.

Fetching Friends
First, let's add a few friends into our database manually through MySQL Workbench. This will allow us to have some seed data that we can use to create and test functionality to display all friends from the database.

INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)
VALUES ("Jay", "Patel", "Instructor", NOW(), NOW());
INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)
VALUES ("Jimmy", "Jun", "Instructor", NOW(), NOW());
Test that you successfully added the two friends into the database using a select query in MySQL Workbench:

SELECT * FROM friends; # Should display two friends
Now that you have added the friends let's try to query the database for them from our base route. Update your route like this:

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print friends
    return render_template('index.html')
Notice how we use the mysql object's query_db function and pass in the query that we would like to run.

Observing Results
Make sure to restart the application and check that you see your friends printed out in the terminal. Take a moment to examine how our query returned data. It should look something like this:



The fetch method returns us an array of dictionaries where each dictionary represents a row in the table. For each dictionary, the keys correspond to the column names and the values correspond to that entry's value.

There are a couple things that may look new:

the 'u' that precede each key or value that is a string. The 'u' indicates a Unicode string that is inherently different from the simple string type. Unicode is used to represent a wider variety of languages and symbols. (Ex.á or ü). For our purposes, they work exactly as strings
the 'L' append to each value for the 'id' field in each dictionary. This represents a 'long' which is a type to store numbers in memory. The 'long' type is more accurate but will behave exactly as an int.
Displaying Results
Now let's display the data on the index.html page. As you remember we can pass data to the view using named parameters in the render_template function. Let's go ahead and pass the whole friends array to the template:

@app.route('/')
def index():
    query = "SELECT * FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our template
Again, this is just passing the query into the query_db function. Now on our index.html page, we will have to display all of the friends using embedded python.

Replace the hardcoded friends on index.html with the following to display friends using embedded python in the template:

<!-- we can use the line below to see all of our data in our template -->
{{ all_friends }}
<h1>These are all my friends!</h1>
<!-- with all the data we can then construct a more structured output -->
{% for friend in all_friends: %}
   <p>ID: {{ friend['id'] }}</p>
   <p>First Name: {{ friend['first_name'] }}</p>
   <p>Last Name: {{ friend['last_name'] }}</p>
   <p>Occupation: {{ friend['occupation'] }}</p>
   <hr>
{% endfor %}
Now if you test out your application again, you will see all of your friends being loaded from the database! Try adding a friend manually through MySQL Workbench and test that the page loads it.

Inserting Data into Queries
Now, if we wanted a route to fetch a specific user we would have to modify the query of fetching all the users slightly:

@app.route('/friends/<friend_id>')
def show(friend_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id}
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', one_friend=friends[0])
Notice how we are grabbing the friend_id from the URL and passing that into the function as the same name as the URL parameter, friend_id.

Important! We are using the format :variable_name to inject values into a query string. This is a way of asking SQL Alchemy to parse the values being inserted into our string in order to protect against any suspicious looking data. Hackers use something known as SQL injection to attack sites. Imagine if a hacker typed "DELETE FROM users WHERE id > 0" into one of your input fields. Without a method of inspecting user entered data for such attacks our whole database would have been destroyed. When we pass a separate dictionary to the execute method found in our MySQLConnection file we are allowing the SQL Alchemy module to take care of this job for us.

Inserting Records
Now that we can retrieve friends we have to add the functionality that allows us to create a friend! Let's focus in on our '/friends' route which will handle adding a friend and then redirect to the base route which already retrieves all friends and displays them.
First, let's make sure that we are properly getting all of the data from the form:
@app.route('/friends', methods=['POST'])
def create():
    print request.form['first_name']
    print request.form['last_name']
    print request.form['occupation']
    # add a friend to the database!
    return redirect('/')
Now try adding a friend and see if the information gets printed to the terminal. Inputting "Andrew Lee Instructor" should print the following to the terminal:

Andrew
Lee
Instructor
Now that we know that the information successfully gets to the server, let's insert it into the database using our MySQL object:

@app.route('/friends', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')
Notice again, we just pass the query into the MySQL object's query_db function.

Updating Records
Say we wanted to update a specific record, we could create another page and add a form that would submit to the following route:

@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'],
             'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/')
Nothing fancy, just posting to a route with a URL parameter - friend_id and using that friend_id in our update query.

Deleting Records
@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')
Now you know how to interact with the database using the mysqlconnection.py file!