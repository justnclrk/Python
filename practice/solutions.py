from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"


@app.route('/')
def index():
    # Question 1
    # l = []
    # for i in range(2000, 3201):
    #     if (i % 7 == 0) and (i % 5 != 0):
    #         l.append(str(i))

    #     print ','.join(l)
    # Question 2
    return "hello world!"


app.run(debug=True)
