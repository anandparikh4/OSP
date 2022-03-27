from mongoengine import Document,StringField,EmailField,IntField,DateField,ReferenceField,NULLIFY,CASCADE
from osp.classes.address import Address
from osp.classes.item import Item
from osp.classes.category import Category
from osp.classes.order import Order,Transaction,REQUEST_STATUS

TYPE = ("Manager" , "Buyer" , "Seller")
GENDER = ("Male" , "Female" , "Others")

class User(Document):
    uid = StringField()
    password = StringField(minlength = 8,required = True)
    name = StringField(required = True,minlength = 1)
    email = EmailField(required = True)
    address = ReferenceField(Address,required=True,reverse_delete_rule=NULLIFY)
    telephone = IntField(required=True, min_value=1000000000, max_value=9999999999)

    meta = {'allow_inheritance' : True}

    def change_data(self,**kwargs):
        try:
            if "name" in kwargs :
                self.name = kwargs["name"]
            if "email" in kwargs:
                self.email = kwargs["email"]
            if "address" in kwargs:
                self.address = kwargs["address"]
            if "telephone" in kwargs:
                self.telephone = kwargs["telephone"]
            self.save()
            return (True, "Profile information updated successfully")

        except Exception as ex:
            return False, str(ex)

    def change_password(self,oldpass, newpass):
        try:
            if oldpass != self.password :
                raise Exception("Wrong password!")
            self.password = newpass
            self.save()
            return True, "Password changed"

        except Exception as e:
            return False,str(e)


class Manager(User):
    gender = StringField(required=True, choices=GENDER)
    dob = DateField(required=True)

    @staticmethod
    def create_manager(**kwargs):
        uid = kwargs["uid"]


    def type(self):
        return "Manager"

    @staticmethod
    def signup_key():                       # mimicking static variables
        return str("for_managers_only")


    def change_category(self, item_id, category_id):

        try:
            item_ = Item.objects(uid=item_id).first()
            if not item_:
                raise Exception("No such item found!")

            category_ = Category.objects(uid=category_id).first()
            if not category_:
                raise Exception("No such item found!")

            item_.category = category_
            item_.save()
        except Exception as e:
            return False,str(e)


    # for adding and removing categories, the static add and remove categories of the class Category can be used directly. No special methods are required in class Manager
    # similarly for deleting items, the static method delete item of class Item can be used directly


    def manage_seller(self,seller_id):
        try:
            seller = Seller.objects(uid=seller_id).first()
            if seller:
                seller.delete()
                return True, "Seller deleted"
            else :
                raise Exception("No such seller found")

        except Exception as e:
            return  False, str(e)

    def manage_buyer(self, buyer_id):
        try:
            buyer = Buyer.objects(uid=buyer_id).first()
            if buyer:
                buyer.delete()
                return (True, "Buyer deleted")
            else:
                raise Exception("No such buyer found")

        except Exception as e:
            return  False, str(e)


    #def audit(self):    # implement after class Buy Requests

    #def negotiations(self,seller_id,buyer_id):   # implement after class Buy Requests


class Seller(User):
    # for adding and deleting products, static methods of Class Item can be used
    def view_pending_orders(self):
         return Order.objects(seller=self)

    def view_sales(self):
         return Transaction.objects(seller = self)

    def negotiate(self,order,offer):
        try:
            order.negotiate(offer)
            return True,"Offer Placed"

        except Exception as ex:
            return False, str(ex)
                                                    # _order is an object of class Order
    def update_order_status(self,_order,status):   # status is an enumeration of REQUEST_STATUS

        _order.request_status = status
        if status == "ACCEPTED":




















