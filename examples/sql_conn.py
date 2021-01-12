# Follow this tutorial to establish connection
# https://www.devart.com/odbc/sqlazure/docs/python.htm

import pyodbc

data_source_name = 'NUST Chatbot Azure'
server = 'TCP:nustdb.database.windows.net'
port = '1433'
database = 'nustdb'
user_id = 'nustdb'
password = 'Password1'
credentials = f'DRIVER={{Devart ODBC Driver for SQL Azure}};Server={server};Port={port};Database={database};User ID={user_id};Password={password}'
cnxn = pyodbc.connect(credentials)
cursor = cnxn.cursor()

cursor.execute("SELECT * FROM COURSE")
row = cursor.fetchone()
while row:
   	print (row)
   	row = cursor.fetchone()
