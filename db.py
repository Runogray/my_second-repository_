import pymysql.cursors

connection = pymysql.connect(host='localhost', user='root', password='', database='application', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

def create_table