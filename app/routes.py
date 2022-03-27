from app import app
from flask import render_template,redirect,url_for,request
import mongoengine as ming
#from osp.classes.user import User
from osp.classes.address import Address

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market", methods=["POST"])
def market_page():
    residence_number = "1"
    street = request.form["id"]
    locality = request.form["password"]
    pincode = 395007
    state = "Gujarat"
    city = "Surat"
    _add = Address(residence_number = residence_number,street =street ,locality = locality,pincode =pincode , state = state ,city=city)
    _add.save()
    _add.save()
    return "Marketplace"

@app.route("/about/<username>")
def about_page(username):

    return f"<p>about of {username}</p>"
