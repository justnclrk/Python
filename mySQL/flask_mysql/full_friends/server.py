from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends1')
@app.route('/')
def index():
    friends = mysql.query_db('SELECT name, age, created_at FROM friends')   # run query with query_db()
    return render_template('index.html', all_friends=friends)               # pass data to our template
@app.route('/thefriends', methods=['POST'])
def add():
    query = "INSERT INTO friends (name, age, created_at) VALUES (:name, :age, NOW())"
    data = {
        'name' : request.form['name'],
        'age'  : request.form['age']
    }
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)