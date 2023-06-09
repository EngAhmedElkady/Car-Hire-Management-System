# Car-Hire-Management-System

This is a car hire management system that allows users to hire cars and also manage the cars that are available for hire. The system is built using the Django framework and Python.

## Getting Started


### Prerequisites

You need to have Python installed on your computer. You can download it from [here](https://www.python.org/downloads/).

### Installing

Clone the repository to your local machine

```
git clone
```

Install the requirements

```
pip install -r requirements.txt
```

Create dummy data

run the script inside the database folder

```
python create_dummy_data.py
```

## API Endpoints

---
### Customer Endpoints
POST http://127.0.0.1:5000/customer/8
```
    {
        "email": "twcypzny.nrssrxzvvinl@example.com",
        "first_name": "twcypzny",
        "last_name": "nrrxzvvinl",
        "phone_number": "1488349414"
    }

```

response
```
{
    "message": "Customer created successfully"
}
```

GET http://127.0.0.1:5000/customer/8

response
```
{
    "email": "twcypzny.nrrxzvvinl@example.com",
    "first_name": "twcypzny",
    "id": 8,
    "last_name": "nrrxzvvinl",
    "phone_number": "1488349414"
}
```

UPDATE http://127.0.0.1:5000/customer/8

```
{
    "email": "twcypzny.nrssrxzvvinl@example.com",
    "first_name": "twcypzny",
    "last_name": "nrrxzvvinl",
    "phone_number": "1488349414"
}
```

response
```
{
    "message": "Customer updated successfully"
}
```

DELETE http://127.0.0.1:5000/customer/8

response
```
{
    "message": "Customer deleted successfully"
}
```
### Booking Endpoints
POST http://127.0.0.1:5000/make_booking

```
{
    "customer_email": "aqosfqrq.vsjsxpiokd@example.com",
    "car_type":"van",
    "date_hire":"2023-04-05",
    "date_return":"2023-04-10"
}
```
response
```
{
    "message": "Booking successful"
}
```

### Report Endpoints

GET http://127.0.0.1:5000/report
response
```
{
    "11": {
        "cost": 1250.0,
        "customer": "aqosfqrq vsjsxpiokd",
        "hire_date": "Wed, 05 Apr 2023 00:00:00 GMT",
        "return_date": "Mon, 10 Apr 2023 00:00:00 GMT",
        "vehicle": "van"
    }
}
```
