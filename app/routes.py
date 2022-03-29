from app import app
from flask import render_template,redirect,url_for,request,flash
import mongoengine as ming
#from osp.classes.user import User
from osp.classes.address import Address
from osp.interface.sign_up import buyer_sign_up,seller_sign_up

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

'''
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
'''


@app.route("/sign_in" , methods = ["GET" ,"POST"])
def sign_in():
    req = request.form
    print(req.keys())
    return render_template("sign_in.html")


@app.route("/sign_up" , methods = ["GET" ,"POST"])
def sign_up():
    req = request.form
    print(req.keys())
    return render_template("sign_up.html")

@app.route("/manager_sign_up" , methods = ["GET" ,"POST"])
def manager_sign_up():
    req = request.form
    print(req.keys())
    return render_template("manager_sign_up.html")