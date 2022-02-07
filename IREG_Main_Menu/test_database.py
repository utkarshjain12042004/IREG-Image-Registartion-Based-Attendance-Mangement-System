import sqlite3

conn = sqlite3.connect("IREG_attendance_management_system_db")
cursor = conn.cursor()

# Query for creating creating a database table for storing details of the student
tbl_student_query = """CREATE TABLE IF NOT EXISTS tbl_student
(Student_ID INTEGER PRIMARY KEY NOT NULL UNIQUE,
First_Name TEXT NOT NULL,
Last_Name TEXT NOT NULL,
Email TEXT NOT NULL,
Date_Of_Birth TEXT NOT NULL,
Date_Of_Admission TEXT NOT NULL,
Father_Name TEXT NOT NULL,
Father_Email TEXT NOT NULL,
Mother_Name TEXT NOT NULL,
Mother_Email TEXT NOT NULL)"""

# Query for creating a database table for storing details of the subjects
tbl_subjects = """CREATE TABLE IF NOT EXISTS tbl_subjects
(Subject_ID INTEGER PRIMARY KEY NOT NULL UNIQUE,
Subject_Name TEXT NOT NULL,
Room_Name TEXT NOT NULL)"""

# Query for creating creating a database table for storing details of the teacher
tbl_teacher_query = """CREATE TABLE IF NOT EXISTS tbl_teacher
(Teacher_ID INTEGER PRIMARY KEY NOT NULL UNIQUE,
First_Name TEXT NOT NULL,
Last_Name TEXT NOT NULL,
Email TEXT NOT NULL,
Date_Of_Birth TEXT NOT NULL,
Subject_Taught INTEGER NOT NULL,
FOREIGN KEY (Subject_ID) REFERENCES tbl_subject (Subject_ID))"""

# Query for creating a database table for storing details of the classes
tbl_class = """CREATE TABLE IF NOT EXISTS tbl_class
(Class_ID INTEGER PRIMARY KEY NOT NULL UNIQUE,
Student_ID INTEGER NOT NULL,
FOREIGN KEY (Student_ID) REFERENCES tbl_student (Student_ID))"""

# Query for creating a database table for storing details of the student attendance
tbl_student_attendance = """CREATE TABLE IF NOT EXISTS tbl_student_attendance
(Period_Number INTEGER PRIMARY KEY NOT NULL UNIQUE,
Student_ID INTEGER NOT NULL,
Class_ID INTEGER KEY NOT NULL,
Attendance TEXT NOT NULL,
FOREIGN KEY (Student_ID) REFERENCES tbl_student (Student_ID),
FOREIGN KEY (Class_ID) REFERENCES tbl_class (Class_ID))"""

# Query for creating a database table for storing the timetable
tbl_student_attendance = """CREATE TABLE IF NOT EXISTS tbl_student_attendance
(Timetable_ID INTEGER PRIMARY KEY NOT NULL UNIQUE,
Period_1 INTEGER NOT NULL,
Period_2 INTEGER KEY NOT NULL,
Period_3 INTEGER KEY NOT NULL,
Period_4 INTEGER KEY NOT NULL,
Period_5 INTEGER KEY NOT NULL,
Day_Name TEXT NOT NULL,
FOREIGN KEY(Period_1) REFERENCES tbl_subjects (subject_ID),
FOREIGN KEY(Period_2) REFERENCES tbl_subjects (subject_ID),
FOREIGN KEY(Period_3) REFERENCES tbl_subjects (subject_ID),
FOREIGN KEY(Period_4) REFERENCES tbl_subjects (subject_ID),
FOREIGN KEY(Period_5) REFERENCES tbl_subjects (subject_ID))"""

# Executing the create table queries
cursor.execute(tbl_student_query)
cursor.execute(tbl_teacher_query)
cursor.execute(tbl_subjects)
cursor.execute(tbl_class)
cursor.execute(tbl_student_attendance)
cursor.execute(tbl_student_attendance)


# Query to insert data in the above created tables
# Student table
student_insert1 = """INSERT INTO tbl_student 
VALUES(1, "Utkarsh", "Jain", "utkarshjain12042004@gmail.com", "2004/07/12", "2010/06/07", 
"Mukesh Jain", "muksjain@gmail.com", 
"Jayshree Jain", "muksjaya@gmail.com")"""

student_insert2 = """INSERT INTO tbl_student 
VALUES(2, "Tanisha", "Jain", "utkarshjain12042004@gmail.com", "2009/11/15", "2014/06/07", 
"Mukesh Jain", "muksjain@gmail.com", 
"Jayshree Jain", "muksjaya@gmail.com")"""
# Subject table
subject_insert1 = """INSERT INTO tbl_subjects
(1, "Maths", "MA4")"""

subject_insert2 = """INSERT INTO tbl_subjects
(1, "Physics", "PH1")"""
# Teacher table
teacher_insert1 = """INSERT INTO tbl_teacher
(1, "Jayshree", "Jain", "muskjaya@gmail.com", "1980/11/14", 1)"""

teacher_insert2 = """INSERT INTO tbl_teacher
(2, "Mukesh", "Jain", "muskjain@gmail.com", "1977/11/07", 2)"""
# Class table
class_insert1 = """INSERT INTO tbl_class
("1", "1")"""

class_insert2 = """INSERT INTO tbl_class
("2", "2")"""
# Executing the queries
cursor.execute(student_insert1)
cursor.execute(student_insert2)
#cursor.execute(subject_insert1)
#cursor.execute(subject_insert2)
cursor.execute(teacher_insert1)
cursor.execute(teacher_insert2)
#cursor.execute(class_insert1)
#cursor.execute(class_insert2)

print(cursor.execute("SELECT * FROM tbl_student").fetchall())
#print(cursor.execute("SELECT * FROM tbl_subject").fetchall())
print(cursor.execute("SELECT * FROM tbl_teacher").fetchall())
#print(cursor.execute("SELECT * FROM tbl_class").fetchall())

conn.commit()
