CREATE DATABASE car_hire_system;

USE car_hire_system;

CREATE TABLE customers (
  customer_id INT PRIMARY KEY auto_increment,
  first_name VARCHAR(50) NOT NULL ,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE vehicle_types (
  type_id INT PRIMARY KEY auto_increment,
  type_name VARCHAR(20) NOT NULL,
  capacity INT 

);

CREATE TABLE vehicles (
  vehicle_id INT PRIMARY KEY auto_increment,
  type_id INT NOT NULL,
  available BOOLEAN,
  FOREIGN KEY (type_id) REFERENCES vehicle_types(type_id)
);


CREATE TABLE bookings (
  booking_id INT PRIMARY KEY auto_increment,
  customer_id INT,
  vehicle_id INT,
  hire_date DATE,
  return_date DATE,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);
