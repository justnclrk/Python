from flask import Flask, redirect, render_template, request, flash, session
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'email_validation')
app.secret_key = "ThisIsSecret!"
@app.route('/')
def index():
    emails = mysql.query_db('SELECT email, created_at FROM emails')
    return render_template('index.html', all_emails=emails)
@app.route('/verified', methods=['POST'])
def validate():
    if EMAIL_REGEX.match(request.form['email']):
        flash("The email address you entered {} is a VALID email address! Thank you!".format(request.form['email']))
        query = "INSERT INTO emails (email, created_at) VALUES (:email, now())"
        data = {
            'email' : request.form['email']
        }
        mysql.query_db(query, data)
    else:
        flash("Email is NOT Valid!")
    return redirect('/')
app.run(debug=True)