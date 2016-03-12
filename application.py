from flask import Flask, render_template, jsonify, request
from codes import generateCode
from app import db
from app.models import ManagerInformation, CustomerCodes

app = Flask(__name__)

from codes import generateManagerCode
from sms import *


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/codes')
def codes():
    manager_code = generateManagerCode()
    return jsonify({"manager_codes": manager_code})


@app.route('/managers/add')
def add_manager():
    storeName = request.args.get('storeName', '')
    storeAddress = request.args.get('storeAddress', '')
    print(storeName)
    print(storeAddress)
    while True:
        num = generateCode()
        if ManagerInformation.query.filter_by(value=num).count() == 0:
            db.session.add(ManagerInformation(storeName, storeAddress, num))
            db.session.commit()
            return num


@app.route('/customers/add')
def add_customer():
    while True:
        num = generateCode()
        if CustomerCodes.query.filter_by(value=num).count() == 0:
            db.session.add(CustomerCodes(num))
            db.session.commit()
            return num


@app.route('/return/<customerId>/<managerId>')
def return_product(customerId, managerId):
    if CustomerCodes.query.filter_by(value=customerId).count() == 1 \
            and ManagerInformation.query.filter_by(value=managerId).count() == 1:
        # TODO: Call their API
        customer = CustomerCodes.query.filter_by(value=customerId).first()
        manager = ManagerInformation.query.filter_by(value=managerId).first()
        db.session.delete(customer)
        db.session.delete(manager)
        db.session.commit()
        res = add_manager()
        return jsonify({"New Manager Id": res})
    else:
        return jsonify({"Status": False})


@app.route('/customers/show')
def show_customers():
    customers = [c.value for c in CustomerCodes.query.all()]
    return jsonify({"customer_codes": customers})


@app.route('/managers/show')
def show_managers():
    managers = [str(m) for m in ManagerInformation.query.all()]
    print(managers)
    return jsonify({"manager_codes": managers})


@app.route("/receive_sms", methods=['GET', 'POST'])
def receive_sms():
    receiveSMS(request)
    # @app.route really wants to return a template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
