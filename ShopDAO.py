#Shop Database Access Object (DAO) for user login and database CRUD operations
# Provides an interface between the flask server and the sql database

# import module and database access configuration file
import mysql.connector
import dbconfiguration as cfg

# Class object for Database Access Object (DAO)
class ShopDAO:
   db=""
   # Create database connection pool
   def initConnectToDB(self):
      self.db = mysql.connector.connect(
      host=cfg.mysql['host'],
      user=cfg.mysql['username'],
      password=cfg.mysql['password'],
      database=cfg.mysql['database'],
    )
   # Initialise DB connection pool
   def __init__(self):
      self.initConnectToDB()


   # Check for cnxn, if none make one.
   def getConnection(self):
      if not self.db.is_connected():
         self.initConnectToDB()
      return self.db.cursor()



   # Create customer, returns customerID of new customer
   def createCustomer(self, customer):
      cursor = self.getConnection()
      #cursor = db.cursor()
      sql = "insert into Customer(FirstName, LastName, Address,Email,PhoneNumber) values (%s,%s,%s,%s,%s)"
      values = [customer[0],customer[1],customer[2],customer[3],customer[4]]
      cursor.execute(sql, values)
      self.db.commit()
      lastRowId = cursor.lastrowid
      cursor.close()
      return lastRowId
      # return customerID

   # Create Orders, returns OrderId of new Order
   def createOrder(self, order):

      cursor = self.getConnection()
      sql = "insert into Orders (Product, OrderDate, Category, Customer_Id) values (%s,%s,%s,%s)"
      values = [

         order[0],
         order[1],
         order[2],
         order[3]
      ]
      cursor.execute(sql, values)
      self.db.commit()
      lastRowId = cursor.lastrowid
      cursor.close()
      return lastRowId
      # return order['orderId']

   # Create user, returns userID of new user
   def createUser(self, user):

      cursor = self.getConnection()
      sql = "insert into Users (Name, Password) values (%s,%s)"
      values = [
         # user['userID'], - auto-increment
         user['name'],
         user['password'],
      ]
      cursor.execute(sql, values)
      self.db.commit()
      lastRowId = cursor.lastrowid
      cursor.close()
      return lastRowId
      # return user['userID']

   # Return all customers from database
   def getAllCustomer(self):
      #db = self.getConnection()
      cursor = self.getConnection()
      sql = 'select * from Customer'
      cursor.execute(sql)
      results = cursor.fetchall()
      returnArray = []
      # print(results)
      for result in results:
         resultAsDict = self.convertCustomerToDict(result)
         returnArray.append(resultAsDict)
      cursor.close()
      return returnArray

   # Return all orders from database
   def getAllOrders(self):
      #db = self.getConnection()
      cursor = self.getConnection()
      sql = 'select * from Orders'
      cursor.execute(sql)
      results = cursor.fetchall()
      returnArray = []
      # print(results)
      for result in results:
         resultAsDict = self.convertOrderToDict(result)
         returnArray.append(resultAsDict)
      cursor.close()
      return returnArray

   # Return info on all users
   def getAllUser(self):
      #db = self.getConnection()
      cursor = self.getConnection()
      sql = 'select * from Users'
      cursor.execute(sql)
      results = cursor.fetchall()
      returnArray = []
      # print(results)
      for result in results:
         resultAsDict = self.convertUserToDict(result)
         # print(result)
         returnArray.append(resultAsDict)
      cursor.close()
      return returnArray

   # Return info on Customer for given customerID
   def findCustomerById(self, customerID):
      #db = self.getConnection()
      cursor = self.getConnection()
      sql = 'select * from Customer where CustomerID = %s'
      values = [customerID]
      cursor.execute(sql, values)
      result = cursor.fetchone()
      customer = self.convertCustomerToDict(result)
      cursor.close()
      return customer

   # Return orders for given orderID
   def findOrderById(self, orderId):
      #db = self.getConnection()
      cursor = self.getConnection()
      sql = 'select * from Orders where OrderId = %s'
      values = [orderId]
      cursor.execute(sql, values)
      result = cursor.fetchone()
      order= self.convertOrderToDict(result)
      cursor.close()
      return order

   # Return user for given userID
   def findUserByID(self, userId):
      #db = self.getConnection()
      cursor = self.getConnection()
      sql = 'select * from Users where userID = %s'
      values = [userId]
      cursor.execute(sql, values)
      result = cursor.fetchone()
      user = self.convertUserToDict(result)
      cursor.close()
      return user
   #Return user for given user name
   def findUserByUserID(self, name):
      #db = self.getConnection()
      cursor = self.getConnection()
      sql = 'select * from Users where name = %s'
      values = [name]
      cursor.execute(sql, values)
      result = cursor.fetchone()
      user = self.convertUserToDict(result)
      cursor.close()
      return user


   # Return info on all Orders associated with a given customer
   def getAllOrderByCustomer(self, customerid):
      #db = self.getConnection()
      cursor = self.getConnection()
      sql = 'select * from Orders where Customer_Id = %s;'
      values = [customerid]
      cursor.execute(sql, values)
      results = cursor.fetchall()
      returnArray = []
      # print(results)
      for result in results:
         resultAsDict = self.convertOrderToDict(result)
         returnArray.append(resultAsDict)
      cursor.close()
      return returnArray

   # Update customer for given customerID and returns updated info
   def updateCustomer(self, customer):
      #db = self.getConnection()
      cursor = self.getConnection()
      #cursor=conn.cursor()
      sql = "update customer set FirstName= %s, LastName =%s ,Address= %s,Email= %s,PhoneNumber= %s where CustomerID = %s"

      values = [customer['FirstName'],customer['LastName'],customer['Address'],customer['Email'],customer['PhoneNumber'],customer['CustomerID']]
      cursor.execute(sql, values)
      db.commit()
      cursor.close()
      return customer

   # Update order info for given orderid
   def updateOrder(self, order):
      #db = self.getConnection()
      cursor = self.getConnection()
      sql = "update Orders set Product = %s, OrderDate = %s, Category = %s, Customer_Id = %s where OrderId = %s"
      values = [
         order['Product'],
         order['OrderDate'],
         order['Category'],
         order['Customer_Id'],
         order['OrderId']
      ]
      cursor.execute(sql, values)
      self.db.commit()
      cursor.close()
      return order

   # Update user info
   def updateUser(self, user):
      #db = self.getConnection()
      cursor = self.getConnection()
      sql = "update users set name = %s, password = %s where userID = %s"
      values = [
         user['name'],
         user['password'],
         user['userID']
      ]
      cursor.execute(sql, values)
      self.db.commit()
      cursor.close()
      return user

   # Delete customer for given customerId
   def deleteCustomer(self, customerId):
      #db = self.getConnection()
      cursor = self.getConnection()
      sql = 'delete from Customer where CustomerId = %s'
      values = [customerId]
      cursor.execute(sql, values)
      self.db.commit()
      cursor.close()
      return {}

   # Delete Order for a given orderId
   def deleteOrder(self, orderId):
      #db = self.getConnection()
      cursor = self.getConnection()
      sql = 'delete from Orders where OrderId = %s'
      values = [orderId]
      cursor.execute(sql, values)
      self.db.commit()
      cursor.close()
      return {}


   # convert Customer into Dictionary
   def convertCustomerToDict(self, result):
      colnames = ['CustomerID', 'FirstName', 'LastName', 'Address', 'Email', 'PhoneNumber']
      customer = {}
      if result:
         for i, colName in enumerate(colnames):
            value = result[i]
            customer[colName] = value
      return customer

   # convert Orders into Dictionary
   def convertOrderToDict(self, result):
      colnames=['OrderId','Product', 'OrderDate','Category','Customer_Id']
      order = {}
      if result:
         for i, colName in enumerate(colnames):
            value = result[i]
            order[colName] = value

      return order

   # convert user into Dictionary
   def convertUserToDict(self, result):
      colnames = ['userID', 'name', 'password']
      user = {}
      if result:
         for i, colName in enumerate(colnames):
            value = result[i]
            user[colName] = value
      return user

# Create instance of the DAO class
ShopDAO = ShopDAO()