from app import app
from flask import render_template,redirect,url_for,request,flash
import mongoengine as ming
#from osp.classes.user import User
from osp.classes.address import Address
from osp.interface.sign_up import buyer_sign_up,seller_sign_up


# manager routes
@app.route("/manager" , methods = ["GET" ,"POST"])
def manager():
    return render_template("manager/manager.html")

@app.route("/manager/manage_buyers" , methods = ["GET" ,"POST"])
def manage_buyers():
    return render_template("manager/manage_buyers.html")

@app.route("/manager/manage_sellers" , methods = ["GET" ,"POST"])
def manage_sellers():
    return render_template("manager/manage_sellers.html")

@app.route("/manager/audit" , methods = ["GET" ,"POST"])
def audit():
    return render_template("manager/audit.html")

@app.route("/manager/help_negotiations" , methods = ["GET" ,"POST"])
def help_negotiations():
    return render_template("manager/help_negotiations.html")


# seller routes
@app.route("/seller" , methods = ["GET" ,"POST"])
def seller():
    return render_template("seller/seller.html")

@app.route("/seller/buy_requests" , methods = ["GET" ,"POST"])
def buy_requests():
    return render_template("seller/buy_requests.html")

@app.route("/seller/items" , methods = ["GET" ,"POST"])
def items():
    return render_template("seller/items.html")

@app.route("/seller/upload_item" , methods = ["GET" ,"POST"])
def upload_item():
    return render_template("seller/upload_item.html")

@app.route("/seller/sales" , methods = ["GET" ,"POST"])
def sales():
    return render_template("seller/sales.html")


# buyer routes

@app.route("/buyer" , methods = ["GET" ,"POST"])
def buyer():
    return render_template("buyer/buyer.html")

@app.route("/buyer/purchase_requests" , methods = ["GET" ,"POST"])
def purchase_requests():
    return render_template("buyer/purchase_requests.html")

@app.route("/buyer/purchases" , methods = ["GET" ,"POST"])
def purchases():
    return render_template("buyer/purchases.html")

@app.route("/dashboard" , methods = ["GET" ,"POST"])
def dashboard():
    return render_template("dashboard.html")



