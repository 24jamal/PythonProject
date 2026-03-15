import pymysql

def get_connection():

    return pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="orders_db",
        autocommit=True
    )