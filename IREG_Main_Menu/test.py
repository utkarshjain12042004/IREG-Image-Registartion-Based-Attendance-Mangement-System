# Importing all the required modules to create the UI
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import numpy as np
import cv2
import mysql.connector
from datetime import datetime

FONT1 = ("Calibri", 45)
FONT2 = ("Calibri", 15)
FONT3 = ("Calibri", 12)




class IREG(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        # We are giving the window a title. This remains the same for all frames which will be shown
        tk.Tk.wm_title(self, "IREG: Image Registration")
        tk.Tk.wm_frame(self)
        tk.Tk.wm_geometry(self, "1090x645+75+70")
        tk.Tk.wm_resizable(self, width=False, height=False)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Creating a dictionary of frames where all teh frames will be stored
        self.frames = {}

        # Adding the frames to the dictionary
        for F in (IREG_Main_Menu_Page, Start_Attendance_Page, Automated_Attendance_Method_Page, View_Attendance_Page, Student_Account_Management, Settings_Page):
            frame = F(container, self)
            frame.configure(bg="Black")
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        # This calls the show page function where the IREG_Main_Menu_Page is a parameter
        self.show_frame(IREG_Main_Menu_Page)

    # This function takes the container parameter which is essentially the index of the dictionary location of the frame to be shown
    def show_frame(self, cont):
        # Assigns the created frame at the dictionary location container
        frame = self.frames[cont]
        # This raises the frame to the top of the screen. This essentially means that this frame is displayed on top of the previous frame
        frame.tkraise()

class IREG_Main_Menu_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        IREG_Main_Menu_Label = tk.Label(self, text="IREG: Main Menu", font=FONT1)
        IREG_Main_Menu_Label.place(x=108, y=5, width=870, height=75)
        IREG_Main_Menu_Label.config(bg="Black", fg="White")

        #======================================== Adding in the buttons ========================================#
        # Adding the Start Attendance Button
        start_Attendance_Button = ttk.Button(self, text="Start Attendance", command=lambda: controller.show_frame(Start_Attendance_Page))
        start_Attendance_Button.place(x=395,y=175, width=300, height=50)

        # Adding the View Attendance
        view_Attendance_Button =  ttk.Button(self, text="View Attendance", command=lambda: controller.show_frame(View_Attendance_Page))
        view_Attendance_Button.place(x=395,y=230, width=300, height=50)

        # Adding the Account Management Button
        account_Management_Button = ttk.Button(self, text="Account Management", command=lambda: controller.show_frame(Student_Account_Management))
        account_Management_Button.place(x=395,y=285, width=300, height=50)

        # Adding the Exit Button
        exit_Button = ttk.Button(self, text="Exit", command=quit)
        exit_Button.place(x=395,y=340, width=300, height=50)
        
        # Adding the Settings Button
        settings_Button = ttk.Button(self, text="Settings", command=lambda: controller.show_frame(Settings_Page))
        settings_Button.place(x=981,y=595, width=100, height=40)

class Start_Attendance_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        Start_Attendance_lbl= tk.Label(self, text="Start Attendance", font=FONT1)
        Start_Attendance_lbl.place(x=108, y=5, width=870, height=75)
        Start_Attendance_lbl.config(bg="Black", fg="White")

        #======================================== Adding in the buttons ========================================#
        # Adding the manual attendance method button
        manual_attendance_method_button = ttk.Button(self, text="Manual Attendance Method", command=lambda: controller.show_frame(Start_Attendance_Page))
        manual_attendance_method_button.place(x=395,y=230, width=300, height=50)

        # Adding the manual attendance method button
        automated_attendance_method_button = ttk.Button(self, text="Automated Attendance Method", command=lambda: controller.show_frame(Automated_Attendance_Method_Page))
        automated_attendance_method_button.place(x=395,y=285, width=300, height=50)

        # Adding the back button
        back_button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(IREG_Main_Menu_Page))
        back_button.place(x=5,y=615)

class Automated_Attendance_Method_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        Automated_Attendance_Method_lbl = tk.Label(self, text="Automated Attendance Method", font=FONT1)
        Automated_Attendance_Method_lbl.place(x=108, y=5, width=870, height=75)
        Automated_Attendance_Method_lbl.config(bg="Black", fg="White")



class View_Attendance_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        # Adding the Page tk.Label
        View_Attendance_lbl= tk.Label(self, text="View Attendance", font=FONT1)
        View_Attendance_lbl.place(x=108, y=5, width=870, height=75)
        View_Attendance_lbl.config(bg="Black", fg="White")

        # Adding the headings to the rows and columns
        # Adding the headings to the columns
        #weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        #column_counter = 1
        #for day in weekdays:
        #    Weekday_lbl = tk.Label(self, text = f"{day}", font=FONT2, bd=2, relief=SOLID)
        #    Weekday_lbl.grid(row = 0, column = column_counter, pady=(90,0), sticky = NSEW)
        #    Weekday_lbl.config(bg="Black", fg="White")
        #    column_counter += 1


        # Monday tk.Label
        Monday_lbl = tk.Label(self, text = "Monday", font=FONT2, bd=2, relief=SOLID)
        Monday_lbl.grid(row = 0, column = 1, pady=(90,0), sticky = NSEW)
        Monday_lbl.config(bg="Black", fg="White")

        # Tuesday tk.Label
        Tuesday_lbl = tk.Label(self, text = "Tuesday", font=FONT2, bd=2, relief=SOLID)
        Tuesday_lbl.grid(row = 0, column = 2, pady=(90,0), sticky = NSEW)
        Tuesday_lbl.config(bg="Black", fg="White")

        # Wednesday tk.Label
        Wednesday_lbl = tk.Label(self, text = "Wednesday", font=FONT2, bd=2, relief=SOLID)
        Wednesday_lbl.grid(row = 0, column = 3, pady=(90,0), sticky = NSEW)
        Wednesday_lbl.config(bg="Black", fg="White")

        # Thurday tk.Label
        Thursday_lbl= tk.Label(self, text = "Thursday", font=FONT2, bd=2, relief=SOLID)
        Thursday_lbl.grid(row = 0, column = 4, pady=(90,0), sticky = NSEW)
        Thursday_lbl.config(bg="Black", fg="White")

        # Friday tk.Label
        Friday_lbl= tk.Label(self, text = "Friday", font=FONT2, bd=2, relief=SOLID)
        Friday_lbl.grid(row = 0, column = 5, pady=(90,0), sticky = NSEW)
        Friday_lbl.config(bg="Black", fg="White")

        # Adding the headings to the rows
        # Label for period 1
        Period_Number_One_lbl= tk.Label(self, text = "1", font=FONT2, bd=2, relief=SOLID, width=1)
        Period_Number_One_lbl.grid(row = 1, column = 0, padx=(4,0), sticky = NSEW)
        Period_Number_One_lbl.config(bg="Black", fg="White")

        # Label for period 2
        Period_Number_Two_lbl= tk.Label(self, text = "2", font=FONT2, bd=2, relief=SOLID, width=1)
        Period_Number_Two_lbl.grid(row = 2, column = 0, padx=(4,0),sticky = NSEW)
        Period_Number_Two_lbl.config(bg="Black", fg="White")

        # Label for period 3
        Period_Number_Three_lbl= tk.Label(self, text = "3", font=FONT2, bd=2, relief=SOLID, width=1)
        Period_Number_Three_lbl.grid(row = 3, column = 0, padx=(4,0), sticky = NSEW)
        Period_Number_Three_lbl.config(bg="Black", fg="White")

        # Label for period 4
        Period_Number_Four_lbl= tk.Label(self, text = "4", font=FONT2, bd=2, relief=SOLID, width=1)
        Period_Number_Four_lbl.grid(row = 4, column = 0, padx=(4,0), sticky = NSEW)
        Period_Number_Four_lbl.config(bg="Black", fg="White")

        # Label for period 5
        Period_Number_Five_lbl= tk.Label(self, text = "5", font=FONT2, bd=2, relief=SOLID)
        Period_Number_Five_lbl.grid(row = 5, column = 0, padx=(4,0), sticky = NSEW)
        Period_Number_Five_lbl.config(bg="Black", fg="White")

        
        period_Number_Counter = 1
        while (period_Number_Counter<=5):
            Period_Number_lbl = tk.Label(self, text = f"{period_Number_Counter}", font=FONT2, bd=2, relief=SOLID, width=1)
            Period_Number_lbl.grid(row = period_Number_Counter, column = 0, padx=(5,0), sticky = NSEW)
            Period_Number_lbl.config(bg="Black", fg="White")

            period_Number_Counter += 1

        

        # Adding the back button
        back_button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(IREG_Main_Menu_Page))
        back_button.place(x=5,y=615)

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
                period_Button = ttk.Button(self, text = f"""{data[0][1]}\n{data[0][2]}""", cursor = "hand2")
                period_Button.grid(row = row_counter, column = column_counter, padx=1, pady=1, ipady=25, ipadx=34,sticky=NSEW)
                column_counter += 1

            row_counter += 1

class Student_Account_Management(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        Student_Account_management_Lbl = tk.Label(self, text="Automated Attendance Method", font=FONT1)
        Student_Account_management_Lbl.place(x=108, y=5, width=870, height=75)
        Student_Account_management_Lbl.config(bg="Black", fg="White")

        # Variables related to the students
        self.var_student_ID = StringVar()
        self.var_student_email = StringVar()
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_date_of_admission = StringVar()
        self.var_date_of_birth = StringVar()
        
        # Variables related to the father
        self.var_father_first_name = StringVar()
        self.var_father_last_name = StringVar()
        self.var_father_email = StringVar()

        # Variables related to the mother
        self.var_mother_first_name = StringVar()
        self.var_mother_last_name = StringVar()
        self.var_mother_email = StringVar()

        # Search Variables
        self.var_search_by_combobox = StringVar()
        self.var_search = StringVar()
############################################################################################################################################
#==========================================================================================================================================#
#                                                                UI DESIGN
# =========================================================================================================================================#
# Adding in the student related text boxes and labels
        # Adding a student id label and textbox
        studentID_lbl = Label(self, text = "Student ID: ", font=FONT3)
        studentID_lbl.grid(row=0, column=0, padx=5, pady=(90,0), sticky=NSEW)
        studentID_lbl.config(bg="Black", fg="White")

        studentID_textbox = ttk.Entry(self, width=25, textvariable=self.var_student_ID, font=FONT3)
        studentID_textbox.grid(row=0, column=1, padx=5, pady=(90,0), sticky=W)

        # Adding a Student Email label and textbox
        student_email_lbl = Label(self, text = "Student Email: ", font=FONT3)
        student_email_lbl.grid(row=0, column=2, padx=5, pady=(90,0), sticky=NSEW)
        student_email_lbl.config(bg="Black", fg="White")

        student_email_textbox = ttk.Entry(self, width=25, textvariable=self.var_student_email, font=FONT3)
        student_email_textbox.grid(row=0, column=3, padx=5, pady=(90,0), sticky=W)

        # Adding a first name label and textbox
        first_name_lbl = Label(self, text = "First Name: ", font=FONT3)
        first_name_lbl.grid(row=2, column=0, padx=5, pady=(5,0), sticky=NSEW)
        first_name_lbl.config(bg="Black", fg="White")

        first_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_first_name, font=FONT3)
        first_name_textbox.grid(row=2, column=1, padx=5, pady=(5,0), sticky=W)

        # Adding a last label and textbox
        last_name_lbl = Label(self, text = "Last Name: ", font=FONT3)
        last_name_lbl.grid(row=2, column=2, padx=5, pady=(5,0), sticky=NSEW)
        last_name_lbl.config(bg="Black", fg="White")

        last_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_last_name, font=FONT3)
        last_name_textbox.grid(row=2, column=3, padx=5, pady=(5,0), sticky=W)

        # Adding a Student Date Of Admission label and textbox
        date_of_admission_lbl = Label(self, text = "Date Of Admission: ", font=FONT3)
        date_of_admission_lbl.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
        date_of_admission_lbl.config(bg="Black", fg="White")

        date_of_admission_textbox = ttk.Entry(self,width=25, textvariable=self.var_date_of_admission, font=FONT3)
        date_of_admission_textbox.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Adding a date of birth label and textbox
        date_of_birth_lbl = Label(self, text = "Date of Birth: ", font=FONT3)
        date_of_birth_lbl.grid(row=3, column=2, padx=5, pady=5, sticky=NSEW)
        date_of_birth_lbl.config(bg="Black", fg="White")

        date_of_birth_textbox = ttk.Entry(self,width=25, textvariable=self.var_date_of_birth, font=FONT3)
        date_of_birth_textbox.grid(row=3, column=3, padx=5, pady=5, sticky=W)




class Settings_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        Settings_Lbl = tk.Label(self, text="Automated Attendance Method", font=FONT1)
        Settings_Lbl.place(x=108, y=5, width=870, height=75)
        Settings_Lbl.config(bg="Black", fg="White")





app = IREG()
app.mainloop()


