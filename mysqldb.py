import csv
import pymysql.cursors

Connection = pymysql.connect(host='localhost', user='root', password='', database='application', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
print('database.connected')

cursor = Connection.cursor

csv_data = csv.reader(open("")
