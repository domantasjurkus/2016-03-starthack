from app import db


class ManagerInformationsss(db.Model):
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


class ReturnedOrdersss(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    orderNumber = db.Column(db.String(100))
    lineNumber = db.Column(db.Integer())
    storeAddress = db.Column(db.String(120))
    storeName = db.Column(db.String(70))

    def __init__(self, orderNumber, lineNumber, storeName, storeAddress):
        self.orderNumber = orderNumber
        self.lineNumber = lineNumber
        self.storeName = storeName
        self.storeAddress = storeAddress

    def __repr__(self):
        return '<ReturnedItems %s:%s>' % (self.orderNumber, self.lineNumber)
