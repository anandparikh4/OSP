<<<<<<< HEAD
from mongoengine import Document,StringField,IntField,ImageField,BooleanField,ReferenceField, CASCADE, FloatField
from osp.classes.category import Category, Seller

class Item(Document):
    item_id = StringField()
    name = StringField(required=True,min_length=1)
    seller = ReferenceField(Seller,required=True,reverse_delete_rule=CASCADE)
    category = ReferenceField(Category, reverse_delete_rule=CASCADE)
    photo = ImageField(size=(300,300,True),required=True)
    price = FloatField(required=True,min_value=1)
    age = IntField(default=0)
    descr = StringField(default="")
    manufacturer_name = StringField(required=True,min_length=1)
    is_heavy = BooleanField(required=True)

    def add_item(self, **kwargs):
        try:
            self.item_id = str(self.id)
            self.name = kwargs['name']
            self.seller = kwargs['seller']
            self.photo = kwargs['photo']
            self.price = kwargs['price']
            self.age = kwargs['age']
            self.descr = kwargs['descr']
            self.manufacturer_name = kwargs['manufacturer_name']
            self.is_heavy = kwargs['is_heavy']
            self.category = kwargs['category']
            self.save()
            self.item_id = str(self.id)
            self.save()
            return True,"Item added successfully"
        except Exception as ex:
            return False, str(ex)

    def remove_item(self):
        try:
            self.delete()
            return True,"Deleted successfully"
        except Exception as ex:
            return False, str(ex)

    def change_details(self,**kwargs):
        try:
            if 'name' in kwargs:
                self.name = kwargs['name']

            if 'price' in kwargs:
                self.price = kwargs['price']

            if 'age' in kwargs:
                self.age = kwargs['age']

            if 'category' in kwargs:
                self.category = kwargs['category']

            if 'descr' in kwargs:
                self.descr = kwargs['descr']

            if 'photo' in kwargs:
                self.photo = kwargs['photo']

            if 'manufacturer_name' in kwargs:
                self.manufacturer_name = kwargs['manufacturer_name']

            return True, "Changed item details successfully"
        except Exception as ex:
            return False, str(ex)
    @staticmethod
    def search(category_search, name_search):
        if category_search == "all":
            return Item.objects(name__icontains=name_search)
        else:
            return Item.objects(category=category_search, name__icontains=name_search)


    class Sold_Products(Document):
        name = StringField(required=True)
        seller_name = StringField(required=True)
        buyer_name = StringField(required=True)
        sale_price = FloatField(required=True,min_value=1)
=======
from mongoengine import Document,StringField,IntField,ImageField,BooleanField,ReferenceField, CASCADE, FloatField
from osp.classes.category import Category, Seller

class Item(Document):
    item_id = StringField()
    name = StringField(required=True,min_length=1)
    seller = ReferenceField(Seller,required=True,reverse_delete_rule=CASCADE)
    photo = ImageField(size=(300,300,True),required=True)
    price = FloatField(required=True,min_value=1)
    age = IntField(default=0)
    descr = StringField(default="")
    manufacturer_name = StringField(required=True,min_length=1)
    is_heavy = BooleanField(required=True)
    category = ReferenceField(Category,reverse_delete_rule=CASCADE)

    def add_item(self, **kwargs):
        try:
            self.item_id = str(self.id)
            self.name = kwargs['name']
            self.seller = kwargs['seller']
            self.photo = kwargs['photo']
            self.price = kwargs['price']
            self.age = kwargs['age']
            self.descr = kwargs['descr']
            self.manufacturer_name = kwargs['manufacturer_name']
            self.is_heavy = kwargs['is_heavy']
            self.category = kwargs['category']
            self.save()
            self.save()
            return True,"Item added successfully"
        except Exception as ex:
            return False, str(ex)

    def remove_item(self):
        try:
            self.delete()
            return True,"Deleted successfully"
        except Exception as ex:
            return False, str(ex)

    @staticmethod
    def search(category_search, name_search):
        if category_search == "all":
            return Item.objects(name__icontains=name_search)
        else:
            return Item.objects(category=category_search, name=name_search)
        
>>>>>>> b4ea49406a7a3fb2a2c32801d7a1bce7fd55e690
