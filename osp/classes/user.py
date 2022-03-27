from mongoengine import Document,StringField,EmailField,IntField,DateField,ReferenceField,NULLIFY,CASCADE
from osp.classes.address import Address
from osp.classes.item import Item
from osp.classes.category import Category

TYPE = ("Manager" , "Buyer" , "Seller")
GENDER = ("Male" , "Female" , "Others")

class User(Document):
    uid = StringField()
    password = StringField(minlength = 8,required = True)
    name = StringField(required = True,minlength = 1)
    email = EmailField(required = True)
    address = ReferenceField(Address,required=True,reverse_delete_rule=NULLIFY)
    telephone = IntField(required = True,min_value=10000000000,max_value=9999999999)

    def change_data(self,**kwargs):
        try:
            self.name = kwargs["name"]
            self.email = kwargs["email"]
            self.address = kwargs["address"]
            self.telephone = kwargs["telephone"]
            return (True, "Profile information updated successfully")

        except Exception as e:
            return(False , str(e))

    def change_password(self,oldpass,newpass):
        try:
            if oldpass != self.password :
                raise Exception("Wrong password!")
            self.password = newpass
            return (True,"Password changed")

        except Exception as e:
            return(False,str(e))



class Manager(User):
    gender = StringField(default = "MALE" , choices = GENDER)
    dob = DateField(required = True)

    def type(self):                         # mimicking static variables
        return "Manager"

    def signup_key(self):
        key = str("for_managers_only")
        return key

    def change_category(self,item_id,category_id):

        try:
            item = Item.objects(uid = item_id)
            if not item :
                raise Exception("No such item found!")

            category = Category.objects(uid = category_id)
            if not category :
                raise Exception("No such item found!")

            item.category = category

        except Exception as e:
            return(False,str(e))

    # for adding and removing categories, the static add and remove categories of the class Category can be used directly. No special methods are required in class Manager

    # similarly for deleting items, the static method delete item of class Item can be used directly


    def manage_seller(self,seller_id):
        seller = Seller.objects(uid = seller_id)

        if seller:
            seller.delete()

        else :
            raise Exception("No such seller found")

        






