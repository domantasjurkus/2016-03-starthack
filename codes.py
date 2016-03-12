import random
from app import db
from app.models import ManagerCodes

# Functions that manage generation of codes

# Generate 4 digit code
def generateCode():
	num = ""
	for i in range(4):
		num += random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
	return num

# 1-time Manager Codes
def generateManagerCode():
	num = generateCode()

	# To do: store final number in database
	db.session.add(ManagerCodes(num))
	db.session.commit()

	codes = ManagerCodes.query.all()

	code_list = []
	for code in codes:
		code_list.append(code.value)

	return code_list

# Return new code if success, 0 if fail
def checkManagerCode(manager_code):
	# To do: check for code in database
	if True:
		return generateManagerCode()
	else:
		return 0

# Items Codes