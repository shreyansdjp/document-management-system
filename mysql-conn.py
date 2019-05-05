import pymysql

def get_connection():
    host = 'localhost'
    user = 'root'
    password = ''
    db_name = 'dms'
    return pymysql.connect(host, user, password, db_name, cursorclass=pymysql.cursors.DictCursor)