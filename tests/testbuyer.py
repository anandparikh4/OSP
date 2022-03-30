import sys
sys.path.append(".")

from osp.classes.user import Buyer
from osp.classes.address import Address
print("Checking the constructor")
address = Address(residence_number="D/704, Lodha Meridian", street="Kukatpally", locality="KPHB", city="Hyderabad", state="Andhra Pradesh", pincode="500072").save()
try:
    c1=Buyer(password="1234",name="test_buyer", email="iitkgp@email.com", address = address, telephone = "8886077670")
    c1.save()
    c1.uid=str(c1.id)
    c1.save()
    # We print passed if no exception occurs
    print("Passed without acception as correct parameters given")
except Exception as e:
    print("Failed",e)

print("Constructor with incorrect parameters")
try:
    c1=Buyer(password="abcd",name="", email="testemail@email.com",address = address, telephone="9")
    c1.save()
    c1.uid=str(c1.id)
    c1.save()
    print("Failed")
    Buyer.objects(uid=c1.uid).first().delete()
except:
    # Print passed if exception occurs as the main aim of this part is to print exception as wrong paramters are given
    print("passed")


print("Deletion of buyer")
try:
    Buyer.objects(uid=c1.uid).first().delete()
    print("Passed")
except Exception as e:
    print("failed",e)
