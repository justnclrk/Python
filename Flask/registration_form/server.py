from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')
def reg():
    return render_template('index.html')


@app.route('/form', methods=['POST'])
def form():
    error = False
    if len(request.form['first_name']) < 1:
        flash("First Name Error!")
        error = True
    if len(request.form['last_name']) < 1:
        flash("Last Name Error!")
        error = True
    if len(request.form['email']) < 1:
        flash("Enter Email!")
        error = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Enter Valid Email!")
        error = True
    if len(request.form['password']) < 8:
        flash("Password too short")
        error = True
    if not len(request.form['password']) == len(request.form['confirm']):
        flash("Passwords not the same!")
        error = True
    if error == True:
        return render_template('index.html')
    else:
        print request.form['first_name']
        print request.form['last_name']
        print request.form['email']
        print request.form['password']
        flash("Thank you for your submission, see you in the matrix!")
        return render_template('index.html')


app.run(debug=True)
