from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/bodymassindex")
@app.route("/savingsgoal")
def home():
    return render_template("home.html")



if __name__ == '__main__':
    app.run(debug=True)