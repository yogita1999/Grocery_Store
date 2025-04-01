from http.client import responses

import pymysql

from backend.sql_connection import get_sql_connection


def get_all_products(connection):
    cursor = connection.cursor()

    query=("SELECT products.product_id,products.Name,products.uom_id,products.price_per_unit, uom.uom_name FROM products inner join uom on uom.uom_id=products.uom_id ")

    cursor.execute(query)
    response=[]
    for (product_id,Name,uom_id,price_per_unit,uom_name) in cursor:
        response.append({
            'product_id':product_id,
            'name':Name,
            'uom_id':uom_id,
            'price_per_unit': price_per_unit,
            'uom_name':uom_name
        })
        # pass

    # cnx.close()
    return response


def insert_new_product(connection, product):
    cursor=connection.cursor()
    query=("insert into products (name,uom_id,price_per_unit) VALUES (%s, %s, %s)")
    data=(product['product_name'],product['uom_id'],product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor=connection.cursor()
    query=("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid


if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection,5))

    # print(insert_new_product(connection,{
    #     'product_name':'brocoli',
    #     'uom_id':'2',
    #     'price_per_unit': '20'
    #     }))

