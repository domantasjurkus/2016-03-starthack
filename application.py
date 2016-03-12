from flask import Flask, render_template, jsonify
from codes import generateCode
from app import db
from app.models import ManagerCodes, CustomerCodes

app = Flask(__name__)

from codes import generateManagerCode


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/codes')
def codes():
    manager_code = generateManagerCode()
    return jsonify({"manager_codes": manager_code})


@app.route('/manager/add')
def add_manager():
    while True:
        num = generateCode()
        if len(ManagerCodes.query.filter_by(value=num)) == 0:
            db.session.add(ManagerCodes(num))
            return num


@app.route('/customers/add')
def add_customer(customerId):
    while True:
        num = generateCode()
        if len(CustomerCodes.query.filter_by(value=num)) == 0:
            db.session.add(CustomerCodes(num))
            return num


@app.route('/return/<customerId>/<managerId>')
def check_customer(customerId, managerId):
    if len(CustomerCodes.query.filter_by(value=customerId)) == 1 \
            and len(ManagerCodes.query.filter_by(value=managerId)) == 1:
        # TODO: Call their API
        customer = CustomerCodes.query.filter_by(value=customerId).first()
        manager = ManagerCodes.query.filter_by(value=managerId).first()
        db.session.delete(customer)
        db.session.delete(manager)
        db.session.commit()
        res = add_manager()
        return res
    else:
        return jsonify


if __name__ == '__main__':
    app.run(debug=True)
