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
FONT2 = ("Calibri", 16)
FONT3 = ("Calibri", 14)

deleted = []

class IREG(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # We are giving the window a title. This remains the same for all frames which will be shown
        tk.Tk.wm_title(self, "IREG: Image Registration")
        tk.Tk.wm_frame(self)
        tk.Tk.wm_geometry(self, "1280x800+0+0")
        self.state("zoomed")
        tk.Tk.wm_resizable(self, width=False, height=False)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Creating a dictionary of frames where all the frames will be stored
        self.frames = {}

        # Adding the frames to the dictionary
        for F in (IREG_Main_Menu_Page, Start_Attendance_Page, Automated_Attendance_Method_Page, View_Attendance_Page, Student_Account_Management_Menu_Page, Add_New_Student_Details_Page, Update_Student_Details, Delete_Student_Details, Settings_Page):
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
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #
class IREG_Main_Menu_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        IREG_Main_Menu_Label = tk.Label(self, text="IREG: Main Menu", font=FONT1)
        IREG_Main_Menu_Label.place(x=205, y=5, width=870, height=75)
        IREG_Main_Menu_Label.config(bg="Black", fg="White")

        style = ttk.Style()
        style.configure("big.TButton", font=('Calibri', 20))
        #======================================== Adding in the buttons ========================================#
        # Adding the Start Attendance Button
        start_Attendance_Button = ttk.Button(self, text="Start Attendance", command=lambda: controller.show_frame(Start_Attendance_Page), style="big.TButton")
        start_Attendance_Button.place(x=440, y=240, width=400, height=50)

        # Adding the View Attendance
        view_Attendance_Button =  ttk.Button(self, text="View Attendance", command=lambda: controller.show_frame(View_Attendance_Page), style="big.TButton")
        view_Attendance_Button.place(x=440, y=300, width=400, height=50)

        # Adding the Account Management Button
        account_Management_Button = ttk.Button(self, text="Account Management", command=lambda: controller.show_frame(Student_Account_Management_Menu_Page), style="big.TButton")
        account_Management_Button.place(x=440, y=360, width=400, height=50)

        # Adding the Settings Button
        settings_Button = ttk.Button(self, text="Settings", command=lambda: controller.show_frame(Settings_Page), style="big.TButton")
        settings_Button.place(x=440, y=420, width=400, height=50)

        # Adding the Exit Button
        exit_Button = ttk.Button(self, text="Exit", command=lambda: IREG.quit(self), style="big.TButton")
        exit_Button.place(x=440, y=480, width=400, height=50)
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #
class Start_Attendance_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        Start_Attendance_lbl= tk.Label(self, text="Start Attendance", font=FONT1)
        Start_Attendance_lbl.place(x=205, y=5, width=870, height=75)
        Start_Attendance_lbl.config(bg="Black", fg="White")

        style = ttk.Style()
        style.configure("big.TButton", font=('Calibri', 20))

        #======================================== Adding in the buttons ========================================#
        # Adding the manual attendance method button
        manual_attendance_method_button = ttk.Button(self, text="Manual Attendance Method", command=lambda: controller.show_frame(Start_Attendance_Page), style="big.TButton")
        manual_attendance_method_button.place(x=440,y=310, width=400, height=50)

        # Adding the manual attendance method button
        automated_attendance_method_button = ttk.Button(self, text="Automated Attendance Method", command=lambda: controller.show_frame(Automated_Attendance_Method_Page), style="big.TButton")
        automated_attendance_method_button.place(x=440,y=370, width=400, height=50)

        # Adding the back button
        back_button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(IREG_Main_Menu_Page))
        back_button.place(x=5,y=5)
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #
class Automated_Attendance_Method_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        Automated_Attendance_Method_lbl = tk.Label(self, text="Automated Attendance Method", font=FONT1)
        Automated_Attendance_Method_lbl.place(x=205, y=5, width=870, height=75)
        Automated_Attendance_Method_lbl.config(bg="Black", fg="White")

        # Adding the back button
        back_button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(IREG_Main_Menu_Page))
        back_button.place(x=5,y=5)

    #                                                            END OF UI DESIGN
    #===========================================================================================================================================#
    #############################################################################################################################################
    #===========================================================================================================================================#
    #                                                      BUTTON IMPLEMENTATION FUNCTIONS
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Function for marking the student attendance in the class based on the results of face recognition
    def automated_attendance(self, student_id, first_name, last_name):
        with open("C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance.csv","r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []

            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])

            if ((student_id not in name_list)):
                now = datetime.now()
                attendance_time = now.strftime("%d/%m/%Y")
                attendance_date = now.strftime("%H:%M:%S")
                name_list.append(student_id)
                print(student_id in name_list)
                f.writelines(f"\n{student_id},{first_name},{last_name},{attendance_date},{attendance_time},Present")
# ========================================================================================================================================= #
    # Button Implementation
    def face_recognition(self):
        # Corresponding Functions
        #def grayscaling_image(img):
        #    pixel_array = asarray(img)

        def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text, clf,):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbour)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0 ,255, 0), 3)
                id,predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
                my_cursor = conn.cursor()


                my_cursor.execute("SELECT * FROM tbl_Student WHERE Student_ID=" + str(id))
                data = my_cursor.fetchall()
                fetch_student_id = data[0][0]
                fetch_first_name = data[0][1]
                fetch_last_name = data[0][2]

                # Confidence is the percentage of difference from the original image. Lower the confidence, the result is more 
                # accurate and vice versa
                if confidence > 77:
                    cv2.putText(img, f"Student ID: {fetch_student_id}", (x, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 3)
                    cv2.putText(img, f"First Name: {fetch_first_name}", (x, y-35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 3)
                    cv2.putText(img, f"Last Name: {fetch_last_name}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 3)
                    self.automated_attendance(fetch_student_id, fetch_first_name, fetch_last_name)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0 , 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (000, 000, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognise(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/Trained_Faces.xml")

        video_Capture = cv2.VideoCapture(0)

        while True:
            ret, img = video_Capture.read()
            img = recognise(img, clf, faceCascade)
            cv2.imshow("Welcome to IREG", img)

            if cv2.waitKey(1)==13:
                break
            
        video_Capture.release()
        cv2.destroyAllWindows()
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #
class View_Attendance_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        style = ttk.Style()
        style.configure("big.TButton", font=('Calibri', 12), bg="White", fg="Black")

        # Adding the Page tk.Label
        View_Attendance_lbl= tk.Label(self, text="View Attendance", font=FONT1)
        View_Attendance_lbl.place(x=205, y=5, width=870, height=75)
        View_Attendance_lbl.config(bg="Black", fg="White")

        # Adding the headings to the rows and columns
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        column_counter = 1
        for day in weekdays:
            Weekday_lbl = tk.Label(self, text=f"{day}", font=FONT2, bd=2, relief=SOLID)
            Weekday_lbl.grid(row = 0, column = column_counter, pady=(100,0), sticky = NSEW)
            Weekday_lbl.config(bg="Black", fg="White")
            column_counter += 1

        # Setting the labels on the row
        period_Number_Counter = 1
        while (period_Number_Counter<=5):
            Period_Number_lbl = tk.Label(self, text=f"{period_Number_Counter}", font=FONT2, bd=2, relief=SOLID, width=5)
            Period_Number_lbl.grid(row = period_Number_Counter, column = 0, padx=(5,0), sticky = NSEW)
            Period_Number_lbl.config(bg="Black", fg="White")

            period_Number_Counter += 1

        # Adding the back button
        back_button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(IREG_Main_Menu_Page))
        back_button.place(x=5,y=5)

        ## Button Generator Loop
        #conn = mysql.connector.connect(host = "localhost", username = "root", password = "utkarshjain120", database = "ireg")
        #my_cursor = conn.cursor()
        ## Loop for generating buttons for Monday
        #row_counter = 1
        #while row_counter<=5:
        #    period_number = (f"Period_{row_counter}")
        #    column_counter = 1
        #    while column_counter<=5:
        #        subject_query = f"SELECT {period_number} FROM tbl_timetable WHERE Timetable_ID = %s"
        #        my_cursor.execute(subject_query, (column_counter,))
        #        subject_id = my_cursor.fetchall()[0][0]
        #        subject_query = "SELECT * FROM tbl_subjects WHERE Subject_ID = %s"
        #        my_cursor.execute(subject_query, (subject_id,))
        #        data = my_cursor.fetchall()

        #        # Adding the button
        #        period_Button = ttk.Button(self, text=f"""{data[0][1]}\n{data[0][2]}""", cursor = "hand2", style="big.TButton")
        #        period_Button.grid(row = row_counter, column = column_counter, padx=2, pady=2, ipady=37, ipadx=35,sticky=NSEW)
        #        column_counter += 1

        #    row_counter += 1

        # Estabilishing the connection between this code and the database
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "utkarshjain120", database = "ireg")
        my_cursor = conn.cursor()

        # Monday Period 1 Button
        # Getting all the data to be added in the button
        subject_query = f"SELECT Period_1 FROM tbl_timetable WHERE Timetable_ID = %s"
        my_cursor.execute(subject_query, (1,))
        subject_id = my_cursor.fetchall()[0][0]
        subject_query = "SELECT * FROM tbl_subjects WHERE Subject_ID = %s"
        my_cursor.execute(subject_query, (subject_id,))
        data = my_cursor.fetchall()

        # Adding in the button
        monday_period_1_Button = ttk.Button(self, text=f"""{data[0][1]}\n{data[0][2]}""", cursor = "hand2", style="big.TButton")
        monday_period_1_Button.grid(row = 1, column = 1, padx=2, pady=2, ipady=37, ipadx=35,sticky=NSEW)
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
class Student_Account_Management_Menu_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Student Account Management Menu Label
        Student_Account_Management_Menu_Lbl = tk.Label(self, text="Student Account Management", font=FONT1)
        Student_Account_Management_Menu_Lbl.place(x=205, y=5, width=870, height=75)
        Student_Account_Management_Menu_Lbl.config(bg="Black", fg="White")

        style = ttk.Style()
        style.configure("big.TButton", font=('Calibri', 20))
        #======================================== Adding in the buttons ========================================#
        # Adding the View Attendance
        add_new_student_Button =  ttk.Button(self, text="Add New Student", command=lambda: controller.show_frame(Add_New_Student_Details_Page), style="big.TButton")
        add_new_student_Button.place(x=440, y=300, width=400, height=50)

        # Adding the Account Management Button
        update_student_details_Button = ttk.Button(self, text="Update Student Details", command=lambda: controller.show_frame(Update_Student_Details), style="big.TButton")
        update_student_details_Button.place(x=440, y=360, width=400, height=50)

        # Adding the Exit Button
        delete_student_Button = ttk.Button(self, text="Delete Student Record", command=lambda: controller.show_frame(Delete_Student_Details), style="big.TButton")
        delete_student_Button.place(x=440, y=480, width=400, height=50)

        # Adding the back button
        back_button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(IREG_Main_Menu_Page))
        back_button.place(x=5,y=5)
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #
class Add_New_Student_Details_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        Student_Account_management_Lbl = tk.Label(self, text="Student Account Management", font=FONT1)
        Student_Account_management_Lbl.place(x=205, y=5, width=870, height=75)
        Student_Account_management_Lbl.config(bg="Black", fg="White")

        style = ttk.Style()
        style.configure("big.TButton", font=('Calibri', 12), bg="Black", fg="White")

        # Variables related to the students
        self.var_student_ID = StringVar()
        self.var_student_email = StringVar()
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_date_of_admission = StringVar()
        self.var_date_of_birth = StringVar()
        
        # Variables related to the father
        self.var_father_name = StringVar()
        self.var_father_email = StringVar()

        # Variables related to the mother
        self.var_mother_name = StringVar()
        self.var_mother_email = StringVar()

        # Search Variables
        self.var_search_by_combobox = StringVar()
        self.var_search = StringVar()
    ############################################################################################################################################
    #==========================================================================================================================================#
    #                                                                UI DESIGN
    # =========================================================================================================================================#
    # Adding in the student related text boxes and labels
        # Creating a new Student ID
        # - Estabilishing the connectin between this project and the database
        conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
        my_cursor = conn.cursor()
        # - Getting all the student IDs from the IREG Database and storing them in the form of an array named student_IDs. 
        my_cursor.execute("SELECT Student_ID FROM tbl_student")
        student_IDs = my_cursor.fetchall()

        # This checks if the number of student profiles stored in the tbl_student table of the database is 0 or not. If it is 0, the 
        # system automatically assigns the student ID as 0.
        if len(student_IDs)==0:
            self.var_student_ID = str(1)
        # If not, it uses the length of the student ID array which contains all the student IDs. Since the student IDs are generated
        # in an orderly fashion. The length of the student IDs helps us to find a starting point for the last student ID used. This 
        # is useful because if any deletions are made, it would reduce the number of profiles but the student IDs would still be present. 
        # This would cause overlaps and would give an error during the database insertion due to duplicate primary key. We find the 
        # primary key by checking if the student ID at that index is present or not. If there is a student Id at that index, we add 
        # 1 to the index and then check it again until we find a free spot. This index is allotted as the student ID
        else:
            last_student_ID = student_IDs[len(student_IDs)-1][0]
            while last_student_ID in student_IDs:
                last_student_ID += 1
            self.var_student_ID = last_student_ID + 1
        conn.close()

        # Adding a student id label and textbox
        studentID_lbl = Label(self, text="Student ID: ", font=FONT3)
        studentID_lbl.grid(row=0, column=0, padx=(150,18), pady=(220,18), sticky=E)
        studentID_lbl.config(bg="Black", fg="White")

        self.new_studentID_lbl = Label(self, text=self.var_student_ID, font=FONT3)
        self.new_studentID_lbl.grid(row=0, column=1, padx=18, pady=(220,18), sticky=W)
        self.new_studentID_lbl.config(bg="Black", fg="White")

        # Adding a Student Email label and textbox
        student_email_lbl = Label(self, text="Student Email: ", font=FONT3)
        student_email_lbl.grid(row=0, column=2, padx=18, pady=(220, 18), sticky=E)
        student_email_lbl.config(bg="Black", fg="White")

        student_email_textbox = ttk.Entry(self, width=25, textvariable=self.var_student_email, font=FONT3)
        student_email_textbox.grid(row=0, column=3, padx=18, pady=(220,18), sticky=W)

        # Adding a first name label and textbox
        first_name_lbl = Label(self, text="First Name: ", font=FONT3)
        first_name_lbl.grid(row=2, column=0, padx=(150,18), pady=18, sticky=E)
        first_name_lbl.config(bg="Black", fg="White")

        first_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_first_name, font=FONT3)
        first_name_textbox.grid(row=2, column=1, padx=18, pady=18, sticky=W)

        # Adding a last label and textbox
        last_name_lbl = Label(self, text="Last Name: ", font=FONT3)
        last_name_lbl.grid(row=2, column=2, padx=18, pady=18, sticky=E)
        last_name_lbl.config(bg="Black", fg="White")

        last_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_last_name, font=FONT3)
        last_name_textbox.grid(row=2, column=3, padx=18, pady=18, sticky=W)

        # Adding a Student Date Of Admission label and textbox
        date_of_admission_lbl = Label(self, text="Date Of Admission: ", font=FONT3)
        date_of_admission_lbl.grid(row=3, column=0, padx=(150,18), pady=18, sticky=E)
        date_of_admission_lbl.config(bg="Black", fg="White")

        date_of_admission_textbox = ttk.Entry(self,width=25, textvariable=self.var_date_of_admission, font=FONT3)
        date_of_admission_textbox.grid(row=3, column=1, padx=18, pady=18, sticky=W)

        # Adding a date of birth label and textbox
        date_of_birth_lbl = Label(self, text="Date of Birth: ", font=FONT3)
        date_of_birth_lbl.grid(row=3, column=2, padx=18, pady=18, sticky=E)
        date_of_birth_lbl.config(bg="Black", fg="White")

        date_of_birth_textbox = ttk.Entry(self,width=25, textvariable=self.var_date_of_birth, font=FONT3)
        date_of_birth_textbox.grid(row=3, column=3, padx=18, pady=18, sticky=W)

        # Father's Information
        # Adding a father first name label and textbox
        father_name_lbl = Label(self, text="Father's Name: ", font=FONT3)
        father_name_lbl.grid(row=4, column=0, padx=(150,18), pady=18, sticky=E)
        father_name_lbl.config(bg="Black", fg="White")

        father_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_father_name, font=FONT3)
        father_name_textbox.grid(row=4, column=1, padx=18, pady=18, sticky=W)

        # Adding father's email label and text box
        father_email_lbl = Label(self, text="Father's Email: ", font=FONT3)
        father_email_lbl.grid(row=4, column=2, padx=18, pady=18, sticky=E)
        father_email_lbl.config(bg="Black", fg="White")

        father_email_textbox = ttk.Entry(self, width=25, textvariable=self.var_father_email, font=FONT3)
        father_email_textbox.grid(row=4, column=3, padx=18, pady=18, sticky=W)

        # Mother's Information
        # Adding a father first name label and textbox
        mother_name_lbl = Label(self, text="Mother's Name: ", font=FONT3)
        mother_name_lbl.grid(row=5, column=0, padx=(150,18), pady=18, sticky=E)
        mother_name_lbl.config(bg="Black", fg="White")

        mother_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_mother_name, font=FONT3)
        mother_name_textbox.grid(row=5, column=1, padx=18, pady=18, sticky=W)

        # Adding father's email label and text box
        mother_email_lbl = Label(self, text="Mother's Email: ", font=FONT3)
        mother_email_lbl.grid(row=5, column=2, padx=4, pady=18, sticky=E)
        mother_email_lbl.config(bg="Black", fg="White")

        mother_email_textbox = ttk.Entry(self, width=25, textvariable=self.var_mother_email, font=FONT3)
        mother_email_textbox.grid(row=5, column=3, padx=18, pady=18, sticky=W)
        # UI Design for getting the student's and their parents information completed
        # --------------------------------------------------------------------------- #
        # UI Design for the buttons to add, delete, update the student accounts
        # Add Student button
        add_student_button = ttk.Button(self, text="Add Student", style="big.TButton", command=self.add_student_button)
        add_student_button.place(x=5, y=680, width=420, height=90)

        # Adding a capture face button below the label
        capture_face_button = ttk.Button(self, text="Capture Face Student", style="big.TButton", command=self.capture_face_button)
        capture_face_button.place(x=430, y=680, width=420, height=90)

        # Clear All Data button
        clear_all_button = ttk.Button(self, text="Clear All Fields", style="big.TButton", command=self.clear_all_button)
        clear_all_button.place(x=855, y=680, width=420, height=90)

        # Adding the back button
        back_button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(Student_Account_Management_Menu_Page))
        back_button.place(x=5,y=5)
    #                                                            END OF UI DESIGN
    #===========================================================================================================================================#
    #############################################################################################################################################
    #===========================================================================================================================================#
    #                                                      BUTTON IMPLEMENTATION FUNCTIONS
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Function for adding in the data when the user clicks on the add student button
    def add_student_button(self):
        if self.var_student_ID=="" or self.var_student_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_admission.get()=="" or self.var_date_of_birth.get()=="" or self.var_father_name.get()=="" or self.var_father_email.get()=="" or self.var_mother_name.get()=="" or self.var_mother_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO tbl_student VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                                                                                         self.var_student_ID[0],
                                                                                                         self.var_first_name.get(),
                                                                                                         self.var_last_name.get(),
                                                                                                         self.var_student_email.get(),
                                                                                                         self.var_date_of_admission.get(),
                                                                                                         self.var_date_of_birth.get(),
                                                                                                         self.var_father_name.get(),
                                                                                                         self.var_father_email.get(),
                                                                                                         self.var_mother_name.get(),
                                                                                                         self.var_mother_email.get()
                                                                                                        ))
                conn.commit()
                conn.close()
                self.var_student_ID = f"{int(self.var_student_ID) + 1}"
                self.new_studentID_lbl.config(text=self.var_student_ID)
                self.clear_all_button()
                messagebox.showinfo("Success", "Student details have been added succesfully", parent=self)

                # Adding Student to the class table
                conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
                my_cursor = conn.cursor()
                my_cursor.execute("Select")

            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self)
    # ------------------------------------------------------------------------------------------------------------------------------------------#
        # Funtion to fetch the date in the table frame created
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM tbl_student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    # ---------------------------------------------------------------------------------------------------------------------------------------
    # Get Cursor
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_student_ID=(data[0]),
        self.new_studentID_lbl.config(text=self.var_student_ID)
        self.var_first_name.set(data[1]),
        self.var_last_name.set(data[2]),
        self.var_student_email.set(data[3]),
        self.var_date_of_admission.set(data[4]),
        self.var_date_of_birth.set(data[5]),
        self.var_father_name.set(data[6]),
        self.var_father_email.set(data[7]),
        self.var_mother_name.set(data[8]),
        self.var_mother_email.set(data[9])
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Clear All Fields button Implementation
    def clear_all_button(self):
        self.var_student_ID = (""),
        self.var_student_email.set(""),
        self.var_first_name.set(""),
        self.var_last_name.set(""),
        self.var_date_of_admission.set(""),
        self.var_date_of_birth.set(""),
        self.var_father_name.set(""),
        self.var_father_email.set(""),
        self.var_mother_name.set(""),
        self.var_mother_email.set("")
    # -------------------------------------------------------------------------------------------------------------------------------------------#
    # Capture Student Face button implementation
    def capture_face_button(self):
        # Validation that all fields are filled up
        if self.var_student_ID=="" or self.var_student_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_admission.get()=="" or self.var_date_of_birth.get()=="" or self.var_father_name.get()=="" or self.var_father_email.get()=="" or self.var_mother_name.get()=="" or self.var_mother_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self)
        else:
            # Added a try box to get rid of any exceptions which might arise
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
                my_cursor = conn.cursor()
                # Selected all the data from the database and stored it in the variable myresult
                my_cursor.execute("SELECT * FROM tbl_student")
                myresult = my_cursor.fetchall()
                # We match the images to an id
                id=0
                # Therfore, we create a loop to manage the IDs
                for x in myresult:
                    id += 1
                my_cursor.execute("UPDATE tbl_student SET First_Name=%s, Last_Name=%s, Email=%s, date_of_admission=%s, Date_Of_Birth=%s, Father_Name=%s, Father_Email=%s, Mother_Name=%s, Mother_Email=%s WHERE Student_ID=%s",(
                                                                                                         self.var_first_name.get(),
                                                                                                         self.var_last_name.get(),
                                                                                                         self.var_student_email.get(),
                                                                                                         self.var_date_of_admission.get(),
                                                                                                         self.var_date_of_birth.get(),
                                                                                                         self.var_father_name.get(),
                                                                                                         self.var_father_email.get(),
                                                                                                         self.var_mother_name.get(),
                                                                                                         self.var_mother_email.get(),
                                                                                                         self.var_student_ID==id+1
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.clear_all_button()
                conn.close()
                # =========== Load predifined data on face frontals from Open CV. Loading Haarcascade frontal image default =========== #
                # ideally, we need to give the path of the location of teh haarcascasde file. But in this case, the haarcascade has been 
                # copied to the code folder and therefore we do not necessaily need to provide a path for it.
                face_classifier = cv2.CascadeClassifier("C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/haarcascade_frontalface_default.xml") 
                # ----------------------------------------------------------------------------------------------------------------------- #
                # Supplementary functions
                # Cropping the video footage and focussing specifially on the face
                def face_cropped(img):
                    # Converting a Blue Green Red BGR image to grayscale form
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces =  face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scalinng Factor = 1.3
                    # Minimum Neighbour = 6
                
                    for(x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        print(face_cropped)
                        return face_cropped
               
            # ---------------------------------------------------------------------------------------------------------------------------- #
                # The 0 here is an extension for the camera footage. If I want it to read a video file, I need to add in the video 
                # location. By this line, we are accessing the camera footage
                cap = cv2.VideoCapture(0)

                img_id = 0
                while True:
                    ret, face_Frame = cap.read()
                    if face_cropped(face_Frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(face_Frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/Data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Capture Face", face)

                    if cv2.waitKey(1)==13 or int(img_id==100):
                        break
                cap.release()
                cv2.destroyWindow("Capture Face")
                self.train_data_button()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self)
    # ------------------------------------------------------------------------------------------------------------------------ #
    # Train the classifier using these face captures
    def train_data_button(self):
        data_dir = ("C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/Data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for face in path:
            img = Image.open(face).convert("L") # Grey Scale Image
            imageNP = np.array(img, 'uint8') # Converting gray scale image to an array of data type uint
            face_ID = int(os.path.split(face)[1].split(".")[1])

            faces.append(imageNP)
            ids.append(face_ID)
            cv2.imshow("Training", imageNP)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        # Train Classifier and Save
        classifier = cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces, ids)
        classifier.write("C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/Trained_Faces.xml")
        cv2.destroyWindow("Training")
        messagebox.showinfo("Train Face Data", "Datasets have been trained using the student faces")
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #
class Update_Student_Details(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        Student_Account_management_Lbl = tk.Label(self, text="Student Account Management", font=FONT1)
        Student_Account_management_Lbl.place(x=205, y=5, width=870, height=75)
        Student_Account_management_Lbl.config(bg="Black", fg="White")

        style = ttk.Style()
        style.configure("big.TButton", font=('Calibri', 12), bg="Black", fg="White")

        # Variables related to the students
        self.var_student_ID = StringVar()
        self.var_student_email = StringVar()
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_date_of_admission = StringVar()
        self.var_date_of_birth = StringVar()
        
        # Variables related to the father
        self.var_father_name = StringVar()
        self.var_father_email = StringVar()

        # Variables related to the mother
        self.var_mother_name = StringVar()
        self.var_mother_email = StringVar()

        # Search Variables
        self.var_search_by_combobox = StringVar()
        self.var_search = StringVar()
    ############################################################################################################################################
    #==========================================================================================================================================#
    #                                                                UI DESIGN
    # =========================================================================================================================================#
    # Adding in the student related text boxes and labels
        # Creating a new Student ID
        self.var_student_ID = ""

        # Adding a student id label and textbox
        studentID_lbl = Label(self, text="Student ID: ", font=FONT3)
        studentID_lbl.grid(row=0, column=0, padx=5, pady=(105,18), sticky=E)
        studentID_lbl.config(bg="Black", fg="White")

        self.new_studentID_lbl = Label(self, text=self.var_student_ID, font=FONT3)
        self.new_studentID_lbl.grid(row=0, column=1, padx=5, pady=(105,18), sticky=W)
        self.new_studentID_lbl.config(bg="Black", fg="White")

        # Adding a Student Email label and textbox
        student_email_lbl = Label(self, text="Student Email: ", font=FONT3)
        student_email_lbl.grid(row=0, column=2, padx=5, pady=(105, 18), sticky=E)
        student_email_lbl.config(bg="Black", fg="White")

        student_email_textbox = ttk.Entry(self, width=25, textvariable=self.var_student_email, font=FONT3)
        student_email_textbox.grid(row=0, column=3, padx=5, pady=(105,18), sticky=W)

        # Adding a first name label and textbox
        first_name_lbl = Label(self, text="First Name: ", font=FONT3)
        first_name_lbl.grid(row=2, column=0, padx=5, pady=18, sticky=E)
        first_name_lbl.config(bg="Black", fg="White")

        first_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_first_name, font=FONT3)
        first_name_textbox.grid(row=2, column=1, padx=5, pady=18, sticky=W)

        # Adding a last label and textbox
        last_name_lbl = Label(self, text="Last Name: ", font=FONT3)
        last_name_lbl.grid(row=2, column=2, padx=5, pady=18, sticky=E)
        last_name_lbl.config(bg="Black", fg="White")

        last_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_last_name, font=FONT3)
        last_name_textbox.grid(row=2, column=3, padx=5, pady=18, sticky=W)

        # Adding a Student Date Of Admission label and textbox
        date_of_admission_lbl = Label(self, text="Date Of Admission: ", font=FONT3)
        date_of_admission_lbl.grid(row=3, column=0, padx=5, pady=18, sticky=E)
        date_of_admission_lbl.config(bg="Black", fg="White")

        date_of_admission_textbox = ttk.Entry(self,width=25, textvariable=self.var_date_of_admission, font=FONT3)
        date_of_admission_textbox.grid(row=3, column=1, padx=5, pady=18, sticky=W)

        # Adding a date of birth label and textbox
        date_of_birth_lbl = Label(self, text="Date of Birth: ", font=FONT3)
        date_of_birth_lbl.grid(row=3, column=2, padx=5, pady=18, sticky=E)
        date_of_birth_lbl.config(bg="Black", fg="White")

        date_of_birth_textbox = ttk.Entry(self,width=25, textvariable=self.var_date_of_birth, font=FONT3)
        date_of_birth_textbox.grid(row=3, column=3, padx=5, pady=18, sticky=W)

        # Father's Information
        # Adding a father first name label and textbox
        father_name_lbl = Label(self, text="Father's Name: ", font=FONT3)
        father_name_lbl.grid(row=4, column=0, padx=4, pady=18, sticky=E)
        father_name_lbl.config(bg="Black", fg="White")

        father_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_father_name, font=FONT3)
        father_name_textbox.grid(row=4, column=1, padx=5, pady=18, sticky=W)

        # Adding father's email label and text box
        father_email_lbl = Label(self, text="Father's Email: ", font=FONT3)
        father_email_lbl.grid(row=4, column=2, padx=4, pady=18, sticky=E)
        father_email_lbl.config(bg="Black", fg="White")

        father_email_textbox = ttk.Entry(self, width=25, textvariable=self.var_father_email, font=FONT3)
        father_email_textbox.grid(row=4, column=3, padx=5, pady=18, sticky=W)

        # Mother's Information
        # Adding a father first name label and textbox
        mother_name_lbl = Label(self, text="Mother's Name: ", font=FONT3)
        mother_name_lbl.grid(row=5, column=0, padx=4, pady=18, sticky=E)
        mother_name_lbl.config(bg="Black", fg="White")

        mother_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_mother_name, font=FONT3)
        mother_name_textbox.grid(row=5, column=1, padx=5, pady=18, sticky=W)

        # Adding father's email label and text box
        mother_email_lbl = Label(self, text="Mother's Email: ", font=FONT3)
        mother_email_lbl.grid(row=5, column=2, padx=4, pady=18, sticky=E)
        mother_email_lbl.config(bg="Black", fg="White")

        mother_email_textbox = ttk.Entry(self, width=25, textvariable=self.var_mother_email, font=FONT3)
        mother_email_textbox.grid(row=5, column=3, padx=5, pady=18, sticky=W)
        # UI Design for getting the student's and their parents information completed
        # --------------------------------------------------------------------------- #
        # Adding the buttons and textboxes for creating a search system
        # Adding a search bar
        search_lbl = tk.Label(self, text="Search By:", font=FONT3)
        search_lbl.place(x=60, y=437, height=30)
        search_lbl.config(bg="Black", fg="White")

        # Adding a Search by combo box
        search_combobox=ttk.Combobox(self, textvariable=self.var_search_by_combobox, font=FONT3, width=16, state="readonly")
        search_combobox["values"] = ("Select", "Student_ID", "First_Name", "Last_Name","Date_of_Birth", "Date_Of_Admission")
        search_combobox.current(0)
        search_combobox.place(x=165, y=437, height=30)

        # Adding an entry field textbox
        search_entry_textbox = ttk.Entry(self, textvariable=self.var_search, width=22, font=FONT3)
        search_entry_textbox.place(x=363, y=437, height=30)
        # Adding a Search button
        search_button = ttk.Button(self, text="Search",cursor="hand2")
        search_button.place(x=610, y=420, width=130, height=60)
        
        # Adding a Show All button
        show_all_button = ttk.Button(self, text="Show All", cursor="hand2")
        show_all_button.place(x=760, y=420, width=130, height=60)
        #============================================================================================================================================================================================================
        # Creating a Table Frame which will contain the table showing all the student profiles
        Table_Frame= ttk.Frame(self, relief=RIDGE)
        Table_Frame.place(x=5, y=500, width=1270, height=270)

        # Creating a scroll bar for both the x axxis and the y axis
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        
        # Creating a table structure with the heading variables being passed in the column brackets
        self.student_table = ttk.Treeview(Table_Frame, column=("std_ID", "first_name", "last_name", "email", "date_of_admission", "date_of_birth", "father_name","father_email", "mother_name","mother_email"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        # Placing the scroll bar on the x axis and the y axis
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Confuguring the scroll bars so that they work whenever the user uses the scroll bars
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Assigning the table headings to the heading variables created in the previous lines
        self.student_table.heading("std_ID", text="Student ID")
        self.student_table.heading("first_name", text="First Name")
        self.student_table.heading("last_name", text="Last Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("date_of_admission", text="Date Of Admission")
        self.student_table.heading("date_of_birth", text="Date Of Birth")
        self.student_table.heading("father_name", text="Father's Name")
        self.student_table.heading("father_email", text="Father Email")
        self.student_table.heading("mother_name", text="Mother's Name")
        self.student_table.heading("mother_email", text="Mother Email")
        self.student_table["show"] = "headings"

        # Setting the width of the columns
        self.student_table.column("std_ID", width=68)
        self.student_table.column("first_name", width=130)
        self.student_table.column("last_name", width=130)
        self.student_table.column("email", width=130)
        self.student_table.column("date_of_admission", width=120)
        self.student_table.column("date_of_birth", width=120)
        self.student_table.column("father_name", width=130)
        self.student_table.column("father_email", width=150)
        self.student_table.column("mother_name", width=130)
        self.student_table.column("mother_email", width=100)

        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.student_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        # UI Design for the search system completed
        # --------------------------------------------------------------------------- #
        # Buttons which will aid in updating the student
        # Update button
        update_button = ttk.Button(self, text="Update Student", style="big.TButton", command=self.update_student_button)
        update_button.place(x=910, y=120, width=350, height=90)

        # Adding a capture face button below the label
        capture_face_button = ttk.Button(self, text="Capture Face Student", style="big.TButton", command=self.capture_face_button)
        capture_face_button.place(x=910, y=230, width=350, height=90)

        # Clear All Data button
        clear_all_button = ttk.Button(self, text="Clear All Fields", style="big.TButton", command=self.clear_all_button)
        clear_all_button.place(x=910, y=340, width=350, height=90)

        # Adding the back button
        back_button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(IREG_Main_Menu_Page))
        back_button.place(x=5,y=5)
    #                                                            END OF UI DESIGN
    #===========================================================================================================================================#
    #############################################################################################################################################
    #===========================================================================================================================================#
    #                                                      BUTTON IMPLEMENTATION FUNCTIONS
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Update button implementation
    def update_student_button(self):
        if self.var_student_ID[0]=="" or self.var_student_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_admission.get()=="" or self.var_date_of_birth.get()=="" or self.var_father_name.get()=="" or self.var_father_email.get()=="" or self.var_mother_name.get()=="" or self.var_mother_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self)
        else:
            try:
                update = messagebox.askyesno("Update Student Account", "Do you want to update student details?", parent=self)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
                    my_cursor = conn.cursor()
                    my_cursor.execute("""UPDATE tbl_student 
                    SET First_Name=%s, Last_Name=%s, Email=%s, date_of_admission=%s, Date_Of_Birth=%s, 
                    Father_Name=%s, Father_Email=%s, Mother_Name=%s, Mother_Email=%s WHERE Student_ID=%s""",
                    (self.var_first_name.get(), self.var_last_name.get(), self.var_student_email.get(), 
                     self.var_date_of_admission.get(), self.var_date_of_birth.get(),
                     self.var_father_name.get(), self.var_father_email.get(),
                     self.var_mother_name.get(), self.var_mother_email.get(),
                     self.var_student_ID[0]))

                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student details have been succesfully updated.", parent=self)
                conn.commit()
                self.fetch_data()
                conn.close()
                self.clear_all_button()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self)
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Funtion to fetch the date in the table frame created
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM tbl_student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Get Cursor
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_student_ID=(data[0]),
        self.new_studentID_lbl.config(text=self.var_student_ID)
        self.var_first_name.set(data[1]),
        self.var_last_name.set(data[2]),
        self.var_student_email.set(data[3]),
        self.var_date_of_admission.set(data[4]),
        self.var_date_of_birth.set(data[5]),
        self.var_father_name.set(data[6]),
        self.var_father_email.set(data[7]),
        self.var_mother_name.set(data[8]),
        self.var_mother_email.set(data[9])
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Clear All Fields button Implementation
    def clear_all_button(self):
        self.var_student_ID = (""),
        self.var_student_email.set(""),
        self.var_first_name.set(""),
        self.var_last_name.set(""),
        self.var_date_of_admission.set(""),
        self.var_date_of_birth.set(""),
        self.var_father_name.set(""),
        self.var_father_email.set(""),
        self.var_mother_name.set(""),
        self.var_mother_email.set("")
    # -------------------------------------------------------------------------------------------------------------------------------------------#
    # Capture Student Face button implementation
    def capture_face_button(self):
        # Validation that all fields are filled up
        if self.var_student_ID=="" or self.var_student_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_admission.get()=="" or self.var_date_of_birth.get()=="" or self.var_father_name.get()=="" or self.var_father_email.get()=="" or self.var_mother_name.get()=="" or self.var_mother_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self)
        else:
            # Added a try box to get rid of any exceptions which might arise
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
                my_cursor = conn.cursor()
                # Selected all the data from the database and stored it in the variable myresult
                my_cursor.execute("SELECT * FROM tbl_student")
                myresult = my_cursor.fetchall()
                # We match the images to an id
                id=0
                # Therfore, we create a loop to manage the IDs
                for x in myresult:
                    id += 1
                my_cursor.execute("UPDATE tbl_student SET First_Name=%s, Last_Name=%s, Email=%s, date_of_admission=%s, Date_Of_Birth=%s, Father_Name=%s, Father_Email=%s, Mother_Name=%s, Mother_Email=%s WHERE Student_ID=%s",(
                                                                                                         self.var_first_name.get(),
                                                                                                         self.var_last_name.get(),
                                                                                                         self.var_student_email.get(),
                                                                                                         self.var_date_of_admission.get(),
                                                                                                         self.var_date_of_birth.get(),
                                                                                                         self.var_father_name.get(),
                                                                                                         self.var_father_email.get(),
                                                                                                         self.var_mother_name.get(),
                                                                                                         self.var_mother_email.get(),
                                                                                                         self.var_student_ID==id+1
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.clear_all_button()
                conn.close()
                # =========== Load predifined data on face frontals from Open CV. Loading Haarcascade frontal image default =========== #
                # ideally, we need to give the path of the location of teh haarcascasde file. But in this case, the haarcascade has been 
                # copied to the code folder and therefore we do not necessaily need to provide a path for it.
                face_classifier = cv2.CascadeClassifier("C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/haarcascade_frontalface_default.xml") 
                # ----------------------------------------------------------------------------------------------------------------------- #
                # Supplementary functions
                # Cropping the video footage and focussing specifially on the face
                def face_cropped(img):
                    # Converting a Blue Green Red BGR image to grayscale form
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces =  face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scalinng Factor = 1.3
                    # Minimum Neighbour = 6
                
                    for(x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
               
            # ---------------------------------------------------------------------------------------------------------------------------- #



                # The 0 here is an extension for the camera footage. If I want it to read a video file, I need to add in the video 
                # location. By this line, we are accessing the camera footage
                cap = cv2.VideoCapture(0)

                img_id = 0
                while True:
                    ret, face_Frame = cap.read()
                    if face_cropped(face_Frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(face_Frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/Data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Capture Face", face)

                    if cv2.waitKey(1)==13 or int(img_id==100):
                        break
                cap.release()
                cv2.destroyWindow("Capture Face")
                self.train_data_button()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self)
    # ------------------------------------------------------------------------------------------------------------------------ #
    # Train the classifier using these face captures
    def train_data_button(self):
        data_dir = ("C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/Data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for face in path:
            img = Image.open(face).convert("L") # Grey Scale Image
            imageNP = np.array(img, 'uint8') # Converting gray scale image to an array of data type uint
            face_ID = int(os.path.split(face)[1].split(".")[1])

            faces.append(imageNP)
            ids.append(face_ID)
            cv2.imshow("Training", imageNP)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        # Train Classifier and Save
        classifier = cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces, ids)
        classifier.write("C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/Trained_Faces.xml")
        cv2.destroyWindow("Training")
        messagebox.showinfo("Train Face Data", "Datasets have been trained using the student faces")
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #
class Delete_Student_Details(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        Student_Account_management_Lbl = tk.Label(self, text="Student Account Management", font=FONT1)
        Student_Account_management_Lbl.place(x=205, y=5, width=870, height=75)
        Student_Account_management_Lbl.config(bg="Black", fg="White")

        style = ttk.Style()
        style.configure("big.TButton", font=('Calibri', 12), bg="Black", fg="White")

        # Variables related to the students
        self.var_student_ID = StringVar()
        self.var_student_email = StringVar()
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_date_of_admission = StringVar()
        self.var_date_of_birth = StringVar()
        
        # Variables related to the father
        self.var_father_name = StringVar()
        self.var_father_email = StringVar()

        # Variables related to the mother
        self.var_mother_name = StringVar()
        self.var_mother_email = StringVar()

        # Search Variables
        self.var_search_by_combobox = StringVar()
        self.var_search = StringVar()
    ############################################################################################################################################
    #==========================================================================================================================================#
    #                                                                UI DESIGN
    # =========================================================================================================================================#
    # Adding in the student related text boxes and labels
        # Creating a new Student ID
        self.var_student_ID = ""
        self.var_student_email = ""
        self.var_first_name = ""
        self.var_last_name = ""
        self.var_date_of_admission = ""
        self.var_date_of_birth = ""
        self.var_father_name = ""
        self.var_father_email = ""
        self.var_mother_name = ""
        self.var_mother_email = ""

        # Adding a student id label and textbox
        studentID_lbl = Label(self, text="Student ID: ", font=FONT3)
        studentID_lbl.place(x=70, y=105)
        studentID_lbl.config(bg="Black", fg="White")

        self.new_studentID_lbl = Label(self, text=self.var_student_ID, font=FONT3)
        self.new_studentID_lbl.grid(row=0, column=1, padx=5, pady=(105,18), sticky=W)
        self.new_studentID_lbl.config(bg="Black", fg="White")

        # Adding a Student Email label and textbox
        student_email_lbl = Label(self, text="Student Email: ", font=FONT3)
        student_email_lbl.grid(row=0, column=2, padx=(255,5), pady=(105, 18), sticky=E)
        student_email_lbl.config(bg="Black", fg="White")

        self.retrieved_student_email_lbl = Label(self, text=self.var_student_email, font=FONT3)
        self.retrieved_student_email_lbl.grid(row=0, column=3, padx=5, pady=(105,18), sticky=W)
        self.retrieved_student_email_lbl.config(bg="Black", fg="White")

        # Adding a first name label and textbox
        first_name_lbl = Label(self, text="First Name: ", font=FONT3)
        first_name_lbl.grid(row=2, column=0, padx=5, pady=18, sticky=E)
        first_name_lbl.config(bg="Black", fg="White")

        self.retrieved_first_name_lbl = Label(self, text=self.var_first_name, font=FONT3)
        self.retrieved_first_name_lbl.grid(row=2, column=1, padx=5, pady=18, sticky=W)
        self.retrieved_first_name_lbl.config(bg="Black", fg="White")

        # Adding a last label and textbox
        last_name_lbl = Label(self, text="Last Name: ", font=FONT3)
        last_name_lbl.grid(row=2, column=2, padx=5, pady=18, sticky=E)
        last_name_lbl.config(bg="Black", fg="White")

        self.retrieved_last_name_lbl = Label(self, text=self.var_last_name, font=FONT3)
        self.retrieved_last_name_lbl.grid(row=2, column=3, padx=5, pady=18, sticky=W)
        self.retrieved_last_name_lbl.config(bg="Black", fg="White")

        # Adding a Student Date Of Admission label and textbox
        date_of_admission_lbl = Label(self, text="Date Of Admission: ", font=FONT3)
        date_of_admission_lbl.grid(row=3, column=0, padx=5, pady=18, sticky=E)
        date_of_admission_lbl.config(bg="Black", fg="White")
                                                                              
        self.retrieved_date_of_admission_lbl = Label(self, text=self.var_date_of_admission, font=FONT3)
        self.retrieved_date_of_admission_lbl.grid(row=3, column=1, padx=5, pady=18, sticky=W)
        self.retrieved_date_of_admission_lbl.config(bg="Black", fg="White")

        # Adding a date of birth label and textbox
        date_of_birth_lbl = Label(self, text="Date of Birth: ", font=FONT3)
        date_of_birth_lbl.grid(row=3, column=2, padx=5, pady=18, sticky=E)
        date_of_birth_lbl.config(bg="Black", fg="White")

        self.retrieved_date_of_birth_lbl = Label(self, text=self.var_date_of_birth, font=FONT3)
        self.retrieved_date_of_birth_lbl.grid(row=3, column=3, padx=5, pady=18, sticky=W)
        self.retrieved_date_of_birth_lbl.config(bg="Black", fg="White")

        # Father's Information
        # Adding a father first name label and textbox
        father_name_lbl = Label(self, text="Father's Name: ", font=FONT3)
        father_name_lbl.grid(row=4, column=0, padx=4, pady=18, sticky=E)
        father_name_lbl.config(bg="Black", fg="White")

        self.retrieved_father_name_lbl = Label(self, text=self.var_father_name, font=FONT3)
        self.retrieved_father_name_lbl.grid(row=4, column=1, padx=5, pady=18, sticky=W)
        self.retrieved_father_name_lbl.config(bg="Black", fg="White")

        # Adding father's email label and text box
        father_email_lbl = Label(self, text="Father's Email: ", font=FONT3)
        father_email_lbl.grid(row=4, column=2, padx=4, pady=18, sticky=E)
        father_email_lbl.config(bg="Black", fg="White")

        self.retrieved_father_email_lbl = Label(self, text=self.var_father_email, font=FONT3)
        self.retrieved_father_email_lbl.grid(row=4, column=3, padx=5, pady=18, sticky=W)
        self.retrieved_father_email_lbl.config(bg="Black", fg="White")

        # Mother's Information
        # Adding a father first name label and textbox
        mother_name_lbl = Label(self, text="Mother's Name: ", font=FONT3)
        mother_name_lbl.grid(row=5, column=0, padx=4, pady=18, sticky=E)
        mother_name_lbl.config(bg="Black", fg="White")

        self.retrieved_mother_name_lbl = Label(self, text=self.var_mother_name, font=FONT3)
        self.retrieved_mother_name_lbl.grid(row=5, column=1, padx=5, pady=18, sticky=W)
        self.retrieved_mother_name_lbl.config(bg="Black", fg="White")

        # Adding father's email label and text box
        mother_email_lbl = Label(self, text="Mother's Email: ", font=FONT3)
        mother_email_lbl.grid(row=5, column=2, padx=4, pady=18, sticky=E)
        mother_email_lbl.config(bg="Black", fg="White")

        self.retrieved_mother_email_lbl = Label(self, text=self.var_mother_email, font=FONT3)
        self.retrieved_mother_email_lbl.grid(row=5, column=3, padx=5, pady=18, sticky=W)
        self.retrieved_mother_email_lbl.config(bg="Black", fg="White")
        # UI Design for getting the student's and their parents information completed
        # --------------------------------------------------------------------------- #
        # Adding the buttons and textboxes for creating a search system
        # Adding a search bar
        search_lbl = tk.Label(self, text="Search By:", font=FONT3)
        search_lbl.place(x=60, y=437, height=30)
        search_lbl.config(bg="Black", fg="White")

        # Adding a Search by combo box
        search_combobox=ttk.Combobox(self, textvariable=self.var_search_by_combobox, font=FONT3, width=16, state="readonly")
        search_combobox["values"] = ("Select", "Student_ID", "First_Name", "Last_Name","Date_of_Birth", "Date_Of_Admission")
        search_combobox.current(0)
        search_combobox.place(x=165, y=437, height=30)

        # Adding an entry field textbox
        search_entry_textbox = ttk.Entry(self, textvariable=self.var_search, width=22, font=FONT3)
        search_entry_textbox.place(x=363, y=437, height=30)
        # Adding a Search button
        search_button = ttk.Button(self, text="Search",cursor="hand2")
        search_button.place(x=610, y=420, width=130, height=60)
        
        # Adding a Show All button
        show_all_button = ttk.Button(self, text="Show All", cursor="hand2")
        show_all_button.place(x=760, y=420, width=130, height=60)
        #============================================================================================================================================================================================================
        # Creating a Table Frame which will contain the table showing all the student profiles
        Table_Frame= ttk.Frame(self, relief=RIDGE)
        Table_Frame.place(x=5, y=500, width=1270, height=270)

        # Creating a scroll bar for both the x axxis and the y axis
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        
        # Creating a table structure with the heading variables being passed in the column brackets
        self.student_table = ttk.Treeview(Table_Frame, column=("std_ID", "first_name", "last_name", "email", "date_of_admission", "date_of_birth", "father_name","father_email", "mother_name","mother_email"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        # Placing the scroll bar on the x axis and the y axis
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Confuguring the scroll bars so that they work whenever the user uses the scroll bars
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Assigning the table headings to the heading variables created in the previous lines
        self.student_table.heading("std_ID", text="Student ID")
        self.student_table.heading("first_name", text="First Name")
        self.student_table.heading("last_name", text="Last Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("date_of_admission", text="Date Of Admission")
        self.student_table.heading("date_of_birth", text="Date Of Birth")
        self.student_table.heading("father_name", text="Father's Name")
        self.student_table.heading("father_email", text="Father Email")
        self.student_table.heading("mother_name", text="Mother's Name")
        self.student_table.heading("mother_email", text="Mother Email")
        self.student_table["show"] = "headings"

        # Setting the width of the columns
        self.student_table.column("std_ID", width=68)
        self.student_table.column("first_name", width=130)
        self.student_table.column("last_name", width=130)
        self.student_table.column("email", width=130)
        self.student_table.column("date_of_admission", width=120)
        self.student_table.column("date_of_birth", width=120)
        self.student_table.column("father_name", width=130)
        self.student_table.column("father_email", width=150)
        self.student_table.column("mother_name", width=130)
        self.student_table.column("mother_email", width=100)

        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.student_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        # UI Design for the search system completed
        # --------------------------------------------------------------------------- #
        # Buttons which will aid in updating the student
        # Update button
        delete_button = ttk.Button(self, text="Delete Student", style="big.TButton", command=self.delete_student_button)
        delete_button.place(x=910, y=120, width=350, height=90)

        # Clear All Data button
        clear_all_button = ttk.Button(self, text="Clear All Fields", style="big.TButton", command=self.clear_all_button)
        clear_all_button.place(x=910, y=340, width=350, height=90)

        # Adding the back button
        back_button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(IREG_Main_Menu_Page))
        back_button.place(x=5,y=5)
    #                                                            END OF UI DESIGN
    #===========================================================================================================================================#
    #############################################################################################################################################
    #===========================================================================================================================================#
    #                                                      BUTTON IMPLEMENTATION FUNCTIONS
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Delete Button Implementation
    def delete_student_button(self):
        if self.var_student_ID=="":
            messagebox.showerror("Error", "Student ID required.", parent=self)
        else:
            try:
                delete = messagebox.askyesno("Delete Student Account", "Do you want to delete student account?", parent=self)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
                    my_cursor = conn.cursor()
                    my_cursor.execute("DELETE FROM tbl_student WHERE Student_ID=%s",(self.var_student_ID,))
                    deleted.append(int(self.var_student_ID))
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                self.clear_all_button()
                messagebox.showinfo("Delete Student Account", "Student account has been succesfully deleted.", parent=self)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self)
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Funtion to fetch the date in the table frame created
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM tbl_student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Get Cursor
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_student_ID = data[0]
        self.var_first_name = data[1]
        self.var_last_name = data[2]
        self.var_student_email = data[3]
        self.var_date_of_admission = data[4]
        self.var_date_of_birth = data[5]
        self.var_father_name = data[6]
        self.var_father_email = data[7]
        self.var_mother_name = data[8]
        self.var_mother_email = data[9]

        self.retrieved_student_email_lbl.config(text=self.var_student_ID)
        self.retrieved_student_email_lbl.config(text=self.var_student_email)
        self.retrieved_first_name_lbl.config(text=self.var_first_name)
        self.retrieved_last_name_lbl.config(text=self.var_last_name)
        self.retrieved_date_of_admission_lbl.config(text=self.var_date_of_admission)
        self.retrieved_date_of_birth_lbl.config(text=self.var_date_of_birth)
        self.retrieved_father_name_lbl.config(text=self.var_father_name)
        self.retrieved_father_email_lbl.config(text=self.var_father_email)
        self.retrieved_mother_name_lbl.config(text=self.var_mother_name)
        self.retrieved_mother_email_lbl.config(text=self.var_mother_email)
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Clear All Fields button Implementation
    def clear_all_button(self):
        self.var_student_ID = "",
        self.var_student_email = "",
        self.var_first_name = "",
        self.var_last_name = "",
        self.var_date_of_admission = "",
        self.var_date_of_birth = "",
        self.var_father_name = "",
        self.var_father_email = "",
        self.var_mother_name = "",
        self.var_mother_email = ""
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #
class Settings_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        Settings_Lbl = tk.Label(self, text="Settings", font=FONT1)
        Settings_Lbl.place(x=205, y=5, width=870, height=75)
        Settings_Lbl.config(bg="Black", fg="White")

        # Adding the View Attendance
        train_data_Button =  ttk.Button(self, text="Train Data", command= lambda: Add_New_Student_Details_Page.train_data_button(self), style="big.TButton")
        train_data_Button.place(x=440, y=240, width=400, height=50)

        # Adding the Account Management Button
        student_faces_Button = ttk.Button(self, text="Student Faces", command= self.student_faces_button, style="big.TButton")
        student_faces_Button.place(x=440, y=300, width=400, height=50)

        # Adding the back button
        back_button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(IREG_Main_Menu_Page))
        back_button.place(x=5,y=5)
    #                                                            END OF UI DESIGN
    #===========================================================================================================================================#
    #############################################################################################################################################
    #===========================================================================================================================================#
    #                                                      BUTTON IMPLEMENTATION FUNCTIONS
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Function for adding in the student faces to a file on the computer
    def student_faces_button(sellf):
        os.startfile("C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/Data")
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #

app = IREG()
app.mainloop()