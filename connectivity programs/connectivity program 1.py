import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="Student_details"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Student")

for i in mycursor:
    print(i)
