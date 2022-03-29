from app import app
from functools import wraps
from flask import json, render_template, jsonify, make_response, send_file, request, redirect, flash, current_app
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from decouple import config
from osp.classes.user import User,Buyer,Seller,Manager
from osp.classes.address import Address

#app.secret_key = config["SECRETKEY"]   # make it secret
app.secret_key = "secret_key"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "sign_in"

@login_manager.user_loader
def load_user(userid):
    return User.objects(uid = userid).first()

def is_manager(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if (current_user.is_anonymous) or current_user.type != "Manager":
            flash("Please login as a Manager to access this page!")
            return redirect("/sign_in")
        return f(*args, **kwargs)
    return decorated

def is_seller(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if (current_user.is_anonymous) or current_user.type != "Seller":
            flash("Please login as a Seller to access this page!")
            return redirect("/sign_in")
        return f(*args, **kwargs)
    return decorated

def is_buyer(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if (current_user.is_anonymous) or current_user.type != "Buyer":
            flash("Please login as a Buyer to access this page!")
            return redirect("/sign_in")
        return f(*args, **kwargs)
    return decorated

@app.route("/home")
@app.route("/")
def home():

    if current_user.is_anonymous:
        return redirect("/sign_in")

    elif current_user.type() == "Manager":
        return redirect("/manager")

    elif current_user.type() == "Seller":
        return redirect("/seller")

    elif current_user.type() == "Buyer":
        return redirect("/buyer")

    return redirect("/sign_in")


@app.route("/sign_up", methods=["GET" , "POST"])
def sign_up():
    req = request.form

    try:
        if request.method == "POST":
            success = False

            obj = Address(residence_number=req["residenceno"], street = req["street"], locality = req["locality"], pincode = req["pincode"], state = req["state"], city = req["city"])
            print(obj)
            obj.save()

            if req["type"] == "buyer":
                success, obj = Buyer.create_buyer(password = req["password"] , name = req["name"] , email = req["email"] , address = obj, telephone = req["telephone"])

            elif req["type"] == "seller":
                success, obj = Seller.create_seller()

            if success == True:
                flash(obj, "info")

            else:
                flash("Unsuccessful sign up", "error")
                flash(obj, "error")

    except Exception as ex:
        flash("Invalid entries! Sign-up failed" , "error")
        return redirect("/welcome")  # change back to sign in

    return render_template("sign_up.html")

@app.route("/welcome" , methods = ["GET" ,"POST"])
def welcome():
    return render_template("welcome.html")


