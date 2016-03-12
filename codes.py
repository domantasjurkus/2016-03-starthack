import random

@app.route('/')
def index():
    return "Invalid Action"

@app.route('/customer/add')
def add_customer(customerId):
    if not customerId in db:
        db[customerId] = generateCustomerCode()
        return db[customerId]
    else:
        return False


@app.route('/customer/check/<customerId>')
def check_customer(customerId):
    pass


def readCodeFromManager(manager):
    '''
    Code if the manager has a code
    False otherwise
    '''
    if manager in db:
        return db[manager]
    else:
        return False


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
