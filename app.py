from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello World!'
    
@app.route('/hello')
def hello():
    return 'Hello'

@app.route('/world')
def world():
    return 'World'
    
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    return f"user: {request.form['username']} Password: {request.form['password']}"

@app.route('/item')
def item():
    item_id = request.args.get('item_id', default = 1, type = int)
    return f"/transactionid is={item_id}"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
    