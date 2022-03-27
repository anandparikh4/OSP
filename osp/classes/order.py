from mongoengine import FloatField,BooleanField,ReferenceField,StringField,ImageField,CASCADE
from osp.classes.item import Item
from osp.classes.user import Seller,Buyer

REQUEST_STATUS = ("Pending","Rejected","Accepted")

class Order:
    offer_price = FloatField(required=True,min_value=0)
    item = ReferenceField(Item,reverse_delete_rule=CASCADE,required = True)
    buyer = ReferenceField(Buyer,reverse_delete_rule=CASCADE,required = True)
    seller = ReferenceField(Seller,reverse_delete_rule=CASCADE,required = True)
    request_status = StringField(default="Pending",choices = REQUEST_STATUS)
    delivery_status = BooleanField(default = False)
    payment_status = BooleanField(default = False)

    @staticmethod
    def create_order(**kwargs):
        try:
            new_order = Order

    def negotiate(self, offer):
        try:
            if offer < 0:
                raise Exception("Please enter a valid offer price")
            self.offer_price = offer
            return True, "Offer placed"

        except Exception as e:
            return False, str(e)

class Transaction:
    offer_price = FloatField(required = True, min_value=0)
    item_name = StringField(required=True, min_length=1)
    item_id = StringField(required=True,min_length=1)
    buyer_name = StringField(required=True,min_length=1)
    buyer_id = StringField(required=True,min_length=1)
    seller_name = StringField(required=True,min_length=1)
    seller_id = StringField(required=True,min_length=1)
    photo = ImageField(size=(300,300,True),required=True)
    category_name = StringField(required=True,min_length=1)
    category_id = StringField(required=True,min_length=1)

    @staticmethod
    def create_transaction(order):
        new_transaction =