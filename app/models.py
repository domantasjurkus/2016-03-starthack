from app import db


class ManagerInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    storeName = db.Column(db.String(70))
    storeAddress = db.Column(db.String(120))
    value = db.Column(db.String(5), unique=True)

    def __init__(self, storeName, storeAddress, value):
        self.storeName = storeName
        self.storeAddress = storeAddress
        self.value = value

    def __repr__(self):
        return '<ManagerCodes %s %s %s >' % (self.storeName, self.storeAddress, self.value)


class CustomerCodes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(5), unique=True)

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<CustomerCodes %r>' % self.value
