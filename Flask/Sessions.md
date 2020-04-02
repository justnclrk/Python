Sessions
We will continue to use our "form_test" project example during this chapter so make sure you have gone through the previous tabs and created that project before moving on.

In this example, we will learn how to pass data between routes. Currently, we have a route that handles the form submit but it doesn't do anything with that data in terms of presenting it to the view.

First, let's create a route in our form_test project that serves a page and supplies the page with a name and email to display.

Add the following route to your server.py file:

@app.route('/show')
def show_user():
  return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')
Now this means that we'll have to create a user.html view that displays the name and email that are passed to it.

/form_test/templates/user.html
<html>
  <head>
    <title>Form Test Show</title>
  </head>
  <body>
    <h1>User:</h1>
    <h3>{{name}}</h3>
    <h3>{{email}}</h3>
  </body>
</html>
Now test out your application by navigating to localhost:5000/show and checking to see if everything works! Note that right now we are hard-coding the name and email instead of using the user-input from the form.

Now let's make it so that submitting the form will somehow store the POST data so that we can access it from our show_user function. In order to do this, we will need to use Session

Session: What is it? What does it do? Why do I need it?
Well, to answer these questions we must first remember back to your first Coding Dojo lecture about the HTTP request/response cycle. You might remember that your browser makes a request to a URL and receives a response from the web server, displaying the HTML, CSS and JavaScript in your browser.

Let's take that notion one step further. In a normal user's interaction with a web site, that user will usually make tens, if not hundreds, of requests to a given web server.

Think about it: You're doing your holiday shopping online. While filling your shopping cart with the gifts you've selected you will do the following:

Visit the home page of your retailer of choice
Log into your account
Submit search queries
Browse the items from the resulting list
View select items in detail
Add certain items to your shopping cart
Check out
Receive confirmation of your order
Each one of those steps along the way is a full HTTP request/response cycle. It begins with your browser sending a request, and ends with the browser rendering a response from the server.

Now, here's the thing about the HTTP request/response cycle. It is stateless. That means that each request/response cycle instance is independent and ignorant of any instances that came before or will come after it.

This matters because, along with each request, your favorite retailer always knows and remembers:

Who you are (your account)
What you've searched for
The items in your cart
etc...
So how does the site know this if each HTTP request/response cycle instance is stateless?

Sites like your favorite online retailer make use of persistent data storage!

Persistent data storage can come in many forms, like a database, which you will learn about soon enough. It can also come in the form of writing to a file, and that's what session does!

Now we know that a given HTTP request/response is stateless, but in the scope of a given req/res cycle, we can read certain pieces of data that we stored in previous cycles, and write certain valuable pieces of data for use in future cycles. This opens up a new world of user experience. With session, the user can have a conversation of sorts with a web site where a user makes decisions that can be tracked so that a server can respond appropriately to create a better user experience.

In a given process (HTTP request/response), data is created (search terms and search results for instance) that OUTLIVES the process that generated it. That data must be kept track of for use in subsequent processes. This data is called state. State allows our site to "know" a lot of useful information. Information like:

Is there a logged in user currently?
Who is the current logged in user?
What links a user has viewed previously
Any other datapoint necessary
That last point is important. Session is a tool for you, the developer, to use to your advantage. The same way you create variables in your functions to help you solve problems, you keep state data in session to help you solve problems down the line, like in subsequent HTTP request/response cycle instances.

So persistent data storage, like session, helps us bridge the gap between a stateless protocol like HTTP with the stateful data generated through it. The combination of the two is at the heart of the modern web and heavily used by web developers around the world.

Cookies vs Databases
You've probably heard of the term cookies before. Frameworks like Flask use cookies to store data like sessions. Flask uses secure hashing of session data to send a packet of information from server to client. This packet is known as a cookie. Once your browser has received this cookie, it writes the information contained in it to a small file on your hard drive.

Comparing/Contrasting Types Of Data Persistence
When developers design a framework they must decide where sessions should be stored. While Flask developers decided to leverage the power of cookies for storing session data, there are certain performance and security compromises being made. Other Frameworks, like Django, choose to store session data in the database, sending only secure keys that can be used to retrieve data from a database only when required.

It is important to realize that, along with many other things in web development, we must sometimes make informed decisions about how we chose to solve a problem. When you are told something works a certain way, you should ask yourself what other solutions to that problem exist and why this solution was chosen.

Determining what data to store and where/how to store it is subject to many considerations. System architecture, data sensitivity, data lifecycle, scope, just to name a few. Knowing more about your meta-data, that is, the data ABOUT your data as well as the differences between the common types of persistent storage is critical to architecting the optimal solution for your requirements. 

Persistent storage type	Lifespan	Common example
Database	Permanent until manually deleted	
(encrypted) Passwords
(encrypted) Credit Card Info
Photos
Cookies	Set per browser settings	
User selected language
Using session in your app
This is how our server.py currently looks:

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # notice how the key we are using to access the info corresponds with the names
   # of the inputs from our html form
   name = request.form['name']
   email = request.form['email']
   return redirect('/') # redirects back to the '/' route
@app.route('/show')
def show_user():
  return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')
app.run(debug=True)
The first thing we need to do to enable session is to import it from Flask!

Add session to your list of imports on the top line:

from flask import Flask, render_template, request, redirect, session
Sessions also require a secret key to run so you'll have to set a secret key in your server.py as follows:

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
Now change your create_user function to use session:

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # here we add two properties to session to store the name and email
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   return redirect('/show') # noticed that we changed where we redirect to so that we can go to the page that displays the name and email!
Previously in our show_user function, we didn't have access to the name and email from the form submission. Now using session we can access the name and email stored from one function in another!

Let's modify our show_user function to use session instead of hard-coding the data:

@app.route('/show')
def show_user():
  return render_template('user.html', name=session['name'], email=session['email'])
Now test out your application!

Submitting the form takes you to the POST /users route which is handled by the create_user function where we store the POST data in session
The create_user function then redirects you to the GET /show route which is handled by the show_user function where we render the user.html template passing along the necessary information to the view
We can also access session in our templates!
Right now we are passing the information stored in session to the templates using named arguments. Instead, we can access session directly from the templates!

First, let's streamline our show_user function:

@app.route('/show')
def show_user():
  return render_template('user.html')
And now let's use session in our templates:

/form_test/templates/user.html
<html>
  <head>
    <title>Form Test Show</title>
  </head>
  <body>
    <h1>User:</h1>
    <h3>{{session['name']}}</h3>
    <h3>{{session['email']}}</h3>
  </body>
</html>
Now that you know how to use sessions, let's go over what we learned:
Session is a way to store information unique to a particular client
Session uses cookies to store some or all of the required information
When you want to access and modify data over multiple redirects use session
You can use session in both your server.py file as well as your templates
Even though you have access to the session, you should not abuse the amount of information you store in it. Store only what you need in the session. Once we incorporate a database you should be limiting what you store in sessions to the most minimal amount of data possible.