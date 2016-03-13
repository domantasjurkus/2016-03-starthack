from flask import Flask, render_template, jsonify, request
from codes import generateUniqueCode
from app import db
from app.models import ManagerInformationsss, ReturnedOrdersss
import json
import requests

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
    stores = ManagerInformationsss.query.all()
    data_returned = ReturnedOrdersss.query.all()

    return render_template('dashboard.html',
        stores=stores,
        data_returned=data_returned
    )

@app.route('/solution')
def solution():
    return render_template('solution.html')

@app.route('/managers/add')
def add_manager():
    storeName = request.args.get('storeName', '')
    storeAddress = request.args.get('storeAddress', '')
    num = generateUniqueCode()
    manager = ManagerInformationsss(storeName, storeAddress, num)
    db.session.add(manager)
    db.session.commit()
    return num


@app.route('/return/items/', methods=['POST'])
def return_items():
    '''
    Given an order number, manager code, and a list of line items,
    adds the given items to the returned database
    '''
    order_number = request.form['orderNumber']
    items = request.form.getlist('items[]')
    manager_code = request.form['managerCode']
    if order_number == "":
        return jsonify({"Error": "Please provide an orderNumber."})
    if items == []:
        return jsonify({"Error": "Please select at least one item to return."})
    if manager_code == "":
        return jsonify({"Error": "Please provide a managerCode."})
    if ManagerInformationsss.query.filter_by(returnCode=manager_code).count() != 1:
        return jsonify({"Error": "Manager ID not valid"})
    manager = ManagerInformationsss.query.filter_by(returnCode=manager_code).first()
    for item in items:
        db.session.add(ReturnedOrdersss(order_number, item, manager.storeName, manager.storeAddress))
    res = generateUniqueCode()  # Not atomic at this point
    manager.returnCode = res
    db.session.commit()
    return render_template('new_code.html', manager_code=res)
    

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

    r = requests.get(BASE_URL + "/orders/" + orderNumber, headers={'X-Auth-Key': API_KEY})
    if r.status_code is not 200:
        return jsonify({"Error": "Not a valid order ID"})
    return render_template('select_item.html', 
        items_list=r.json()["orderDetails"]["orderItems"], 
        manager_code=managerId, 
        orderNumber=orderNumber
    )

# Return entire order if on sms
@app.route('/return/sms/', methods=['POST'])
def return_product_sms():
    '''
    Given an order number and a manager code,
    Returns a list of all the line items of the order
    '''    
    orderNumber = request.form['orderNumber']
    managerId = request.form['managerCode']

    if ManagerInformationsss.query.filter_by(returnCode=managerId).count() != 1:
        return jsonify({"Error": "Manager ID not valid"})

    r = requests.get(BASE_URL + "/orders/" + orderNumber, headers={'X-Auth-Key': API_KEY})
    if r.status_code is not 200:
        return jsonify({"Error": "Not a valid order ID"})
    
    # PARSE INFO AND RETURN ALL
    json_items_list=r.json()["orderDetails"]["orderItems"]
    items_to_return = []
    for json_item in json_items_list:
        items_to_return.append(json_item['code'])

    if orderNumber == "":
        return jsonify({"Error": "Please provide an orderNumber."})
    if items_to_return == []:
        return jsonify({"Error": "Please select at least one item to return."})
    if managerId == "":
        return jsonify({"Error": "Please provide a managerCode."})
    if ManagerInformationsss.query.filter_by(returnCode=managerId).count() != 1:
        return jsonify({"Error": "Manager ID not valid"})
    manager = ManagerInformationsss.query.filter_by(returnCode=managerId).first()
    for item in items_to_return:
        db.session.add(ReturnedOrdersss(orderNumber, item, manager.storeName, manager.storeAddress))
    res = generateUniqueCode()  # Not atomic at this point
    manager.returnCode = res
    db.session.commit()
    return jsonify({"New Code": res})

@app.route('/managers/clear')
def clear_managers():
    ManagerInformationsss.query.filter(ManagerInformationsss.returnCode == 'pje8').delete()
    #db.session.query(ManagerInformationsss).delete()
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
    receiveSMS(request)
    # @app.route really wants to return a template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
