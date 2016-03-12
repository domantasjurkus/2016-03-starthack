from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from codes import generateManagerCode
from sms import *


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/codes')
def codes():
    manager_code = generateManagerCode()
    return manager_code


@app.route("/receive_sms", methods=['GET', 'POST'])
def receive_sms():
    receiveSMS(request)

    # @app.route really wants to return a template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
