import psycopg2
from psycopg2.extras import RealDictCursor
from config import config
import json

def db_get_working_hours():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'SELECT * FROM WorkingHours;'
        cursor.execute(SQL)
        data = cursor.fetchall()
        cursor.close()
        
        # Convert datetime fields to strings
        for row in data:
            if 'startTime' in row:
                row['startTime'] = row['startTime'].isoformat()
            if 'endTime' in row:
                row['endTime'] = row['endTime'].isoformat()

        return {"workinghour_list": data}
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Database error: {error}")
        return None
    finally:
        if con is not None:
            con.close()

def db_get_working_hours_by_id(id):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'SELECT * FROM WorkingHours where id = %s;'
        cursor.execute(SQL, (id,))
        row = cursor.fetchone()
        cursor.close()
        return json.dumps(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def db_create_hour_entry(customerID, employeeID, startTime, endTime, lunchBreak):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'INSERT INTO WorkingHours (customerID, employeeID, startTime, endTime, lunchBreak) VALUES (%s, %s, %s, %s, %s);'
        cursor.execute(SQL, (customerID, employeeID, startTime, endTime, lunchBreak))
        con.commit()
        result = {"success": "created working hour entry"}
        cursor.close()
        return json.dumps(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def db_update_hour_entry(workingHourID, customerID, employeeID, startTime, endTime, lunchBreak):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = """UPDATE WorkingHours SET customerID = %s, employeeID = %s, startTime = %s, endTime = %s, lunchBreak = %s 
              WHERE id = %s;"""
        cursor.execute(SQL, (customerID, employeeID, startTime, endTime, lunchBreak, workingHourID))
        con.commit()
        cursor.close()
        result = {"success": "updated work hour entry id: %s " % workingHourID}
        return json.dumps(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def db_delete_hour_entry(workingHourID):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'DELETE FROM WorkingHours WHERE id = %s;'
        cursor.execute(SQL, (workingHourID,))
        con.commit()
        cursor.close()
        result = {"success": "deleted work hour entry id: %s " % id}
        return json.dumps(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

if __name__ == '__main__':
    pass