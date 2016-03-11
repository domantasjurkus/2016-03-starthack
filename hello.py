from flask import Flask, render_template
app = Flask(__name__)

from codes import generateManagerCode

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/codes')
def codes():
	manager_code = generateManagerCode()
	return manager_code

if __name__ == '__main__':
    app.run(debug=True)