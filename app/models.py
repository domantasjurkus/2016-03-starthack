from app import db

class ManagerCode(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	value = db.Column(db.Integer)

	def __init__(self, value):
	    self.value = value

	def __repr__(self):
	    return '<ManagerCode %r>' % self.value
