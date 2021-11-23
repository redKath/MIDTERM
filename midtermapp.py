from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy


midtermapp = Flask(__name__)

@midtermapp.route("/")
def login():
    return render_template("login.html")

@midtermapp.route("templates/registration.html", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('login'))

    # show the form, it wasn't submitted
    return render_template('registration.html')
  

if __name__ == "__main__":
    midtermapp.run(host="0.0.0.0", port=5000)
