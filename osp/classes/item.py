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
            return Item.objects(category=category_search)