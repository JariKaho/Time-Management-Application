from flask import Flask, request
from services_hours import db_get_working_hours, db_get_working_hours_by_id, db_create_hour_entry, db_update_hour_entry, db_delete_hour_entry, db_delete_hour_entry

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return {"index": True}

@app.route('/workinghours', methods=['GET'])
def get_all_working_hours():
    try:  
        return db_get_working_hours()
    except:
        return {"error": "no data"}

@app.route('/workinghours/<int:id>', methods=['GET'])
def get_working_hours_by_id(id):
    try:
        return db_get_working_hours_by_id(id)
    except:
        return {"error": "no work hour entry with id %s" % id}

@app.route("/workinghours", methods=['POST'])
def create_hour_entry():
    try: 
        data = request.get_json()
        customerID = data['customerID']
        employeeID = data['employeeID']
        startTime = data['startTime']
        endTime = data['endTime']
        lunchBreak = data['lunchBreak']
        db_create_hour_entry(customerID, employeeID, startTime, endTime, lunchBreak)
        return {"success": "created work hour entry:"}
    except:
        return {"error": "error creating work hour entry"}

@app.route("/workinghours/<int:id>", methods=['PUT'])
def update_hour_entry(id):
    try:
        workingHourID = id
        customerID = data['customerID']
        employeeID = data['employeeID']
        startTime = data['startTime']
        endTime = data['endTime']
        lunchBreak = data['lunchBreak']
        data = request.get_json()
        db_update_hour_entry(workingHourID, customerID, employeeID, startTime, endTime, lunchBreak)
        return {"success": "updated hour entry"}
    except:
        return {"error": "error updating hour entry"}

@app.route('/workinghours/<int:id>', methods=['DELETE'])
def delete_hour_entry(id):
    try:
        return db_delete_hour_entry(id)
    except:
        return {"error": "no such hour entry"}

if __name__ == "__main__":
    app.run()
