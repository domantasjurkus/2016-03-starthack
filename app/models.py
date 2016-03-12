from app import db


class ManagerInformationss(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    desc = db.Column(db.String(140))
    storeName = db.Column(db.String(70))
    storeAddress = db.Column(db.String(120))
    returnCode = db.Column(db.String(5), unique=True)

    def __init__(self, desc, storeName, storeAddress, returnCode):
        self.desc = desc
        self.storeName = storeName
        self.storeAddress = storeAddress
        self.returnCode = returnCode

    def __repr__(self):
        return '<ManagerCodes, %s, %s, %s, >' % (self.storeName, self.storeAddress, self.returnCode)

    def serialize(self):
        return {
                "id": self.id,
                "desc": self.desc,
                "storeName": self.storeName,
                "storeAddress": self.storeAddress,
                "returnCode": self.returnCode}


class ReturnedOrders(db.Model):
    id = db.Column(db.String(100), primary_key=True)

    def __init__(self, orderId, orderNumber):
        self.id = orderNumber

    def __repr__(self):
        return '<ReturnedItems %s:%s>' % (self.id, self.orderNumber)

'''
class CustomerCodes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(5), unique=True)

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<CustomerCodes %r>' % self.value
'''
