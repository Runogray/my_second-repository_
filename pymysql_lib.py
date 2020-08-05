import pymysql.cursors

#connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='kbanks',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

#def create_Table():

##try:
##    with connection.cursor() as cursor:
##        # Create a new record
##        sql = "create table users (id INT(3) PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(50), password VARCHAR(30), account_num VARCHAR(12), age VARCHAR(3));"
##        cursor.execute(sql)
##
##    # connection is not autocommit by default. So you must commit to save
##    # your changes.
##    connection.commit()
##
##
##finally:
##    print("successfully Added User...!!")
##    connection.close()
##    

#return True

def add_user(name, age, password, account_num): 
    try:
        with connection.cursor() as cursor:
            #Create a new record
            sql = f"INSERT INTO users(name, age, password, account_num, balance) VALUES('{name}', '{age}', '{password}', '{account_num}', 0);" 
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
        print("successfully Added User...!!")
        connection.close()


def fetch_user_details(name):

    try:
        with connection.cursor() as cursor:
            # create a new record
            sql = f"SELECT name, password, balance from users WHERE name = '{name}';"
            cursor.execute(sql)
        # connection is not autocommit by default. So you must commit to save
        # your changes.
       
        data = cursor.fetchall()
        return (data)

     
    finally:
        print("successfully ...!!")
        connection.close()

    
    
def get_balance(name):
    
    try:
        with connection.cursor() as cursor:
            #create a new record
            sql = f"SELECT balance FROM users WHERE name = '{name}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.

        data = cursor.fetchall()
        return(data)

    finally:
        print("successfully fetched User...!!")
       


def alter_balance(name, balance):

    try:
         with connection.cursor() as cursor:
            #create a new record
            sql = f"UPDATE users SET balance = {balance} WHERE name = '{name}'"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        # connection.commit()
        
    finally:
        print("successfully updated user Balance User...!!")
        

            

    




