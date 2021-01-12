from flask import Flask, jsonify, request, abort,render_template,session,redirect,url_for
from  ShopDAO import ShopDAO

#app = Flask(__name__, static_url_path='', static_folder='.')
app = Flask(__name__)
app.secret_key = 'abcd1234yturKLMH67nh'

#@app.route('/')
#def index():
#    return "Hello, World!"
@app.route('/')
def index():
    if not 'username' in session:
      return redirect(url_for('login'))

    return render_template('index.html',name = session['username'])
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userID = request.form['username']
        password = request.form['password']
        # Get user from database
        if userID or password:
            foundUser = ShopDAO.findUserByUserID(userID)
            #return jsonify(foundUser)
            if foundUser:
            #source: https://flask.palletsprojects.com/en/1.1.x/logging/
                    app.logger.info('User found')
                    # compare user password
                    if password == foundUser["password"]:
                        # username and associated password match found
                        app.logger.info('Password matched for user %s', userID)
                        session['username'] = userID
                        return redirect(url_for('index',name = session['username']))
                    else:
                        app.logger.info('Password does not match for user')
                        return render_template('login.html', error='Incorrect password: Please try again')
                        
                    # if not user found
            app.logger.info('User not found')
            return render_template('login.html', error="User not found")
        else:
        # for GET method
            app.logger.info('Redirect to login')
            return render_template('login.html', error='Please Login')
    else:
        return render_template('login.html')
# Get All customers
#curl "http://127.0.0.1:5000/customer"
@app.route('/customer')
def getAll():
    #print("in getall")
    results = ShopDAO.getAllCustomer()
    return jsonify(results)
    #return render_template('customer.html')
#find customer by Id
#curl "http://127.0.0.1:5000/customer/2"
@app.route('/customer/<int:id>')
def findById(id):
    foundCustomer = ShopDAO.findCustomerById(id)
    return jsonify(foundCustomer)
# Create customer
#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books
@app.route('/customer', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    # other checking 
    customer = {
        'FirstName':request.json['FirstName'],
        'LastName':request.json['LastName'],
        'Address':request.json['Address'],
        'Email':request.json['Email'],
        'PhoneNumber':request.json['PhoneNumber'],
        }
    values = (customer['FirstName'],customer['LastName'],customer['Address'],customer['Email'], customer['PhoneNumber'])
    newId = ShopDAO.createCustomer(values)
    customer['CustomerID']=newId
    return jsonify(customer)

#update customer
#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"FirstName\":\"wat\", \"LastName\":\"bds\",\"Address\":\"wat\",\"Email\":\"frr@gg.ie\",\"PhoneNumber\":\"67893\"}" http://127.0.0.1:5000/customer/1
# curl -X PUT -d "{\"FirstName\":\"wat\", \"LastName\":\"bds\",\"Address\":\"wat\",\"Email\":\"frr@gg.ie\",\"PhoneNumber\":\"67893\",}" -H "content-type:application/json" http://127.0.0.1:5000/customer/2
@app.route('/customer/<int:CustomerID>', methods=['PUT'])
def update(CustomerID):
    foundCustomer = ShopDAO.findCustomerById(CustomerID)
    if not foundCustomer:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    #if 'CustomerID' in reqJson and type(reqJson['CustomerID']) is not int:
     #   abort(400)
    if 'FirstName' in reqJson:
        foundCustomer['FirstName'] = reqJson['FirstName']
    if 'LastName' in reqJson:
        foundCustomer['LastName'] = reqJson['LastName']
    if 'Address' in reqJson:
        foundCustomer['Address'] = reqJson['Address']
    if 'Email' in reqJson:
        foundCustomer['Email'] = reqJson['Email']
    if 'PhoneNumber' in reqJson:
        foundCustomer['PhoneNumber'] = reqJson['PhoneNumber']
     
    ShopDAO.updateCustomer(foundCustomer)
    return jsonify(foundCustomer)
# delete customer
@app.route('/customer/<int:id>' , methods=['DELETE'])
def delete(id):
    ShopDAO.deleteCustomer(id)
    return jsonify({"done":True})
# get all Orders
#curl "http://127.0.0.1:5000/orders"
@app.route('/orders')
def getAllOrders():
    #print("in getall")
    results = ShopDAO.getAllOrders()
    return jsonify(results)
# find Order by Id
#curl "http://127.0.0.1:5000/orders/2"
@app.route('/orders/<int:id>')
def findOrderById(id):
    foundOrder = ShopDAO.findOrderById(id)
    return jsonify(foundOrder)
#create Order
#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books
@app.route('/orders', methods=['POST'])
def createOrder():
    if not request.json:
        abort(400)
    # other checking 
    order = {
        'Product':request.json['Product'],
        'OrderDate':request.json['OrderDate'],
        'Category':request.json['Category'],
        'Customer_Id':request.json['Customer_Id'],
         }
    values = (order['Product'],order['OrderDate'],order['Category'], order['Customer_Id'])
    newId = ShopDAO.createOrder(values)
    order['OrderId']=newId
    return jsonify(order)
# update Order
#curl -X PUT -d "{ \"Product\":\"sumsung\",\"Catgory\":\"Used\",\"OrderDate\":\"2020-01-04\",\"customer_id\":3}" -H "content-type:application/json" http://127.0.0.1:5000/orders/2
@app.route('/orders/<int:OrderId>', methods=['PUT'])
def updateOrder(OrderId):
    foundOrder = ShopDAO.findOrderById(OrderId)
    if not foundOrder:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    #if 'CustomerID' in reqJson and type(reqJson['CustomerID']) is not int:
     #   abort(400)
    if 'Product' in reqJson:
        foundOrder['Product'] = reqJson['Product']
    if 'OrderDate' in reqJson:
        foundOrder['OrderDate'] = reqJson['OrderDate']
    if 'Category' in reqJson:
        foundOrder['Category'] = reqJson['Category']
    if 'Customer_Id' in reqJson:
        foundOrder['Customer_Id'] = reqJson['Customer_Id']
    
     
    ShopDAO.updateOrder(foundOrder)
    return jsonify(foundOrder)

# delete order
@app.route('/orders/<int:id>' , methods=['DELETE'])
def deleteOrder(id):
    ShopDAO.deleteOrder(id)
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug=True)