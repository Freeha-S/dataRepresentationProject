DROP DATABASE IF EXISTS Phonedb;
CREATE DATABASE Phonedb;

USE Phonedb;

CREATE TABLE Customer(
	CustomerID INT NOT NULL AUTO_INCREMENT,
   	FirstName VARCHAR(250) DEFAULT NULL,
	LastName VARCHAR(250) DEFAULT NULL,
   	Address VARCHAR(250) DEFAULT NULL,
   	Email VARCHAR(250) DEFAULT NULL,
   	PhoneNumber INT DEFAULT NULL,
   	PRIMARY KEY (CustomerID)
  );

CREATE TABLE Orders(
	OrderId INT NOT NULL AUTO_INCREMENT,
	Product VARCHAR(250) DEFAULT NULL,
	OrderDate varchar(250) DEFAULT '2020-12-31',
	Category VARCHAR(250) DEFAULT NULL,
	Customer_id INT NOT NULL,
	PRIMARY KEY (OrderId),
	CONSTRAINT FK_customer_order
   	FOREIGN KEY (Customer_id)
   	REFERENCES Customer(CustomerID)
      	ON DELETE RESTRICT
   );    


CREATE TABLE Users(
	userID INT NOT NULL AUTO_INCREMENT,
   	name VARCHAR(250) DEFAULT NULL,
   	password varchar(250) DEFAULT NULL,
   	PRIMARY KEY (userID)
   	);

INSERT INTO customer (FirstName, LastName, Address, Email,PhoneNumber) VALUES ("Sam", "Smith", "Galway","sam@gmail.com","1234567");
INSERT INTO customer (FirstName, LastName, Address, Email,PhoneNumber) VALUES ("John", "Duffy", 'Galway','john@gmail.com','2234567');
INSERT INTO customer (FirstName, LastName, Address, Email,PhoneNumber) VALUES ("Sara", "Smith", 'Mayo','sara@gmail.com','1244567');
INSERT INTO orders (product, Orderdate, Category, customer_id) VALUES ("iphone7", "2021-01-01","Refurbished" , 1);
INSERT INTO orders (product, Orderdate, Category, customer_id) VALUES ("iphone11", "2021-01-02","New" , 2);
INSERT INTO orders (product, Orderdate, Category, customer_id) VALUES ("Sumsung 8", "2021-01-03","Used" , 3);
INSERT INTO orders (product, Orderdate, Category, customer_id) VALUES ("iphonePro", "2021-01-04","Refurbished" , 2);

INSERT INTO users (name, password) VALUES ("admin", "admin");
INSERT INTO users (name, password) VALUES ("freha", "1234");
