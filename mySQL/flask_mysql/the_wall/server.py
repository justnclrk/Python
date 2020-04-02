from flask import Flask, redirect, render_template, request, flash, session
from mysqlconnection import MySQLConnector
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'the_wall')
app.secret_key = "ThisIsSecret!"


@app.route('/')
def index():
    users = mysql.query_db(
        'SELECT first_name, last_name, email, password, created_at, updated_at FROM users')
    return render_template('index.html', all_users=users)


@app.route('/register', methods=['POST'])
def register():
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
            'first_name': fname,
            'last_name': lname,
            'email': email,
            'password': password
        }
        mysql.query_db(query, data)
        flash("Login info submitted, thank you!")
        return redirect('/wall')


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    query = "SELECT * FROM users WHERE users.email = :email AND users.password = :password"
    data = {
        'email': email,
        'password': password
    }
    user = mysql.query_db(query, data)
    if len(user) == 0:
        flash("Login Failed: email and/or password invalid please try again")
        return redirect('/')
    session['uid'] = user[0]['id']
    session['first_name'] = user[0]['first_name']
    return redirect('/wall')


@app.route('/wall')
def wall():
    if 'uid' not in session:
        return redirect('/')
    messages_query = "SELECT users.id AS poster_id, users.first_name AS poster_first_name, messages.id AS post_id, messages.message AS post, messages.created_at FROM users JOIN messages on users.id = messages.user_id ORDER BY messages.id DESC"
    messages = mysql.query_db(messages_query)
    comments_query = "SELECT users.id AS commenter_id, users.first_name AS commenter_first_name, comments.comment AS comment, message_id AS post_id, comments.created_at FROM comments JOIN users ON comments.user_id = users.id"
    comments = mysql.query_db(comments_query)
    return render_template('wall.html', messages=messages, comments=comments)


@app.route('/messages', methods=["POST"])
def message():
    wall_message = request.form['wall_message']
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, now(), now())"
    data = {
        'user_id': session['uid'],
        'message': wall_message,
    }
    mysql.query_db(query, data)
    return redirect('/wall')


@app.route('/comment', methods=["POST"])
def comment():
    comment = request.form['comment']
    message_id = request.form['message_id']
    query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, now(), now())"
    data = {
        'user_id': session['uid'],
        'message_id': message_id,
        'comment': comment
    }
    mysql.query_db(query, data)
    return redirect('/wall')


@app.route('/logout')
def logout():
    del session['uid']
    return redirect('/')


app.run(debug=True)
