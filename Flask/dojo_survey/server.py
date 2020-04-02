from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route('/')
def survey_page():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def survey_result():
    return render_template('results.html', name=request.form["name"], location=request.form["location"], lang=request.form["lang"], comm=request.form["comm"])


app.run(debug=True)
