# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import numpy as np
import cv2
import mysql.connector
from datetime import datetime

class Student_Account_Management:
    def __init__(self, root):
        self.root = root
        # Setting the window height and width along with where the window should open on the screen.
        self.root.geometry("1090x645+75+70")
        self.root.resizable(width=False, height=False)
        self.root.title("IREG: Student Account Management")

        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="Light Yellow", relief = RIDGE)
        mainFrame.place(x=2, y=2, width=1086, height=640)

        # Account Management Label Frame
        Student_Account_Management_lbl= Label(mainFrame, text="Student Account Management", font=("Segoe UI Variable", 45, "bold"), bg="Light Yellow", fg="Black")
        Student_Account_Management_lbl.place(x=108, y=0, width=870, height=75)

# ========================================================================================================================================================
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
# ========================================================================================================================================================
        # Student Information frame: This will contain all the information
        Student_Information_Frame= LabelFrame(mainFrame, bd=2, bg="Light Yellow", relief=RIDGE, text="Student Details", font=("Segoe UI Variable", 12, "bold"),)
        Student_Information_Frame.place(x=5, y=72, width=793, height=135)
# ========================================================================================================================================================
        # Adding in the student related text boxes and labels
        # Adding a student id label and textbox
        studentID_label = Label(Student_Information_Frame, text = "Student ID: ", font=("Segoe UI Variable", 12, "bold"), bg = "Light Yellow")
        studentID_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        studentID_textbox = ttk.Entry(Student_Information_Frame, width=25, textvariable=self.var_student_ID, font=("Segoe UI Variable", 12, "bold"),)
        studentID_textbox.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Adding a Student Email label and textbox
        student_email_label = Label(Student_Information_Frame, text = "Student Email: ", font=("Segoe UI Variable", 12, "bold"), bg = "Light Yellow")
        student_email_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        
        student_email_textbox = ttk.Entry(Student_Information_Frame, width=25, textvariable=self.var_student_email, font=("Segoe UI Variable", 12, "bold"),)
        student_email_textbox.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Adding a first name label and textbox
        first_name_label = Label(Student_Information_Frame, text = "First Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "Light Yellow")
        first_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        first_name_textbox = ttk.Entry(Student_Information_Frame, width=25, textvariable=self.var_first_name, font=("Segoe UI Variable", 12, "bold"),)
        first_name_textbox.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # Adding a last label and textbox
        last_name_label = Label(Student_Information_Frame, text = "Last Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "Light Yellow")
        last_name_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        
        last_name_textbox = ttk.Entry(Student_Information_Frame, width=25, textvariable=self.var_last_name, font=("Segoe UI Variable", 12, "bold"),)
        last_name_textbox.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Adding a Student Date Of Admission label and textbox
        date_of_admission_label = Label(Student_Information_Frame, text = "Date Of Admission: ", font=("Segoe UI Variable", 12, "bold"), bg = "Light Yellow")
        date_of_admission_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        
        date_of_admission_textbox = ttk.Entry(Student_Information_Frame,width=25, textvariable=self.var_date_of_admission, font=("Segoe UI Variable", 12, "bold"),)
        date_of_admission_textbox.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Adding a date of birth label and textbox
        date_of_birth_label = Label(Student_Information_Frame, text = "Date of Birth: ", font=("Segoe UI Variable", 12, "bold"), bg = "Light Yellow")
        date_of_birth_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        date_of_birth_textbox = ttk.Entry(Student_Information_Frame,width=25, textvariable=self.var_date_of_birth, font=("Segoe UI Variable", 12, "bold"),)
        date_of_birth_textbox.grid(row=3, column=3, padx=5, pady=5, sticky=W)
# ========================================================================================================================================================
        # Parent Information Frame: This frame have the fields asking information for the student's parents
        Parent_Information_Frame= LabelFrame(mainFrame, bd=2, bg="Light Yellow", relief=RIDGE, text="Parent Details", font=("Segoe UI Variable", 12, "bold"),)
        Parent_Information_Frame.place(x=5, y=212, width=793, height=163)
# ========================================================================================================================================================
        # Adding a subframe for fathers details
        Father_Information_Frame= LabelFrame(Parent_Information_Frame, bd=2, bg="Light Yellow", relief=RIDGE, text="Father's Details", font=("Segoe UI Variable", 12, "bold"),)
        Father_Information_Frame.place(x=10, y=4, width=360, height=130)
# ========================================================================================================================================================
        # Adding the information labels and text boxes
        # Adding father's first name label and text box
        father_first_name_label = Label(Father_Information_Frame, text = "First Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "Light Yellow")
        father_first_name_label.grid(row=0, column=0, padx=4, pady=5, sticky=W)

        father_first_name_textbox = ttk.Entry(Father_Information_Frame, width=25, textvariable=self.var_father_first_name, font=("Segoe UI Variable", 12, "bold"),)
        father_first_name_textbox.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Adding father's last name label and text box
        father_last_name_label = Label(Father_Information_Frame, text = "Last Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "Light Yellow")
        father_last_name_label.grid(row=1, column=0, padx=4, pady=5, sticky=W)

        father_last_name_textbox = ttk.Entry(Father_Information_Frame, width=25, textvariable=self.var_father_last_name, font=("Segoe UI Variable", 12, "bold"),)
        father_last_name_textbox.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Adding father's email label and text box
        father_email_label = Label(Father_Information_Frame, text = "Email: ", font=("Segoe UI Variable", 12, "bold"), bg = "Light Yellow")
        father_email_label.grid(row=2, column=0, padx=4, pady=5, sticky=W)

        father_email_textbox = ttk.Entry(Father_Information_Frame, width=25, textvariable=self.var_father_email, font=("Segoe UI Variable", 12, "bold"),)
        father_email_textbox.grid(row=2, column=1, padx=5, pady=5, sticky=W)
# ========================================================================================================================================================
        # Adding a subframe for mothers details
        Mother_Information_Frame= LabelFrame(Parent_Information_Frame, bd=2, bg="Light Yellow", relief=RIDGE, text="Mother's Details", font=("Segoe UI Variable", 12, "bold"),)
        Mother_Information_Frame.place(x=410, y=4, width=360, height=130)
# ========================================================================================================================================================
        # Adding the information labels and text boxes
        # Adding mother's first name label and text box
        mother_first_name_label = Label(Mother_Information_Frame, text = "First Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "Light Yellow")
        mother_first_name_label.grid(row=0, column=0, padx=4, pady=5, sticky=W)

        mother_first_name_textbox = ttk.Entry(Mother_Information_Frame, width=25, textvariable=self.var_mother_first_name, font=("Segoe UI Variable", 12, "bold"),)
        mother_first_name_textbox.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Adding mother's last name label and text box
        mother_last_name_label = Label(Mother_Information_Frame, text = "Last Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "Light Yellow")
        mother_last_name_label.grid(row=1, column=0, padx=4, pady=5, sticky=W)

        mother_last_name_textbox = ttk.Entry(Mother_Information_Frame, width=25, textvariable=self.var_mother_last_name, font=("Segoe UI Variable", 12, "bold"),)
        mother_last_name_textbox.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Adding mother's email label and text box
        mother_email_label = Label(Mother_Information_Frame, text = "Email: ", font=("Segoe UI Variable", 12, "bold"), bg = "Light Yellow")
        mother_email_label.grid(row=2, column=0, padx=4, pady=5, sticky=W)

        mother_email_textbox = ttk.Entry(Mother_Information_Frame, width=25, textvariable=self.var_mother_email, font=("Segoe UI Variable", 12, "bold"),)
        mother_email_textbox.grid(row=2, column=1, padx=5, pady=5, sticky=W)
# ========================================================================================================================================================
        # Adding a search frame which will have all the functions required to conduct a search
        Search_Frame= LabelFrame(mainFrame, bd=2, bg="Light Yellow", relief=RIDGE, text="Search System", font=("Segoe UI Variable", 12, "bold"),)
        Search_Frame.place(x=5, y=380, width=1070, height=250)

        # Adding a search bar
        search_label = Label(Search_Frame, text="Search By:", font=("Segoe UI Variable", 12, "bold"), bg="Light Yellow", fg="Black")
        search_label.grid(row=0, column=0, padx=15, pady=5, sticky=W)

        # Adding a Search by combo box
        search_combobox=ttk.Combobox(Search_Frame, textvariable=self.var_search_by_combobox, font=("Segoe UI Variable", 12, "bold"), width=17, state="readonly")
        search_combobox["values"] = ("Select", "Student_ID", "First_Name", "Last_Name","Date_of_Birth", "Date_Of_Admission")
        search_combobox.current(0)
        search_combobox.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Adding an entry field textbox
        search_entry_textbox = ttk.Entry(Search_Frame, textvariable=self.var_search, width=26, font=("Segoe UI Variable", 12, "bold"))
        search_entry_textbox.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        # Adding a Search button
        search_button = Button(Search_Frame, command=self.search_button, width=23, text="Search", cursor="hand2", font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="Light Yellow")
        search_button.grid(row=0, column=3,padx=5, pady=5, sticky=W)
        
        # Adding a Show All button
        show_all_button = Button(Search_Frame, command=self.fetch_data, width=23, text="Show All", cursor="hand2", font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="Light Yellow")
        show_all_button.grid(row=0, column=4, padx=5, pady=5, sticky=W)
#============================================================================================================================================================================================================
        # Table Frame
        Table_Frame= Frame(Search_Frame, bd=2, bg="Light Yellow", relief=RIDGE)
        Table_Frame.place(x=0, y=45, width=1066, height=183)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(Table_Frame, column=("std_ID", "first_name", "last_name", "email", "date_of_admission", "date_of_birth", "father_first_name", "father_last_name", "father_email", "mother_first_name", "mother_last_name", "mother_email"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("std_ID", text="Student ID")
        self.student_table.heading("first_name", text="First Name")
        self.student_table.heading("last_name", text="Last Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("date_of_admission", text="Date Of Admission")
        self.student_table.heading("date_of_birth", text="Date Of Birth")
        self.student_table.heading("father_first_name", text="Father's First Name")
        self.student_table.heading("father_last_name", text="Father's Last Name")
        self.student_table.heading("father_email", text="Father Email")
        self.student_table.heading("mother_first_name", text="Mother's First Name")
        self.student_table.heading("mother_last_name", text="Mother's Last Name")
        self.student_table.heading("mother_email", text="Mother Email")
        self.student_table["show"] = "headings"
        
        self.student_table.column("std_ID", width=68)
        self.student_table.column("first_name", width=130)
        self.student_table.column("last_name", width=130)
        self.student_table.column("email", width=130)
        self.student_table.column("date_of_admission", width=120)
        self.student_table.column("date_of_birth", width=120)
        self.student_table.column("father_first_name", width=130) 
        self.student_table.column("father_last_name", width=130)
        self.student_table.column("father_email", width=150)
        self.student_table.column("mother_first_name", width=130)
        self.student_table.column("mother_last_name", width=130)
        self.student_table.column("mother_email", width=100)

        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.student_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

# ==========================================================================================================================================#
        # Adding a button frame which will have the save, update and delete button
        Button_Frame = Frame(mainFrame, bd=2, relief=RIDGE, bg="Light Yellow")
        Button_Frame.place(x=803, y=79, width=273, height=304)

        # Add Student button
        add_student_button = Button(Button_Frame, width=25, height=2, command=self.add_student_button, text="Add Student", font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="Light Yellow")
        add_student_button.grid(row=0, padx=5, pady=4)
        
        # Update button
        update_button = Button(Button_Frame, width=25, height=2, command=self.update_student_button, text="Update Student Details", font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="Light Yellow")
        update_button.grid(row=1, padx=5, pady=4)
        
        # Delete button
        delete_button = Button(Button_Frame, width=25, height=2, command= self.delete_student_button, text="Delete Student", font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="Light Yellow")
        delete_button.grid(row=2, padx=5, pady=4)

        # Adding a capture face button below the label
        capture_face_button = Button(Button_Frame, width=25, height=2, cursor="hand2",command=self.capture_face_button, text="Capture Face", font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="Light Yellow")
        capture_face_button.grid(row=3, padx=5, pady=4)

        # Clear All Data button
        clear_all_button = Button(Button_Frame, width=25, height=2, command= self.clear_all_button, text="Clear All Fields", font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="Light Yellow")
        clear_all_button.grid(row=4, padx=5, pady=4)
#                                                            END OF UI DESIGN
#===========================================================================================================================================#
#############################################################################################################################################
#===========================================================================================================================================#
#                                                      BUTTON IMPLEMENTATION FUNCTIONS
# ------------------------------------------------------------------------------------------------------------------------------------------#
    # Function for adding in the data when the user clicks on the add student button
    def add_student_button(self):
        if self.var_student_ID.get()=="" or self.var_student_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_admission.get()=="" or self.var_date_of_birth.get()=="" or self.var_father_first_name.get()=="" or self.var_father_last_name.get()=="" or self.var_father_email.get()=="" or self.var_mother_first_name.get()=="" or self.var_mother_last_name.get()=="" or self.var_mother_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO tbl_student VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                                                                                         self.var_student_ID.get(),
                                                                                                         self.var_first_name.get(),
                                                                                                         self.var_last_name.get(),
                                                                                                         self.var_student_email.get(),
                                                                                                         self.var_date_of_admission.get(),
                                                                                                         self.var_date_of_birth.get(),
                                                                                                         self.var_father_first_name.get(),
                                                                                                         self.var_father_last_name.get(),
                                                                                                         self.var_father_email.get(),
                                                                                                         self.var_mother_first_name.get(),
                                                                                                         self.var_mother_last_name.get(),
                                                                                                         self.var_mother_email.get()
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                self.clear_all_button()
                messagebox.showinfo("Success", "Student details have been added succesfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

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

    # Get Cursor
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_student_ID.set(data[0]),
        self.var_first_name.set(data[1]),
        self.var_last_name.set(data[2]),
        self.var_student_email.set(data[3]),
        self.var_date_of_admission.set(data[4]),
        self.var_date_of_birth.set(data[5]),
        self.var_father_first_name.set(data[6]),
        self.var_father_last_name.set(data[7]),
        self.var_father_email.set(data[8]),
        self.var_mother_first_name.set(data[9]),
        self.var_mother_last_name.set(data[10]),
        self.var_mother_email.set(data[11])
# ------------------------------------------------------------------------------------------------------------------------------------------#
    # Update button implementation
    def update_student_button(self):
        if self.var_student_ID.get()=="" or self.var_student_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_admission.get()=="" or self.var_date_of_birth.get()=="" or self.var_father_first_name.get()=="" or self.var_father_last_name.get()=="" or self.var_father_email.get()=="" or self.var_mother_first_name.get()=="" or self.var_mother_last_name.get()=="" or self.var_mother_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update Student Account", "Do you want to update student details?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE tbl_student SET First_Name=%s, Last_Name=%s, Email=%s, date_of_admission=%s, Date_Of_Birth=%s, Father_First_Name=%s, Father_Last_Name=%s, Father_Email=%s, Mother_First_Name=%s, Mother_Last_Name=%s, Mother_Email=%s WHERE Student_ID=%s",(
                                                                                                         self.var_first_name.get(),
                                                                                                         self.var_last_name.get(),
                                                                                                         self.var_student_email.get(),
                                                                                                         self.var_date_of_admission.get(),
                                                                                                         self.var_date_of_birth.get(),
                                                                                                         self.var_father_first_name.get(),
                                                                                                         self.var_father_last_name.get(),
                                                                                                         self.var_father_email.get(),
                                                                                                         self.var_mother_first_name.get(),
                                                                                                         self.var_mother_last_name.get(),
                                                                                                         self.var_mother_email.get(),
                                                                                                         self.var_student_ID.get()
                                                                                                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student details have been succesfully updated.", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                self.clear_all_button()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", paren=self.root)
# ------------------------------------------------------------------------------------------------------------------------------------------#
    # Delete Button Implementation
    def delete_student_button(self):
        if self.var_student_ID.get()=="":
            messagebox.showerror("Error", "Student ID required.", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Student Account", "Do you want to delete student account?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
                    my_cursor = conn.cursor()
                    # my_cursor.execute("DELETE FROM tbl_student WHERE Student_ID=%s", (self.var_student_ID.get()))
                    sql_query = "DELETE FROM tbl_student WHERE Student_ID=%s"
                    values = (self.var_student_ID.get(),)
                    my_cursor.execute(sql_query, values)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                self.clear_all_button()
                messagebox.showinfo("Delete Student Account", "Student account has been succesfully deleted.", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
# ------------------------------------------------------------------------------------------------------------------------------------------#
    # Clear All Fields button Implementation
    def clear_all_button(self):
        self.var_student_ID.set(""),
        self.var_student_email.set(""),
        self.var_first_name.set(""),
        self.var_last_name.set(""),
        self.var_date_of_admission.set(""),
        self.var_date_of_birth.set(""),
        self.var_father_first_name.set(""),
        self.var_father_last_name.set(""),
        self.var_father_email.set(""),
        self.var_mother_first_name.set(""),
        self.var_mother_last_name.set(""),
        self.var_mother_email.set("")
# -------------------------------------------------------------------------------------------------------------------------------------------#
    def capture_face_button(self):
        # Validation that all fields are filled up
        if self.var_student_ID.get()=="" or self.var_student_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_admission.get()=="" or self.var_date_of_birth.get()=="" or self.var_father_first_name.get()=="" or self.var_father_last_name.get()=="" or self.var_father_email.get()=="" or self.var_mother_first_name.get()=="" or self.var_mother_last_name.get()=="" or self.var_mother_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            # Added a try box to get rid pf any exceptions which might arise
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
                my_cursor.execute("UPDATE tbl_student SET First_Name=%s, Last_Name=%s, Email=%s, date_of_admission=%s, Date_Of_Birth=%s, Father_First_Name=%s, Father_Last_Name=%s, Father_Email=%s, Mother_First_Name=%s, Mother_Last_Name=%s, Mother_Email=%s WHERE Student_ID=%s",(
                                                                                                         self.var_first_name.get(),
                                                                                                         self.var_last_name.get(),
                                                                                                         self.var_student_email.get(),
                                                                                                         self.var_date_of_admission.get(),
                                                                                                         self.var_date_of_birth.get(),
                                                                                                         self.var_father_first_name.get(),
                                                                                                         self.var_father_last_name.get(),
                                                                                                         self.var_father_email.get(),
                                                                                                         self.var_mother_first_name.get(),
                                                                                                         self.var_mother_last_name.get(),
                                                                                                         self.var_mother_email.get(),
                                                                                                         self.var_student_ID.get()==id+1
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
                messagebox.showinfo("Capture Face", "Succesfully captured student face.")
                self.train_data_button()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
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
        messagebox.showinfo("Training Success", "Datasets have been trained successfully.")
    # ------------------------------------------------------------------------------------------------------------------------ #
    # Search button implementation
    def search_button(self):
        if self.var_search_by_combobox.get()=="Select" or self.var_search.get()=="":
            if self.var_search_by_combobox.get()=="Select":
                messagebox.showerror("Error", "Please select an option to search by")
            else:
                messagebox.showerror("Error", "Please enter the data you want to search for in the search textbox")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM tbl_student WHERE " + str(self.var_search_by_combobox.get()) + " LIKE '%" + str(self.var_search.get()) + " %'")
                data = my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

# ---------------------------------------------------------------------------------------------------------------------------- #

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Student_Account_Management(root)
    root.mainloop()