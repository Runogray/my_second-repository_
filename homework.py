import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='application_data',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def create_table():
    
    try:
        with connection.cursor() as cursor:
        # Create a new record repaymentDuedate, repaymentPaydate) VALUES('{customerID}', '{loanID}', '{application_data}', '{LoanNumber}', '{loanAmount}', '{interestRate}', '{TermDays}', '{repaymentDuedate}', '{repaymentPaydate});"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
         print("successfully Added User...!!")
         sql = "CREATE TABLE users (id INT(3) PRIMARY KEY NOT NULL AUTO_INCREMENT, customerID VARCHAR(12), loanID VARCHAR(15), applicationDate VARCHAR(11), LoanNumber INT(3), loanAmount int(6), interestRate DECIMAL(3,1), TermDays INT(3), repaymentDueDate VARCHAR(11), repaymentPayDate VARCHAR(11));"
            cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
            connection.commit()

    finally:
        connection.close()
        print ("successfully created Database...!!")


# def add_data(customerID, loanID, application_data, LoanNumber, loanAmount, interestRate, TermDays, repaymentPaydate):
#     try:
#         with connection.cursor() as cursor:
#             # Create a new record
#             sql =f"INSERT INTO application_data (customerID, loanID, applicationDate, LoanNumber, loanAmount, interestRate, TermDays,