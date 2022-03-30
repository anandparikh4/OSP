import datetime
from functools import wraps

from decouple import config
from flask import render_template, request, redirect, flash
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

from app import app
from osp.classes.address import Address
from osp.classes.user import User, Buyer, Seller, Manager
from osp.interface.sign_in import signin

app.secret_key = config("SECRETKEY")   # made it secret
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
            obj.save()

            if req["type"] == "buyer":
                success, obj = Buyer.create_buyer(password = req["password"] , name = req["name"] , email = req["email"] , address = obj, telephone = req["telephone"])

            elif req["type"] == "seller":
                success, obj = Seller.create_seller(password = req["password"] , name = req["name"] , email = req["email"] , address = obj, telephone = req["telephone"])

            if success == True:
                flash("Successful sign-up", "info")
                return redirect("/sign_in")
            else:
                flash("Unsuccessful sign up", "error") #not working
                return redirect("/sign_up")

    except Exception as ex:
        flash("Invalid entries! Sign-up failed", "error") #not working
        return redirect("/sign_up")

    return render_template("sign_up.html")

@app.route("/manager_sign_up", methods=["GET", "POST"])
def manager_sign_up():
    req = request.form
    try:
        if request.method == "POST":
            if req["key"] == config("MANAGERKEY"):
                obj = Address(residence_number=req["residenceno"], street = req["street"], locality = req["locality"], pincode = req["pincode"], state = req["state"],
                              city=req["city"])
                obj.save()
                dob = datetime.datetime.strptime(req['birthday'], "%Y-%m-%d")
                success, new_manager = Manager.create_manager(password = req["password"] , name = req["name"] , email = req["email"] , address = obj, telephone = req["telephone"],
                                                              dob=dob,gender=req["gender"])
                if success == True:
                    flash("Successful sign-up", "info")
                    return redirect("/sign_in")
                else:
                    flash("Successful sign-up", "info")
                    return redirect("/manager_sign_up")
            else:
                flash("Wrong sign-up key!")
                return redirect("/manager_sign_up")
    except Exception as ex:
        flash(str(ex), "error")
        return redirect("/manager_sign_up")
    return render_template("manager_sign_up.html")

@login_manager.unauthorized_handler
def unauthorized_callback():
       return redirect("sign_in")


@app.route("/welcome" , methods=["GET", "POST"])
@login_required
def welcome():
    # flash("this is test message")
    return render_template("welcome.html")


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    req = request.form
    try:
        if request.method == 'POST':
            userid = req['userid']
            password = req['password']
            user1 = signin(userid, password, "M")
            user2 = signin(userid, password, "B")
            user3 = signin(userid, password, "S")
            if user1:
                user1.is_authenticated = True
                user1.save()
                login_user(user1)
                return redirect("/welcome")

            elif user2:
                user2.is_authenticated = True
                user2.save()
                login_user(user2)
                return redirect("/welcome")

            elif user3:
                user3.is_authenticated = True
                user3.save()
                login_user(user3)
                return redirect("/welcome")

            if ( (not user1) and (not user2) and (not user3) ):
                raise Exception("Invalid login credentials")
    except Exception as ex:
        flash("Invalid login credentials", "error")
        return render_template("sign_in.html")
    return render_template("sign_in.html")



@app.route("/sign_out")
@login_required
def logout():
    user = current_user
    user.is_authenticated = False
    user.save()
    logout_user()
    return redirect("/sign_in")

