from app import app
from flask import render_template,redirect,url_for,request,flash
import mongoengine as ming
#from osp.classes.user import User
from osp.classes.address import Address
from osp.interface.sign_up import buyer_sign_up,seller_sign_up

