# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import numpy as np
import cv2
import mysql.connector
from datetime import datetime

class Update_Student_Profile:
    # This is the constructor of the class IREG_Main_Menu
    def __init__(self, root):
        self.root = root
        # Setting the dimensions of the window and the point where the window is displayed from
        self.root.geometry("1280x760+0+0")
        # Setting the property of resizing the window to false
        self.root.resizable(width=False, height=False)
        self.root.title("IREG")

        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="White", relief = SOLID)
        mainFrame.place(x=2, y=2, width=1276, height=755) # Specifying the coordinates along with the dimensions of the frame

        # Label Frame
        Update_Student_Profile_lbl= Label(mainFrame, text="Update Student Profile", font=("Segoe UI Variable", 45, "bold"), bg="White", fg="Black")
        Update_Student_Profile_lbl.place(x=1, y=5, width=1270, height=75) # Specifying the coordinates along with the dimensions of the frame

        # Variables related to the students
        self.var_student_ID = IntVar()
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_student_email = StringVar()
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

        # Button Frame
        Button_Frame= Frame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Button_Frame.place(x=885, y=460, width=380, height=290) # Specifying the coordinates along with the dimensions of the frame

        # ======================================================================================================================================== #
        # Student Information frame: This frame will contain all the fields asking for information related to the student
        Student_Information_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Student Details", font=("Segoe UI Variable", 12, "bold"))
        Student_Information_Frame.place(x=5, y=85, width=826, height=200)
        # =================================================================== #
        # Adding in the student related text boxes and labels
        # Adding a student id label and textbox
        studentID_label = Label(Student_Information_Frame, text = "Student ID: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        studentID_label.grid(row=0, column=0, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label

        #studentID_textbox = ttk.Entry(Student_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"),)
        #studentID_textbox.grid(row=0, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        self.var_student_ID = None
        self.new_studentID_lbl = Label(Student_Information_Frame, text=self.var_student_ID, font=("Segoe UI Variable", 12, "bold"), bg = "White")
        self.new_studentID_lbl.grid(row=0, column=1, padx=(15,5), pady=15, sticky=W)

        # Adding a Student Email label and textbox
        student_email_label = Label(Student_Information_Frame, text = "Student Email: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        student_email_label.grid(row=0, column=2, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label
       
        student_email_textbox = ttk.Entry(Student_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_student_email)
        student_email_textbox.grid(row=0, column=3, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a first name label and textbox
        first_name_label = Label(Student_Information_Frame, text = "First Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        first_name_label.grid(row=2, column=0, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label

        first_name_textbox = ttk.Entry(Student_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_first_name)
        first_name_textbox.grid(row=2, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a last label and textbox
        last_name_label = Label(Student_Information_Frame, text = "Last Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        last_name_label.grid(row=2, column=2, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label
       
        last_name_textbox = ttk.Entry(Student_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_last_name)
        last_name_textbox.grid(row=2, column=3, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a Student Date Of Admission label and textbox
        date_of_admission_label = Label(Student_Information_Frame, text = "Date Of Admission: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        date_of_admission_label.grid(row=3, column=0, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label
       
        date_of_admission_textbox = ttk.Entry(Student_Information_Frame,width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_date_of_admission)        
        date_of_admission_textbox.grid(row=3, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a date of birth label and textbox
        date_of_birth_label = Label(Student_Information_Frame, text = "Date of Birth: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        date_of_birth_label.grid(row=3, column=2, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label

        date_of_birth_textbox = ttk.Entry(Student_Information_Frame,width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_date_of_birth)
        date_of_birth_textbox.grid(row=3, column=3, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # ======================================================================================================================================== #
        # Parent Inforamtion Frame: This frame will contain all the fields asking for information related to the parents
        Parent_Information_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Parent Details", font=("Segoe UI Variable", 12, "bold"))
        Parent_Information_Frame.place(x=5, y=300, width=826, height=150)
        # =================================================================== #
        # Adding in the student related text boxes and labels
        # Adding a student id label and textbox
        father_name_label = Label(Parent_Information_Frame, text = "Father's Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        father_name_label.grid(row=0, column=0, padx=(25,5), pady=17, sticky=W) # Specifying the coordinates of the label

        father_name_textbox = ttk.Entry(Parent_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_father_name)
        father_name_textbox.grid(row=0, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a Student Email label and textbox
        father_email_label = Label(Parent_Information_Frame, text = "Father's Email: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        father_email_label.grid(row=0, column=2, padx=(25,5), pady=17, sticky=W) # Specifying the coordinates of the label
       
        father_email_textbox = ttk.Entry(Parent_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_father_email)
        father_email_textbox.grid(row=0, column=3, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a first name label and textbox
        mother_name_label = Label(Parent_Information_Frame, text = "Mother's Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        mother_name_label.grid(row=2, column=0, padx=(25,5), pady=17, sticky=W) # Specifying the coordinates of the label

        mother_name_textbox = ttk.Entry(Parent_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_mother_name)
        mother_name_textbox.grid(row=2, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a last label and textbox
        mother_email_label = Label(Parent_Information_Frame, text = "Mother's Email: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        mother_email_label.grid(row=2, column=2, padx=(25,5), pady=17, sticky=W) # Specifying the coordinates of the label
       
        mother_email_textbox = ttk.Entry(Parent_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_mother_email)
        mother_email_textbox.grid(row=2, column=3, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # ======================================================================================================================================== #
        # Capture Student Face Frame: This frame will be blank in the beginning but after the user clicks on the capture 
        # student face button, the live video footage will be embedded in the frame
        Capture_Student_Face_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Capture Student Face", font=("Segoe UI Variable", 12, "bold"))
        Capture_Student_Face_Frame.place(x=835, y=85, width=430, height=365) # Specifying the coordinates along with the dimensions of the frame

        #======================================== Adding in the buttons ========================================#
        # Add New Student Profile Button
        update_student_Button = Button(Button_Frame, text="Update Student Profile", cursor="hand2", command = self.update_student_button, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        update_student_Button.place(x=5, y=5, height=65, width=365) # Specifying the coordinates along with the dimensions of the button

        # Capture Student Face
        capture_student_face_Button =  Button(Button_Frame, text="Capture Student Face", cursor="hand2", command = self.capture_face_button, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        capture_student_face_Button.place(x=5, y=75, height=65, width=365) # Specifying the coordinates along with the dimensions of the button

        # Clear All Fields Button
        clear_all_fields_Button = Button(Button_Frame, text="Clear All Fields", cursor="hand2", command = self.clear_all_button, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        clear_all_fields_Button.place(x=5, y=145, height=65, width=365) # Specifying the coordinates along with the dimensions of the button
       
        # Back to Student Account Management Button
        back_to_student_account_management_Button = Button(Button_Frame, text="Back to Previous Page", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        back_to_student_account_management_Button.place(x=5, y=216, height=65, width=365) # Specifying the coordinates along with the dimensions of the button

        # ======================================================================================================================================== #
        # Search Frame: This frame will contain the search system which will be show the user all the student profiles created
        Search_Frame= Frame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Search_Frame.place(x=5, y=460, width=875, height=285)

        # Adding a search bar
        search_label = Label(Search_Frame, text="Search By:", font=("Segoe UI Variable", 12, "bold"), bg="White", fg="Black")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Adding a Search by combo box
        search_combobox=ttk.Combobox(Search_Frame, font=("Segoe UI Variable", 12, "bold"), width=15, state="readonly")
        search_combobox["values"] = ("Select", "Student ID", "First Name", "LastName","Date of Birth", "Date Of Admission")
        search_combobox.current(0)
        search_combobox.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Adding an entry field textbox
        search_entry_textbox = ttk.Entry(Search_Frame, width=20, font=("Segoe UI Variable", 12, "bold"))
        search_entry_textbox.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        # Adding a Search button
        search_button = Button(Search_Frame, width=10, text="Search", cursor="hand2", font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="White")
        search_button.grid(row=0, column=3,padx=5, pady=5, sticky=W)
        
        # Adding a Show All button
        show_all_button = Button(Search_Frame, width=10, text="Show All", cursor="hand2", font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="White")
        show_all_button.grid(row=0, column=4, padx=5, pady=5, sticky=W)
#============================================================================================================================================================================================================
        # Table Frame
        Table_Frame= Frame(Search_Frame, bd=2, bg="White", relief=RIDGE)
        Table_Frame.place(x=0, y=45, width=870, height=235)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(Table_Frame, column=("std_ID", "first_name", "last_name", "email", "date_of_admission", "date_of_birth", "father_name", "father_email", "mother_name", "mother_email"), 
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
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
        self.student_table.heading("father_name", text="Father's Name")
        self.student_table.heading("father_email", text="Father Email")
        self.student_table.heading("mother_name", text="Mother's Name")
        self.student_table.heading("mother_email", text="Mother Email")
        self.student_table["show"] = "headings"
        
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
#                                                            END OF UI DESIGN
#===========================================================================================================================================#
#############################################################################################################################################
#===========================================================================================================================================#
#                                                      BUTTON IMPLEMENTATION FUNCTIONS
# ------------------------------------------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------------------------------------------#
    # Update button implementation
    def update_student_button(self):
    # Validating if the user has entered in all the details asked for on the Update Student Profile page
        if self.var_student_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_admission.get()=="" or self.var_date_of_birth.get()=="" or self.var_father_name.get()=="" or self.var_father_email.get()=="" or self.var_mother_name.get()=="" or self.var_mother_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            # Send an error message to the user if details are not completely filled
        else:
            # Adding a try except block inorder to prevent the system from stop functioning completely incase of an error
            try:
                # Asks the user if they want to update the selected profile
                update = messagebox.askyesno("Update Student Account", "Do you want to update student details?", parent=self.root)
                if update > 0:
                # If the user click yes, the change will be made in the database
                    conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
                    my_cursor = conn.cursor()
                    # Update student information SQL Query
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
                                                                            self.var_student_ID[0]))
                else:
                    # If not, the changes are not made
                    if not update:
                        return
                messagebox.showinfo("Success", "Student details have been successfully updated.", parent=self.root) # Printing a success message
                conn.commit() # Making the changes in the database
                self.fetch_data() # Reflecting the change in the table on this page
                conn.close() # Closing the database connection 
                self.clear_all_button() # Clearing all the data peasant in the textboxes
            except Exception as es:
                # Incase of any errors, an error box will be shown to the user which will contain the error code along with the error message
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Function to fetch the date in the table frame created
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
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
        self.var_date_of_admission.set(data[3]),
        self.var_student_email.set(data[4]),
        self.var_date_of_birth.set(data[5]),
        self.var_father_name.set(data[6]),
        self.var_father_email.set(data[7]),
        self.var_mother_name.set(data[8]),
        self.var_mother_email.set(data[9])
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Clear All Fields button Implementation
    def clear_all_button(self):
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
    def capture_face_button(self):
        # Validation that all fields are filled up
        if self.var_student_ID.get()=="" or self.var_student_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_admission.get()=="" or self.var_date_of_birth.get()=="" or self.var_father_name.get()=="" or self.var_father_email.get()=="" or self.var_mother_name.get()=="" or self.var_mother_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            # Added a try box to get rid pf any exceptions which might arise
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
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
                    # Scaling Factor = 1.3
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


# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Update_Student_Profile(root)
    root.mainloop()
