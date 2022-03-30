import sys
sys.path.append(".")

from osp import Address

print("#### Testing empty fields in address ####\n")
try:
    Address(residence_number="", street="", locality="", pincode="", state="", city="").save()
    print("FAILED: Incorrect address entered.")
except Exception as e:
    for key, value in e.__dict__["errors"].items():
        print(f"{key}: {value}")
    print("PASSED: Exceptions raised successfully.\n")


print("#### Testing valid fields in address (should raise exceptions) ####\n")
try:
    Address(residence_number="D/704, Lodha Meridian", street="Kukatpally", locality="KPHB", city="Hyderabad", state="Andhra Pradesh", pincode="500072").save()
    print("PASSED: Correct address saved successfully.")
except Exception as e:
    for key, value in e.__dict__["errors"].items():
        print(f"{key}: {value}")
    print("FAILED: Correct address raised exceptions.\n")