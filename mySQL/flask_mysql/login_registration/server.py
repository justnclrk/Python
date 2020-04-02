from flask import Flask, redirect, render_template, request, flash, session
from mysqlconnection import MySQLConnector
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'login_registration')
app.secret_key = "ThisIsSecret!"
@app.route('/')
def index():
    users = mysql.query_db('SELECT first_name, last_name, email, password, created_at, updated_at FROM users')
    return render_template('index.html', all_users=users)
@app.route('/success', methods=['POST'])
def success():
    fname = request.form['first_name']
    lname = request.form['last_name']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    confirm = md5.new(request.form['confirm']).hexdigest()
    errors = False
    if len(fname) < 2:
        flash("First Name must be at least 2 letters!")
        errors = True
    if len(lname) < 2:
        flash("Last Name must be at least 2 letters!")
        errors = True
    if not EMAIL_REGEX.match(email):
        flash("Email must be vaild!")
        errors = True
    if len(password) < 8:
        flash('Password must be 8 characters!')
        errors = True
    if password != confirm:
        errors = True
    if errors == True:
        return redirect('/')
    else:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, now(), now())"
        data = {
            'first_name' : fname,
            'last_name' : lname,
            'email' : email,
            'password' : password
        }
        mysql.query_db(query, data)
        flash("Login info submitted, thank you!")
        return redirect('/')
@app.route('/user', methods=['POST'])
def login():
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    query = "SELECT id, first_name, last_name, created_at FROM users WHERE users.email = :email AND users.password = :password"
    data = {
        'email' : email,
        'password' : password
    }
    loggedIn_user = mysql.query_db(query, data)
    if len(loggedIn_user)>0:
        session['uid'] = loggedIn_user[0]['id']
        return render_template('user_page.html',user=loggedIn_user[0])
    else:
        flash("Login Failed: email and/or password invalid please try again")
        return redirect('/')
app.run(debug=True)