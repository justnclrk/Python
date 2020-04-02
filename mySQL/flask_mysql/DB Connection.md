MySQL Connection
In this chapter, we are going to teach you how to connect to MySQL by using a Python module named mysql-connector. Keep in mind while you are going through this chapter that we have provided you with a connection file so that you can learn how to interact with the database and run certain commands through an interface that we are providing. You do not need to understand how to create the connection file (you will by the end of the bootcamp, we promise!) but you do need to understand how it works.

The first step in connecting to the database is installing the mysql-connector-python module. In your terminal, with your project-specific virtual environment active, run the following command:

For Mac OS users:
IF YOU HAVE ERRORS WITH THE BELOW LINES READ ON FOR THE FIX:
pip install MySQL-python==1.2.5
pip install Flask-SQLAlchemy==2.1
RUN THIS LINE IF YOU GET AN ERROR FROM 'pip install MySQL-python':
For Mac/Linux users: 

brew install mysql-connector-c
For PC users:

pip install Flask-SQLAlchemy==2.1 mysqlclient==1.3.4
First, create a database called "mydb" that has a users table with a name field. Add 2-3 users using MySQLWorkbench so that you can test out the connection.

Now create a new project called "flask_mysql" and create a server.py file and a mysqlconnection.py file. 
mysqlconnection.py will be the file that connects to MySQL using the MySQL-python module we installed earlier

/flask_mysql/mysqlconnection.py
""" import the necessary modules """
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
# Create a class that will give us an object that we can use to connect to a database
class MySQLConnection(object):
    def __init__(self, app, db):
        config = {
                'host': 'localhost',
                'database': db, # we got db as an argument
                'user': 'root',
                'password': 'root',
                'port': '3306' # change the port to match the port your SQL server is running on
        }
        # this will use the above values to generate the path to connect to your sql database
        DATABASE_URI = "mysql://{}:{}@127.0.0.1:{}/{}".format(config['user'], config['password'], config['port'], config['database'])
        app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        # establish the connection to database
        self.db = SQLAlchemy(app)
    # this is the method we will use to query the database
    def query_db(self, query, data=None):
        result = self.db.session.execute(text(query), data)
        if query[0:6].lower() == 'select':
            # if the query was a select
            # convert the result to a list of dictionaries
            list_result = [dict(r) for r in result]
            # return the results as a list of dictionaries
            return list_result
        elif query[0:6].lower() == 'insert':
            # if the query was an insert
    	    # commit changes
            self.db.session.commit()
            # return the id of the row that was inserted
            return result.lastrowid
        else:
            # if the query was an update or delete, return nothing and commit changes
            self.db.session.commit()
# This is the module method to be called by the user in server.py. Make sure to provide the db name!
def MySQLConnector(app, db):
    return MySQLConnection(app, db)
/flask_mysql/server.py
from flask import Flask
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query
print mysql.query_db("SELECT * FROM users")
app.run(debug=True)
Note that we are not handling any routes on our server.py file. Instead, when we run "python server.py" we should see our users printed to the terminal.

First, run the application to make sure that you are getting your users from the database. 

Things to know about the connection:
Read all of the comments in the connection file to fully understand what is going on. Note that you don't need to know how to create one of these files -- instead, you should know how to use the file and by the end of the bootcamp, you will be experienced enough to create your own connection files.


Privacy Policy