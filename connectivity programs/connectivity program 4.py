import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="Student_details"
)

mycursor = mydb.cursor()


mycursor.execute("SELECT SUM(marks) FROM student WHERE marks > 430")


for i in mycursor:
    print(i)

mydb.close( )
