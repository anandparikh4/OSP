from osp.classes.user import Buyer,Seller,Manager


def sign_in(user_id, user_password, type):
    if type == "M":
        ans = Manager.objects(uid=user_id,password=user_password).first()

    elif type == "B":
        ans = Buyer.objects(uid=user_id,password=user_password).first()

    else:
        ans = Seller.objects(uid=user_id,password=user_password).first()

    if not ans:
        raise Exception("Invalid login credentials")

    return ans #what to return
