import sqlite3

class Database:
   '''Initiates the database.'''
   def __init__(self):
      self.db = sqlite3.connect('IREG_Database.db')
      self.createTable()
   def createTable(self):
      # CREATING TABLE FOR TABLE CLASSROOM tbl_classroom
      a = self.db.execute("""
                            CREATE TABLE IF NOT EXISTS tbl_student(
                            student_ID INT(3) UNSIGNED ZEROFILL NOT NULL,
                            first_Name VARCHAR(100) NOT NULL,
                            last_Name VARCHAR(100) NOT NULL,
                            date_Of_Birth DATE NOT NULL,
                            year_Of_Admission DATE NOT NULL,
                            email VARCHAR(500) NOT NULL,
                            father_First_Name VARCHAR(100) NOT NULL,
                            father_Last_Name VARCHAR(100) NOT NULL,
                            father_Email VARCHAR(500) NOT NULL,
                            mother_First_Name VARCHAR(100) NOT NULL,
                            mother_Last_Name VARCHAR(100) NOT NULL,
                            mother_Email VARCHAR(500) NOT NULL,
                            PRIMARY KEY (student_ID),
                            UNIQUE INDEX student_ID_UNIQUE (student_ID ASC) VISIBLE,
                            UNIQUE INDEX email_UNIQUE (email ASC) VISIBLE)""")
      self.db.commit()

      # CREATING TABLE FOR TABLE CLASSROOM tbl_classroom
      b = self.db.execute("""
                            CREATE TABLE IF NOT EXISTS tbl_teacher(
                            teacher_ID INT(3) UNSIGNED ZEROFILL NOT NULL,
                            subject_Taught VARCHAR(50) NOT NULL,
                            email VARCHAR(500) NOT NULL,
                            first_Name VARCHAR(100) NOT NULL,
                            last_Name VARCHAR(100) NOT NULL,
                            date_Of_Birth DATE NOT NULL,
                            PRIMARY KEY (teacher_ID),
                            UNIQUE INDEX teacher_ID_UNIQUE (teacher_ID ASC) VISIBLE,
                            UNIQUE INDEX email_UNIQUE (email ASC) VISIBLE)""")
      self.db.commit()

      # CREATING TABLE FOR TABLE CLASSROOM tbl_classroom
      c = self.db.execute("""
                            CREATE TABLE IF NOT EXISTS tbl_class_timetable(
                            class_ID INT(3) UNSIGNED ZEROFILL NOT NULL,
                            teacher_ID INT(3) UNSIGNED ZEROFILL NOT NULL,
                            student_ID INT(3) UNSIGNED ZEROFILL NOT NULL,
                            period_Number INT(1) NOT NULL
                            PRIMARY KEY (class_ID),
                            UNIQUE INDEX student_ID_UNIQUE (student_ID ASC) VISIBLE,
                            UNIQUE INDEX teacher_ID_UNIQUE (teacher_ID ASC) VISIBLE)""")
      self.db.commit()

      # CREATING TABLE FOR TABLE CLASSROOM tbl_classroom
      d = self.db.execute("""
                            CREATE TABLE IF NOT EXISTS tbl_class(
                            student_ID INT(3) UNSIGNED ZEROFILL NOT NULL,
                            teacher_ID INT(3) UNSIGNED ZEROFILL NOT NULL,
                            PRIMARY KEY (student_ID, teacher_ID)
                            UNIQUE INDEX student_ID_UNIQUE (student_ID ASC) VISIBLE,
                            UNIQUE INDEX teacher_ID_UNIQUE (teacher_ID ASC) VISIBLE)""")
      self.db.commit()

      # CREATING TABLE FOR TABLE 
      #e = self.db.execute("""

      #                      """)
      #self.db.commit()

      #f = self.db.execute("""

      #                      """)
      #self.db.commit()


