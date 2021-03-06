# MySQL
""" Remember, you get input from users or from databases. 
MySQL is a popular database and here is how to use Python in MySQL"""

""" for the best use of this tutorial, 
run each chapter separately from the others to avoid buffering and errors.
Preferable use jupyter notebooks for the best results because you will be contolling each cell you run."""

""" First, Install MySQL on your computer in order to be able to work with it.
https://www.mysql.com/downloads/ will give you ideas of how."""

""" Then install the mysql-connector-python, This is one of the mysql drivers 
that let python connect to the database """

# Test MySQL connector
import mysql.connector # if there is no error, then the connector is working.

# Create connection to the Database
import mysql.connector


mydb = mysql.connector.connect( # Create a new object mydb using the connector module
    host = "localhost", 
    user = "root", #Default username
    password = "**********" # your Mysql Password, !USE YOUR OWN!
)

print(mydb)

# Create a database
""" Once a database is created please comment the line of its creation, make sure that line is not executed ever """

mycursor = mydb.cursor() # Create a cursor object 'mycursor' for the connection. 
mycursor.execute("CREATE DATABASE mydatabase") # use the object to execute the 'CREATE DATABASE statement

#Check if a database exists
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

# Create a table
""" Once a table is created please comment the line of its creation, make sure that line is not executed ever """
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
for x in mycursor:
    print(x)

#Create primary key for our table
mycursor.execute("CREATE TABLE customers (id: INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255)))")

""" if the table already exist, use the ALTER TABLE keyword """

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# Insert a record in the table
import mysql.connector

mydb = mysql.connector.connect( # Create a new object mydb using the connector module
    host = "localhost", 
    user = "root", #Default username
    password = "*********", # your Mysql Password !USE YOUR OWN!
    database = "database1" # Yes, you can call the database here once it has been created.
)
mycursor = mydb.cursor(buffered = True) # buffered is set to true to avoid the unread results error.
#mycursor.execute("CREATE DATABASE database1") """ comment these lines after the creation"""
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", " 567 NY")
mycursor.execute(sql,val)
mydb.commit() # This statement is required to make the changes to the table, otherwise no changes are made.
print(mycursor.rowcount, "record inserted")


# Insert many rows
sql = "INSERT INTO customers  (name, address) VALUES (%s, %s)" 
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val) # Here it is no longer execute but executemany() method.
mydb.commit()
print (mycursor.rowcount, " records were inserted ")

#Get the Insert ID
""" ID of the last inserted row """
val = ("Michelle", "Blue Village")
mycursor.execute(sql,val)
mydb.commit()
print( " 1 record inserted, ID: ", mycursor.lastrowid)

# Select from database
mycursor.execute("SELECT *FROM customers") # the '*' means all
myresult = mycursor.fetchall() # Fetch all looks for all rows from the last executed statement
for x in myresult: # for a readable display, to get each record on its line
    print(x)

#Select columns only
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# fetchone()
""" display the first row of the result """
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)

# WHERE
""" to select with a filter """
sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

""" to select records containing a given word """
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#prevent SQL injection
""" escape values provided by the user , to prevent the hacking"""
sql = "SELECT * FROM customers WHERE address = %s" # the placeholder %s helps escape the user's input.
adr = ("Yellow garden 2", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult: # 
    print(x)

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "***********",
    database = "testdb"
) 
my_cursor = mydb.cursor()
#my_cursor.execute("CREATE DATABASE testdb")
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db[0])
#my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY )")
# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
#     print(table[0])
# newdata = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# record1 = ("John", "john@john.com", 40)
# my_cursor.execute(newdata, record1)
# mydb.commit()

# sql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# val = [
#   ('Peter', 'example@example.com', 56),
#   ('Amy', 'example@example.com', 74),
#   ('Hannah', 'example@example.com', 34),
#   ('Michael', 'example@example.com', 23),
#   ('Sandy', 'example@example.com', 64),
#   ('Betty', 'example@example.com', 43),
#   ('Richard', 'example@example.com', 54),
#   ('Susan', 'example@example.com', 23),
#   ('Vicky', 'example@example.com', 89),
#   ('Ben', 'example@example.com', 23),
#   ('William', 'example@example.com', 34),
#   ('Chuck', 'example@example.com', 34),
#   ('Viola', 'example@example.com', 35)
# ]
# my_cursor.executemany(sql, val)
# mydb.commit()



# my_cursor.execute("SELECT * FROM users ORDER BY name DESC") #ORDERING IN REVERSE ALPHABET (default is ASC for )
# for a in my_cursor:
#     print(a)
# delete_users = " DELETE FROM users WHERE name = %s " # DELETE records that have name of the placeholder
# name_to_delete = ("Ben",) # The name has to be Ben
# my_cursor.execute(delete_users, name_to_delete)
# mydb.commit()

#my_cursor.execute("CREATE TABLE table_to_delete (address VARCHAR(255), po VARCHAR(255), id INTEGER AUTO_INCREMENT PRIMARY KEY)")
# data = "INSERT INTO table_to_delete (address, po) VALUES = %s,%s"
# values = ("MTL St, 245", "735A")
# mydb.commit()
#my_cursor.execute("DROP TABLE table_to_delete") # THIS DELETES THE TABLE THAT WAS JUST CREATED
#my_cursor.execute("DROP TABLE IF EXISTS table_to_delete") # DELETES THE TABLE ONLY IF IT EXIST TO AVOID THE ERROR

# updating_records = "UPDATE users SET age = %s WHERE age = %s" # THIS UPDATES THE AGE RECORDS.
# updated_records = (70, 34 ) # UPDATES ALL RECORDS WITH AGE 34 TO AGE 70
# my_cursor.execute(updating_records, updated_records)
# mydb.commit()
# print(my_cursor.rowcount, "record(s) affected")
