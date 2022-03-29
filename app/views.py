from app import app
from functools import wraps
from flask import json, render_template, jsonify, make_response, send_file, request, redirect, flash, current_app
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from decouple import config
from osp.classes.user import User

app.secret_key = config["SECRETKEY"]   # make it secret

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


