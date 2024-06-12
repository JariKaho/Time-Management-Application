from flask import Flask, request
from services import db_get_employees, db_get_employee_by_id, db_create_employee, db_update_employee, db_delete_employee
app = Flask(__name__)

# Employees #

@app.route("/", methods=["GET"])
def index():
    return {"index": True}

@app.route('/employees', methods=['GET'])
def get_all_employees():
    try:  
        return db_get_employees()
    except:
        return {"error": "no data"}

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id):
    try:
        return db_get_employee_by_id(id)
    except:
        return {"error": "no employee with id %s" % id}

@app.route("/employees", methods=['POST'])
def create_employee():
    try: 
        data = request.get_json()
        name = data['name']
        db_create_employee(name)
        return {"success": "created employee: %s" % name}
    except:
        return {"error": "error creating employee"}

@app.route("/employee/<int:id>", methods=['PUT'])
def update_employee(id):
    try:
        data = request.get_json()
        name = data['name']

        db_update_employee(id, name)
        return {"success": "updated employee"}
    except:
        return {"error": "error updating employee"}

@app.route('/employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    try:
        return db_delete_employee(id)
    except:
        return {"error": "no such employee"}
    
if __name__ == "__main__":
    app.run()
