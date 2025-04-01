from http.client import responses
from itertools import product

from flask import Flask , request,jsonify

from backend.sql_connection import get_sql_connection
from backend import  product_dao

app=Flask(__name__)

# import product_dao
import uom_dao
import json
import orders_dao
connection= get_sql_connection()

@app.route('/getProducts')
def get_products():
    products = product_dao.get_all_products(connection)
    response =jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getUOM',methods=['GET'])
def get_uom():
    response =uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getAllOrders',methods=['GET'])
def get_all_orders():
    response= orders_dao.get_all_orders(connection)
    response =jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/insertProduct',methods=['POST'])
def insert_product():
    request_payload=json.loads(request.form['data'])
    product_id =product_dao.insert_new_product(connection,request_payload)
    response = jsonify({
        'product_id': product_id
    })

@app.route('/deleteProduct',methods=['POST'])
def delete_product():
    return_id = product_dao.delete_product(connection, request.form['product_id'])
    response =jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

# def insert_order()
if __name__ == "__main__":
    print("Starting Python FLask Server For Grocery Store Management System")
    app.run(port=5000)