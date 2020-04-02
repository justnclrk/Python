from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home_page():
    return "No ninjas here!"


@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")


@app.route('/ninjas/<color>')
def ninjas_color(color):
    if (color == "blue" or color == "orange" or color == "red" or color == "purple"):
        return render_template("ninja" + color + ".html")
    else:
        return render_template("april.html")


app.run(debug=True)
