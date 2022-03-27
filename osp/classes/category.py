from mongoengine import Document,StringField

class Category(Document):
    name = StringField(required = True , min_length=1)
    uid = StringField()       # default empty, then assigned

    @staticmethod
    def add_category(name):
        try:
            new_category = Category(name = name)
            new_category.save()
            new_category.update(uid = id)
            return(True,"Category successfully created")

        except Exception as e:
            return(False,str(e))

    @staticmethod
    def delete_category(someid):
        try:
            Category.objects(uid = someid).delete()   # delete the category with that name

            return (True,"Category and corresponding items successfully deleted")
        except Exception as e:
            return (False, str(e))

