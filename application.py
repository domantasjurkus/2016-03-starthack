from flask import Flask, render_template, jsonify

app = Flask(__name__)

from codes import generateManagerCode

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/codes')
def codes():
	manager_code = generateManagerCode()
	return jsonify({"manager_codes":manager_code})

@app.route('/manager/add')
def add_customer(customerId):
    if True:
        db[customerId] = generateCode()
        return db[customerId]
    else:
        return False

@app.route('/customers/add')
def add_customer(customerId):
    if True:
        db[customerId] = generateCode()
        return db[customerId]
    else:
        return False

@app.route('/return/<customerId>/<managerId>')
def check_customer(customerId, managerId):


if __name__ == '__main__':
    app.run(debug=True)
