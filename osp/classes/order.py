from mongoengine import FloatField,BooleanField,ReferenceField,StringField,CASCADE
from osp.classes.item import Item
from osp.classes.user import Seller,Buyer

REQUEST_STATUS = ("Pending","Rejected","Accepted")

class Order:
    offer_price = FloatField(required = True,min_value=0)
    item = ReferenceField(Item,reverse_delete_rule=CASCADE,required = True)
    buyer = ReferenceField(Buyer,reverse_delete_rule=CASCADE,required = True)
    seller = ReferenceField(Seller , reverse_delete_rule=CASCADE,required = True)
    request_status = StringField(default="Pending",choices = REQUEST_STATUS)
    delivery_status = BooleanField(default = False)
    payment_status = BooleanField(default = False)

    def negotiate(self,offer):
        try:
            if offer < 0:
                raise Exception("Please enter a valid offer price")
            self.offer_price = offer
            return (True , "Offer placed")

        except Exception as e:
            return (False , str(e))

class Transaction:
    offer_price = FloatField(required = True,min_value=0)
    item = ReferenceField(Item,reverse_delete_rule=CASCADE,required = True)
    buyer = ReferenceField(Buyer,reverse_delete_rule=CASCADE,required = True)
    seller = ReferenceField(Seller , reverse_delete_rule=CASCADE,required = True)