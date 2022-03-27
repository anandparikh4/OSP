from mongoengine import Document,StringField,IntField,ImageField,BooleanField,ReferenceField, CASCADE, FloatField
from osp.classes.category import Category, Seller


class Item(Document):
    uid = StringField()
    name = StringField(required=True,min_length=1)
    seller = ReferenceField(Seller,required=True,reverse_delete_rule=CASCADE)
    category = ReferenceField(Category, reverse_delete_rule=CASCADE)
    photo = ImageField(size=(300,300,True),required=True)
    price = FloatField(required=True,min_value=1)
    age = IntField(default=0)
    descr = StringField(default="")
    manufacturer_name = StringField(required=True,min_length=1)
    is_heavy = BooleanField(required=True)


    @staticmethod
    def add_item(**kwargs):
        try:
            new_item = Item(kwargs['name'],kwargs['seller'],kwargs['category'],kwargs['photo'],kwargs['price'],kwargs['age'],kwargs['descr'],kwargs['manufacturer_name'],kwargs['is_heavy'])
            new_item.save()
            new_item.uid = str(new_item.id)
            new_item.update()
            return True, "Item added successfully"
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
        uid = StringField()
        name = StringField(required=True)
        seller_name = StringField(required=True)
        buyer_name = StringField(required=True)
        sale_price = FloatField(required=True,min_value=1)
        photo = ImageField(size=(300,300,True),required=True)
        category = StringField(required=True)


        def add_sold_product(self,**kwargs):
            self.name = kwargs['name']
            self.seller_name = kwargs['seller_name']
            self.buyer_name = kwargs['buyer_name']
            self.sale_price = kwargs['sale_price']
            self.photo = kwargs['photo']
            self.category = kwargs['category']
