from mongoengine import Document,StringField,EmailField,IntField,ReferenceField,NULLIFY,CASCADE
from osp.classes.address import Address

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




