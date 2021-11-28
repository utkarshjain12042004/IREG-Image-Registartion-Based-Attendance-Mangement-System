# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
import mysql.connector
from datetime import datetime



# Creating a class for the UI
class View_Attendance:
    # This is the constructor of the class Face_Recognition_System
    def __init__(self, root):
        self.root = root
        self.root.geometry("1090x645+75+70")
        self.root.resizable(width = False, height = False)
        self.root.title("IREG: Start Attendance")
        
        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd = 2, bg = "Light Yellow", relief = SOLID)
        mainFrame.place(x = 2, y = 2, width = 1086, height = 640) 

        # Label Frame
        View_Attendance_lbl =  Label(mainFrame, text = "IREG: View Attendance", font = ("Segoe UI Variable", 45, "bold"), bg = "Light Yellow", fg = "Black")
        View_Attendance_lbl.place(x = 108, y = 5, width = 870, height = 75)

        def update_current_date_and_time():
            # Obtaining the current Date and time labels
            current_date_and_time = datetime.now()

            # Current Day Label
            Current_Day_lbl = Label(mainFrame, text = datetime.today().strftime("%A"), font = ("Calibri", 12, "bold"), bg = "Light Yellow", fg = "Black")
            Current_Day_lbl.place(x = 1016, y = 71, width = 65, height = 15)

            # Current date label
            Current_Date_lbl =  Label(mainFrame, text = current_date_and_time.strftime("%d/%m/%y"), font = ("Calibri", 12, "bold"), bg = "Light Yellow", fg = "Black")
            Current_Date_lbl.place(x = 1016, y = 91, width = 65, height = 15)

            # Current time label
            Current_Time_lbl =  Label(mainFrame, text = current_date_and_time.strftime("%H:%M:%S"), font = ("Calibri", 12, "bold"), bg = "Light Yellow", fg = "Black")
            Current_Time_lbl.place(x = 1016, y = 111, width = 65, height = 15)

            root.after(1000, update_current_date_and_time())

        update_current_date_and_time()


        # Period Frame
        Period_Frame =  LabelFrame(mainFrame, bd = 2, bg = "Light Yellow", relief = SOLID, text = "Timetable", font = ("Segoe UI Variable", 12, "bold"))
        Period_Frame.place(x = 2, y = 131, width = 1078, height = 503)

        # Adding the headings to the rows and columns
        # Adding the headings to the columns
        # Monday Label
        Monday_label = Label(Period_Frame, text = "Monday", font = ("Segoe UI Variable", 12, "bold"), bg = "Light Yellow", bd=2, relief=SOLID)
        Monday_label.grid(row = 0, column = 1,sticky = NSEW)

        # Tuesday Label
        Tuesday_label = Label(Period_Frame, text = "Tuesday", font = ("Segoe UI Variable", 12, "bold"), bg = "Light Yellow", bd=2, relief=SOLID)
        Tuesday_label.grid(row = 0, column = 2,sticky = NSEW)

        # Wednesday Label
        Wednesday_label = Label(Period_Frame, text = "Wednesday", font = ("Segoe UI Variable", 12, "bold"), bg = "Light Yellow", bd=2, relief=SOLID)
        Wednesday_label.grid(row = 0, column = 3,sticky = NSEW)

        # Thurday Label
        Thursday_label = Label(Period_Frame, text = "Thursday", font = ("Segoe UI Variable", 12, "bold"), bg = "Light Yellow", bd=2, relief=SOLID)
        Thursday_label.grid(row = 0, column = 4,sticky = NSEW)

        # Friday Label
        Friday_label = Label(Period_Frame, text = "Friday", font = ("Segoe UI Variable", 12, "bold"), bg = "Light Yellow", bd=2, relief=SOLID)
        Friday_label.grid(row = 0, column = 5,sticky = NSEW)

        # Adding the headings to the rows
        # Label for period 1
        Period_Number_One_label = Label(Period_Frame, text = "1", font = ("Segoe UI Variable", 12, "bold"), bg = "Light Yellow", bd=2, relief=SOLID, width=1)
        Period_Number_One_label.grid(row = 1, column = 0, padx=(4,0), sticky = NSEW)

        # Label for period 2
        Period_Number_Two_label = Label(Period_Frame, text = "2", font = ("Segoe UI Variable", 12, "bold"), bg = "Light Yellow", bd=2, relief=SOLID, width=1)
        Period_Number_Two_label.grid(row = 2, column = 0, padx=(4,0),sticky = NSEW)

        # Label for period 3
        Period_Number_Three_label = Label(Period_Frame, text = "3", font = ("Segoe UI Variable", 12, "bold"), bg = "Light Yellow", bd=2, relief=SOLID, width=1)
        Period_Number_Three_label.grid(row = 3, column = 0, padx=(4,0), sticky = NSEW)

        # Label for period 4
        Period_Number_Four_label = Label(Period_Frame, text = "4", font = ("Segoe UI Variable", 12, "bold"), bg = "Light Yellow", bd=2, relief=SOLID, width=1)
        Period_Number_Four_label.grid(row = 4, column = 0, padx=(4,0), sticky = NSEW)

        # Label for period 5
        Period_Number_Five_label = Label(Period_Frame, text = "5", font = ("Segoe UI Variable", 12, "bold"), bg = "Light Yellow", bd=2, relief=SOLID)
        Period_Number_Five_label.grid(row = 5, column = 0, padx=(4,0), sticky = NSEW)

        # Adding the buttons
        # Period 1 Button
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "utkarshjain120", database = "ireg")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT Period_1 FROM tbl_timetable WHERE Timetable_ID = 1")
        subject_id = my_cursor.fetchall()[0][0]
        subject_query = "SELECT * FROM tbl_subjects WHERE Subject_ID = %s"
        my_cursor.execute(subject_query, (subject_id,))
        data = my_cursor.fetchall()
        conn.commit()
        conn.close()

        # Button Generator Loop
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "utkarshjain120", database = "ireg")
        my_cursor = conn.cursor()
        # Loop for generating buttons for Monday
        row_counter = 1
        while row_counter<=5:
            period_number = (f"Period_{row_counter}")
            column_counter = 1
            while column_counter<=5:
                subject_query = f"SELECT {period_number} FROM tbl_timetable WHERE Timetable_ID = %s"
                my_cursor.execute(subject_query, (column_counter,))
                subject_id = my_cursor.fetchall()[0][0]
                subject_query = "SELECT * FROM tbl_subjects WHERE Subject_ID = %s"
                my_cursor.execute(subject_query, (subject_id,))
                data = my_cursor.fetchall()

                # Adding the button
                period_Button = Button(Period_Frame, text = f"""{data[0][1]}
{data[0][2]}""", cursor = "hand2", font = ("Segoe UI Variable", 12, "bold"), bg = "Light Yellow", fg = "Black", width = 20, height = 4, bd=2, relief = SOLID)
                period_Button.config(anchor = CENTER)
                period_Button.grid(row = row_counter, column = column_counter)

                column_counter += 1

            row_counter += 1


        







#        while column_counter<5:
#            # Getting the subject ID which is the used to get the name and room of the subject 
#            subject_query = "SELECT Period_1 FROM tbl_timetable WHERE Timetable_ID = %s"
#            my_cursor.execute(subject_query, (column_counter+1,))
#            subject_id = my_cursor.fetchall()[0][0]
#            subject_query = "SELECT * FROM tbl_subjects WHERE Subject_ID = %s"
#            my_cursor.execute(subject_query, (subject_id,))
#            data = my_cursor.fetchall()

#            # Adding the button
#            period_Button = Button(Period_Frame, text = f"""{data[0][1]}
#{data[0][2]}""", cursor = "hand2", font = ("Segoe UI Variable", 12, "bold"), bg = "Light Yellow", fg = "Black", width = 20, height = 4, bd=2, relief = SOLID)
#            period_Button.config(anchor = CENTER)
#            period_Button.grid(row = 1, column = column_counter+1)

#            column_counter += 1

#        # Loop for generating buttons for Tuesday
#        column_counter1 = 0
#        while column_counter1<5:
#                # Getting the subject ID which is the used to get the name and room of the subject 
#                subject_query = "SELECT Period_2 FROM tbl_timetable WHERE Timetable_ID = %s"
#                my_cursor.execute(subject_query, (column_counter1+1,))
#                subject_id = my_cursor.fetchall()[0][0]
#                subject_query = "SELECT * FROM tbl_subjects WHERE Subject_ID = %s"
#                my_cursor.execute(subject_query, (subject_id,))
#                data = my_cursor.fetchall()

#                # Adding the button
#                period_Button = Button(Period_Frame, text = f"""{data[0][1]}
#{data[0][2]}""", cursor = "hand2", font = ("Segoe UI Variable", 12, "bold"), bg = "Black", fg = "Light Yellow", width = 20, height = 4)
#                period_Button.config(anchor = CENTER)
#                period_Button.grid(row = 2, column = column_counter1+1, pady=5)

#                column_counter1 += 1
        
#        # Loop for generating buttons for Wednesday
#        column_counter2 = 0
#        while column_counter2<5:
#            # Getting the subject ID which is the used to get the name and room of the subject 
#            subject_query = "SELECT Period_3 FROM tbl_timetable WHERE Timetable_ID = %s"
#            my_cursor.execute(subject_query, (column_counter2+1,))
#            subject_id = my_cursor.fetchall()[0][0]
#            subject_query = "SELECT * FROM tbl_subjects WHERE Subject_ID = %s"
#            my_cursor.execute(subject_query, (subject_id,))
#            data = my_cursor.fetchall()
        
#            # Adding the button
#            period_Button = Button(Period_Frame, text = f"""{data[0][1]}
#{data[0][2]}""", cursor = "hand2", font = ("Segoe UI Variable", 12, "bold"), bg = "Black", fg = "Light Yellow", width = 20, height = 4)
#            period_Button.config(anchor = CENTER)
#            period_Button.grid(row = 3, column = column_counter2+1, pady=5)
        
#            column_counter2 += 1

#        # Loop for generating buttons for Thursday
#        column_counter3 = 0
#        while column_counter3<5:
#            # Getting the subject ID which is the used to get the name and room of the subject 
#            subject_query = "SELECT Period_4 FROM tbl_timetable WHERE Timetable_ID = %s"
#            my_cursor.execute(subject_query, (column_counter3+1,))
#            subject_id = my_cursor.fetchall()[0][0]
#            subject_query = "SELECT * FROM tbl_subjects WHERE Subject_ID = %s"
#            my_cursor.execute(subject_query, (subject_id,))
#            data = my_cursor.fetchall()
            
#            # Adding the button
#            period_Button = Button(Period_Frame, text = f"""{data[0][1]}
#{data[0][2]}""", cursor = "hand2", font = ("Segoe UI Variable", 12, "bold"), bg = "Black", fg = "Light Yellow", width = 20, height = 4)
#            period_Button.config(anchor = CENTER)
#            period_Button.grid(row = 4, column = column_counter3+1, pady=5)

#            column_counter3 += 1

#        # Loop for generating buttons for Friday
#        column_counter4 = 0
#        while column_counter4<5:
#            # Getting the subject ID which is the used to get the name and room of the subject 
#            subject_query = "SELECT Period_5 FROM tbl_timetable WHERE Timetable_ID = %s"
#            my_cursor.execute(subject_query, (column_counter4+1,))
#            subject_id = my_cursor.fetchall()[0][0]
#            subject_query = "SELECT * FROM tbl_subjects WHERE Subject_ID = %s"
#            my_cursor.execute(subject_query, (subject_id,))
#            data = my_cursor.fetchall()
            
#            # Adding the button
#            period_Button = Button(Period_Frame, text = f"""{data[0][1]}
#{data[0][2]}""", cursor = "hand2", font = ("Segoe UI Variable", 12, "bold"), bg = "Black", fg = "Light Yellow", width = 20, height = 4)
#            period_Button.config(anchor = CENTER)
#            period_Button.grid(row = 5, column = column_counter4+1, pady=5)

#            column_counter4 += 1










# This piece of code helps in calling class Face_Recognition_System
if __name__ == "__main__":
    root = Tk()
    obj = View_Attendance(root)
    root.mainloop()


