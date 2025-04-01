from backend.sql_connection import get_sql_connection
from datetime import datetime

def insert_order(connection, order):
    cursor = connection.cursor()

    order_query =(" INSERT INTO `order`"
                  "(customer_name,total,datetime)"
                  "VALUES (%s,%s,%s)")
    order_data =(order['customer_name'],order['grand_total'],datetime.now())
    cursor.execute(order_query,order_data)
    idorder=cursor.lastrowid

    order_details_query =("INSERT INTO order_details "
                          "(idorder,product_id,quantity,total_price)"
                          "VALUES (%s,%s,%s,%s)")

    #insert order_details
    order_details_data=[]
    for order_detail_record in order['order_details']:
        order_details_data.append([
            idorder,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])

    cursor.executemany(order_details_query,order_details_data)

    connection.commit()
    return idorder

def get_all_orders(connection):
    cursor=connection.cursor()
    query=("SELECT * FROM grocery_store.order")
    cursor.execute(query)

    response=[]
    for(idorder,customer_name,total,dt) in cursor:
        response.append({
            'order_id':idorder,
            'customer_name':customer_name,
            'total':total,
            'datetime':dt
        })
    return response


if __name__=='__main__':
    connection =get_sql_connection()
    print(get_all_orders(connection))
    # print(insert_order(connection,{
    #     'customer_name': 'Yogita',
    #     'grand_total': '500',
    #     # 'datetime': datetime.now(),
    #     'order_details':[
    #         {
    #             'product_id':6,
    #             'quantity': 2,
    #             'total_price':50
    #         }
    #         # {
    #         #     'product_id':7,
    #         #     'quantity':1,
    #         #     'total_price':30
    #         # }
    #     ]
    # }))