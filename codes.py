import random

# Functions that manage generation of codes

# 1-time Manager Codes
def generateManagerCode():
	num = ""
	for i in range(4):
		num += random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])

	# To do: store final number in database

	return num

# Return new code if success, 0 if fail
def checkManagerCode(manager_code):
	# To do: check for code in database
	if True:
		return generateManagerCode()
	else:
		return 0

# Items Codes