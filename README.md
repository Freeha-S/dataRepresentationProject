# dataRepresentationProject
## Lecturer: Andrew Beatty
## Student: Freha Saleem
The purpose of this repository is to implement a Web Appliation as follows:
- A basic Flask server that has a REST API, (to perform CRUD operations) on two database table and accompanying web interface. Using AJAX calls, to perform these CRUD operations with authorization (logging in). hosted online at (pythonanywhere)
## Pythonanywhere link:
Link for app: http://freeha123.pythonanywhere.com/

## Repository
- gitignore
- README.md
- LICENSE
- ShopDAO.py
- dbconfiguration.py
- initdb.sql
- requirements.txt
- server.py
- templates
  - index.html
  - login.html

### Database has three tables

- Customer
~~~~sql
CREATE TABLE Customer(
	CustomerID INT NOT NULL AUTO_INCREMENT,
   	FirstName VARCHAR(250) DEFAULT NULL,
	LastName VARCHAR(250) DEFAULT NULL,
   	Address VARCHAR(250) DEFAULT NULL,
   	Email VARCHAR(250) DEFAULT NULL,
   	PhoneNumber INT DEFAULT NULL,
   	PRIMARY KEY (CustomerID)
  );
~~~~
- Orders
~~~~sql
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
~~~~  
- Users
~~~~sql
CREATE TABLE Users(
	userID INT NOT NULL AUTO_INCREMENT,
   	name VARCHAR(250) DEFAULT NULL,
   	password varchar(250) DEFAULT NULL,
   	PRIMARY KEY (userID)
   	);
~~~~
Users table is used for authentication<br/>
In Orders table CustomerID is used as key that connect both tables
## App Detail
On the Main screen
**usedID: admin**
**password: admin**
*used to login the app*
<br/>
after logging in you can
- View (Customers/Orders)list from the database
- Create a new (Customer/Order) -- add to the database
	- New order can be created only for existing customer
- Update existing (Customer /Order)
- Delete existing (Customer/Order)
	- The customer with existing order cannot be deleted
<br/>


### To Run this web application on your local machine:
#### Prequisites
- anaconda installation Anaconda.
- MySQL.

## Cloning the repository
**create and use a copy of this repositiory on your local machine.**

- In this repository.
Click on the green button "Code". Select "Clone with HTTPS". Copy the URL.
- Navigate to your preferred directory (folder) where you like to keep the copy .
- Type git clone  https://github.com/Freeha-S/dataRepresentationProject.git ( this is the URL you have copied).
The repository is now installed.
-To install the necessary packages in the same folder/directory excecute the following: pip install -r requirements.txt
- To check the packages have been installed using command: pip freeze.
- To create database Use the initdb.sql to create the tables & insert data for testing in a database called phonedb.
- In dbconfiguration.py Enter your own database username & password here.
## Running the app
- Navigate to the the folder where you cloned this repository.
- In terminal execute this command: python server.py
- In your browser navigate to http://127.0.0.1:5000/
- You are now ready to use this web application
	- use  userID: admin, password: admin to login
## Pythonanywhere link:
Link for app: http://freeha123.pythonanywhere.com/
