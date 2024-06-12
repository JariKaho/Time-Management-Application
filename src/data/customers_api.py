from flask import Flask, request
from services_customers import db_get_customers, db_get_customers_by_id, db_create_customers, db_update_customers, db_delete_customers


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return {"index": True}

@app.route('/customers', methods=['GET'])
def get_all_customers():
    try:  
        return db_get_customers()
    except:
        return {"error": "no data"}

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer_by_id(id):
    try:
        return db_get_customers_by_id(id)
    except:
        return {"error": "no customer with id %s" % id}

@app.route("/customers", methods=['POST'])
def create_customer():
    try: 
        data = request.get_json()
        name = data['name']
        db_create_customers(name)
        return {"success": "created customer: %s" % name}
    except:
        return {"error": "error creating customer"}

@app.route("/customers/<int:id>", methods=['PUT'])
def update_customer(id):
    try:
        data = request.get_json()
        name = data['name']

        db_update_customers(id, name)
        return {"success": "updated customer"}
    except:
        return {"error": "error updating customer"}

@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customers(id):
    try:
        return db_delete_customers(id)
    except:
        return {"error": "no such customer"} 

if __name__ == "__main__":
    app.run()
