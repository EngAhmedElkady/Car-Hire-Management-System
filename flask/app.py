from cgitb import reset
from operator import le
from unittest import result
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="car_hire_system"
)

@app.route('/customer', methods=['POST'])
def add_customer():
    if 'first_name' not in request.json or 'last_name' not in request.json or 'email' not in request.json or 'phone_number' not in request.json:
        return jsonify({'message': 'Missing data'}), 400
    
    cursor = db.cursor()
    email=request.json['email']
    cursor.execute("SELECT * FROM customers WHERE email=%s", (email,))
    result = cursor.fetchall()
    if len(result) > 0:
        return jsonify({"message": "Email already exists"})

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    phone_number = request.json['phone_number']
    query = "INSERT INTO customers (first_name,last_name,email, phone_number) VALUES (%s, %s, %s, %s)"
    values = (first_name, last_name ,email, phone_number)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    return jsonify({'message': 'Customer added successfully'})

@app.route('/customer/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM customers WHERE customer_id=%s", (customer_id,))
    result = cursor.fetchall()

    if len(result) == 0:
        return jsonify({"message": "Customer_id not found"})
        
    first_name = result[0][1]
    last_name = result[0][2]
    email = result[0][3]
    phone_number = result[0][4]
    
    if 'first_name' in request.json:
        first_name = request.json['first_name']
    if 'last_name' in request.json:
        last_name = request.json['last_name']
    if 'email' in request.json:
        email = request.json['email']
        cursor.execute("SELECT * FROM customers WHERE email=%s", (email,))
        result = cursor.fetchall()


        if len(result)>0 and result[0][3] == email:
            return jsonify({"message": "Email already exists"})
    if 'phone_number' in request.json:
        phone_number = request.json['phone_number']

    query = "UPDATE customers SET first_name=%s,last_name=%s,email=%s, phone_number=%s WHERE customer_id=%s"
    values = (first_name,last_name, email, phone_number,str(customer_id))
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    return jsonify({'message': 'Customer updated successfully'})

    
@app.route('/customer/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM customers WHERE customer_id=%s", (customer_id,))
    result = cursor.fetchall()
    if len(result) == 0:
        return jsonify({"message": "Customer_id not found"})
    
    # find the bookings of the customer
    cursor.execute("SELECT * FROM bookings WHERE customer_id=%s", (customer_id,))
    result = cursor.fetchall()
    if len(result) > 0:
        query = "DELETE FROM bookings WHERE customer_id=%s"
        values = (customer_id,)
        cursor.execute(query, values)
        db.commit()
  
    query = "DELETE FROM customers WHERE customer_id=%s"
    values = (customer_id,)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    return jsonify({'message': 'Customer deleted successfully'})



@app.route('/customer/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer_id = int(customer_id)
    try:
        cursor = db.cursor()
        query = "SELECT * FROM customers WHERE customer_id=%s"
        values = (customer_id,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        if result:
            customer = {
                'id': result[0],
                'first_name': result[1],
                'last_name': result[2],
                'email': result[3],
                'phone_number': result[4]
            }
            return jsonify(customer)
        else:
            return jsonify({'message': 'Customer_id not found'})
    except Exception as e:
        return jsonify({"message": "Customer_id not found"})

if __name__ == '__main__':
    app.run(debug=True)
