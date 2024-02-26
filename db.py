# Dependancies Install MySQL on your machine

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Kart1512!@'
) 


#cursor object
cursorObject = dataBase.cursor()

# create a database
dbname = "CRM_DB"
cursorObject.execute("CREATE DATABASE {}".format(dbname))

print("Database : {} is created successfully !".format(dbname))


