from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
import random  # import the random module
# The random module has many useful functions. This is one that gives a random number in a range


@app.route('/')
def game():
    if "magic_number" not in session:
        session["magic_number"] = random.randrange(0, 101)
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return render_template('game.html')


@app.route('/reset', methods=['POST'])
def reset():
    session["magic_number"] = random.randrange(0, 101)
    return redirect('/')


app.run(debug=True)
