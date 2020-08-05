import pymysql.cursors

connection = pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            db="kbank",
                            charset="utf8mb4",
                            cursorclass=pymysql.cursors.DictCursor)
def create_table():
    try:
        with connection.cursor() as cursor:
            sql = "CREATE TABLE users (id INT(3) PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(50), transfer_from VARCHAR(30), transfer_to VARCHAR(30), amount INT(3), date INT(30));"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        print("Successfully created Database")
        # connection.close()
    return True

def ad_users():
    try:
        with connection.cursor() as cursor:
            sql = f"INSERT INTO users (name, ) VALUES('{name}','{transfer_from}','{transfer_to}','{amount}','{date}','{comment}0);"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        print("Successfully Added user")
        # connection.close()

def get_balance(name):
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT balance FROM users WHERE name = '{name}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        data = cursor.fetchall()
        return data
    finally:
        print("Successfully fetched")
        # connection.close()

def alter_balance(name, balance):
    try:
        with connection.cursor() as cursor:
            sql = f"UPDATE users SET balance ={balance} WHERE name = '{name}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        print("Successfully fetched")
        # connection.close()

def fetch_user_detail(name):
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT name,password,balance FROM users WHERE name = '{name}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        data = cursor.fetchall()
        return data
    finally:
        print("Successfully fetched")
        # connection.close()
def show_user_detail(name):
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT name,account_no,balance FROM users WHERE name = '{name}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        data = cursor.fetchall()
        return data
    finally:
        print("Successfully fetched")
        # connection.close()

def fetch_detail():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users;"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        data = cursor.fetchall()
        return data
    finally:
        print("Successfully fetched")
        # connection.close()

def log(name,destination,amount,type):
    try:
        with connection.cursor() as cursor:
            sql = f"INSERT INTO transactions (name,destination,amount,type) VALUES('{name}','{destination}',{amount},'{type}');"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        print("Successfully logged transaction ")
        # connection.close()

def show_user_statement(name):
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT name,type,destination,amount FROM transactions WHERE name = '{name}';"
            # sql2 = f"SELECT balance,amount FROM users WHERE name = '{name}';"
            cursor.execute(sql)
            # cursor.execute(sql2)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        data = cursor.fetchall()
        return data
    finally:
        print("Successfully fetched")
        # connection.close()