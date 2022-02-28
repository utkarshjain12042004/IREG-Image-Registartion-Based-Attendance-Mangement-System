import mysql.connector

conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
my_cursor = conn.cursor()
# - Getting all the student IDs from the IREG Database and storing them in the form of an array named student_IDs. 
my_cursor.execute("SELECT Student_ID FROM mydb.tbl_student")
student_IDs = my_cursor.fetchall()
print(student_IDs)
var_student_ID = 0
# This checks if the number of student profiles stored in the tbl_student table of the database is 0 or not. If it is 0, the 
# system automatically assigns the student ID as 0.
if len(student_IDs)==0:
    var_student_ID = str(1)
else:
    last_student_ID = student_IDs[len(student_IDs)-1][0]
    var_student_ID = last_student_ID + 1
print(var_student_ID)
conn.close()