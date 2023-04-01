import datetime
import mysql.connector
import random
import string

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="car_hire_system"
)
cursor = db.cursor()

# Generate random string of specified length
def generate_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Create list of dummy customers
def create_dummy_customers(num_customers):
    global cursor
    query = "SELECT * FROM customers"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return "Customers already exist"
    else:
        for i in range(num_customers):
            first_name = generate_string(8)
            last_name = generate_string(10)
            email = first_name + '.' + last_name + '@example.com'
            phone = ''.join(random.choice(string.digits) for i in range(10))

            # DATABASE INSERTION
            query = "INSERT INTO customers (first_name,last_name,email, phone_number) VALUES (%s, %s, %s, %s)"
            values = (first_name, last_name ,email, phone)
            cursor.execute(query, values)
            db.commit()
        return "Customers created successfully"
    

def create_dummy_vehicles_types(num_vehicles):
    global cursor
    query = "SELECT * FROM vehicle_types"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return "Vehicle_types already exist"
    else:
        types=["small car","family car","van"]
        capacities=[4,7,None]
        for i in range(3):
            type_name=types[i]
            capacity=capacities[i]

            # DATABASE INSERTION
            query = "INSERT INTO vehicle_types (type_name, capacity)  VALUES (%s, %s)"
            values = (type_name, capacity)
            cursor.execute(query, values)
            db.commit()
        return "Vehicle_types created successfully"
    
def create_dummy_vehicles(num_vehicles):
    global cursor
    query = "SELECT * FROM vehicles"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return "Vehicles already exist"
    else:
        for i in range(num_vehicles):
            type_id=random.randint(1,3)
            available=random.choice([True,False])

            # DATABASE INSERTION
            query = "INSERT INTO vehicles (type_id, available)  VALUES (%s, %s)"
            values = (type_id, available)
            cursor.execute(query, values)
            db.commit()
        return "Vehicles created successfully"

def create_dummy_bookings(num_bookings):
    global cursor
    query = "SELECT * FROM bookings"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return "Bookings already exist"
    else:
        for i in range(num_bookings):
            customer_id=random.randint(1,10)
            vehicle_id=random.randint(1,10)
            hire_date=datetime.date(2021,random.randint(1,12),random.randint(1,28))
            return_date=hire_date+datetime.timedelta(days=random.randint(1,7))
            total_cost=random.randint(1,1000)

            # DATABASE INSERTION
            query = "INSERT INTO bookings (customer_id, vehicle_id, hire_date, return_date, cost)  VALUES (%s, %s, %s, %s, %s)"
            values = (customer_id, vehicle_id, hire_date, hire_date, total_cost)
            cursor.execute(query, values)
            db.commit()
        return "Bookings created successfully"

# Example usage: create 10 dummy customers
customers = create_dummy_customers(10)
cursor.nextset()

# Example usage: create 3 dummy vehicle types
Vehicle_types = create_dummy_vehicles_types(3)
cursor.nextset()

# Example usage: create 10 dummy vehicles
vehicles = create_dummy_vehicles(10)
cursor.nextset()

# Example usage: create 10 dummy bookings
bookings = create_dummy_bookings(10)
cursor.nextset()


# Print the results
print(customers)
print(Vehicle_types)
print(vehicles)
print(bookings)
