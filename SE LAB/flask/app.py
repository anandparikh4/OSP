from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/customer_signup")
def cust_signup():
    return render_template('customer_signup.html')

@app.route("/manager_signup")
def man_signup():
    return render_template('manager_signup.html')

if __name__ == "__main__":
    app.run(debug = True)
