from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    query = "SELECT * FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our template
@app.route('/create', methods=['POST'])
def create():
    add_friend_query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, now(), now())"
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'occupation' : request.form['occupation']
    }
    mysql.query_db(add_friend_query, data)
    return redirect('/')
app.run(debug=True)