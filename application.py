from flask import Flask, render_template, jsonify, request
from codes import generateUniqueCode
from app import db
from app.models import ManagerInformationsss, ReturnedOrdersss
import json


app = Flask(__name__)

from codes import generateManagerCode
from sms import *

BASE_URL = ("http://testhorizon.gothiagroup.com/"
            "eCommerceServicesWebApi_ver339/api/v3/")
API_KEY = "2d64db29fea4adbed35825365c334d75640eb92ae38020b640de66b93c952023"

@app.route("/")
def index():

    return render_template('return_form.html')


@app.route('/dashboard')
def dashboard():

    data = getTemplateStubs()

    return render_template('dashboard.html',
        data_taken=data['taken'],
        data_purchased=data['purchased'],
        data_returned=data['returned']
    )


@app.route("/log", methods=['GET'])
def log():
    global return_history
    return render_template('log.html', data=return_history)


@app.route('/solution')
def solution():

    return render_template('solution.html')

@app.route('/codes')
def codes():
    manager_code = generateManagerCode()
    return jsonify({"manager_codes": manager_code})


@app.route('/managers/add')
def add_manager():
    desc = request.args.get('desc', '')
    storeName = request.args.get('storeName', '')
    storeAddress = request.args.get('storeAddress', '')
    num = generateUniqueCode()
    manager = ManagerInformationsss(desc, storeName, storeAddress, num)
    db.session.add(manager)
    db.session.commit()
    return num


@app.route('/return/items', methods=['POST'])
def return_items():
    '''
    Given an order number, manager code, and a list of line items,
    adds the given items to the returned database
    '''
    order_number = request.form['orderNumber']
    item_numbers = request.form['itemNumbers']
    manager_code = request.form['managerCode']
    if order_number == "":
        return jsonify({"Error": "Please provide an orderNumber."})
    if item_numbers == []:
        return jsonify({"Error": "Please provide itemNumbers."})
    if manager_code == "":
        return jsonify({"Error": "Please provide a managerCode."})
    if ManagerInformationsss.query.filter_by(returnCode=managerId).count() != 1:
        return jsonify({"Error": "Manager ID not valid"})
    manager = ManagerInformationsss.query.filter_by(returnCode=manager_code)
    for item_number in item_numbers:
        db.session.add(ReturnedOrdersss(order_number, int(item_number), manager.storeName, manager.storeAddress))
    res = generateUniqueCode()  # Not atomic at this point
    manager.returnCode = res
    db.session.commit()
    return jsonify({"Status": "Good"})


@app.route('/return/', methods=['POST'])
def return_product():
    '''
    Given an order number and a manager code,
    Returns a list of all the line items of the order
    '''
    orderNumber = request.form['orderNumber']
    managerId = request.form['managerCode']

    if ManagerInformationsss.query.filter_by(returnCode=managerId).count() != 1:
        return jsonify({"Error": "Manager ID not valid"})

    r = requests.post(ARVATO_BASE + "/orders/" + orderNumber, headers={'X-Auth-Key': API_KEY})
    if r.status_code is not 200:
        return jsonify({"Error": "Not a valid order ID"})
    return r.json()["shipments"]["shipmentsItems"]

@app.route('/managers/clear')
def clear_managers():
    db.session.query(ManagerInformationsss).delete()
    db.session.commit()
    return jsonify({"Status": "Good"})

@app.route('/returns/clear')
def clear_returns():
    db.session.query(ReturnedOrdersss).delete()
    db.session.commit()
    return jsonify({"Status": "Good"})

@app.route('/managers/show')
def show_managers():
    managers = [m.serialize() for m in ManagerInformationsss.query.all()]
    print(managers)
    return jsonify({"manager_codes": managers})

@app.route('/returns/addresses')
def return_addresses():
    addresses = [(r.storeName, r.storeAddress) for r in ReturnedOrdersss.query.all()]
    return jsonify(addresses)

@app.route("/receive_sms", methods=['GET', 'POST'])
def receive_sms():
    global return_history
    receiveSMS(request, return_history)
    # @app.route really wants to return a template
    return render_template('base.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
