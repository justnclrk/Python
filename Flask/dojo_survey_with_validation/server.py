from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def survey_page():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def survey_result():
    error = False
    if len(request.form['name']) < 1:
        flash("Please enter your name!")
        error = True
    if len(request.form['location']) < 1:
        flash("Please enter your location!")
        error = True
    if len(request.form['lang']) < 1:
        flash("Please enter your favorite language!")
        error = True
    if len(request.form['comm']) > 121:
        flash("Your comment can't be longer than 120 characters!")
        error = True
    if error == True:
        return render_template('index.html')
    else:
        return render_template('results.html', name=request.form["name"], location=request.form["location"], lang=request.form["lang"], comm=request.form["comm"])
app.run(debug=True)