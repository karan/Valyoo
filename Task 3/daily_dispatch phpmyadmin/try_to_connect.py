#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="192.168.1.22", # your host, usually localhost
                     port=5123, # port of the connection
                     user="amit", # your username
                      passwd="amit", # your password
                      db="inventory") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the query you need
curr = db.cursor() 

# Use all the SQL you like
curr.execute("""SELECT * FROM orders WHERE created_at LIKE '2013-07-30%'""")

# print one result
result = curr.fetchone()
print result, type(result)

print '======================================='

results = curr.fetchall()
print type(results)
for row in results:
    print type(row), row
    print type(row[10]), row[10]
