from mongoengine import Document,StringField,IntField,ImageField,BooleanField

class Item(Document):
    name = StringField(required=True,min_length=1)
    photo = ImageField(size=(300,300,True),required=True)
    price = IntField(required=True,min_value=1)
    age = IntField(default=0)
    descr = StringField(default="")
    manufacturer_name = StringField(required=True,min_length=1)
    isheavy = BooleanField(required=True)
