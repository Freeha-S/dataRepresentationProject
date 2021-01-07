# dataRepresentationProject
## Lecturer: Andrew Beatty
## Student: Freha Saleem
The purpose of this repository is to implement a Web Appliation as follows:
A basic Flask server that has a REST API, (to perform CRUD operations) two database table and Accompanying web interface, using AJAX calls, to perform these CRUD operations With authorization (logging in). hosted online (pythonanywhere)

## Repository
gitignore
README.md
LICENSE
ShopDAO.py
dbconfiguration.py
initdb.sql
requirements.txt
server.py
templates
  - index.html
  - login.html
Shop database base has three tables
- customer
- orders
- users
user table is used for authentication
usedID: admin 
password: admin
used to login the app
where
- View customers,Orders list from the database
- Create a new customer , new order(add to the database)
- Update existing customer /order
- delete existing customer/order
in order table customer ID is used as key that connect both tables

Running this web application on your local machine:
Prequisites
anaconda installation Anaconda.
MySQL.

## Cloning the repository
**create and use a copy of this repositiory on your local machine.**

In this repository.
Click on the green button "Code". Select "Clone with HTTPS". Copy the URL.
navigate to your preferred directory (folder) where you like to keep the copy .
Type git clone ( this is the URL you have copied).
The repository is now installed.
To install the necessary packages in the same folder/directory excecute the following: pip install -r requirements.txt
Verify that the packages have been installed using command: pip freeze.
To create database Use the initdb.sql to create the tables & insert data for testing in a database called phonedb.
In dbconfiguration.py Enter your own database username & password here.
## Running the app
navigate to the the folder where you cloned this repository.
In terminal execute this command: python server.py
In your browser navigate to http://127.0.0.1:5000/
You are now ready to use this web application.
## Pythonanywhere link:
Link for app: http://freeha123.pythonanywhere.com/
