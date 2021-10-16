# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk


class Account_Management:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x700+0+0")
        self.root.title("Account Management")

        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="White", relief = RIDGE)
        mainFrame.place(x=2, y=2, width=596, height=696)

        # Account Management Label Frame
        Account_Management_lbl = Label(mainFrame, text="Account Management", font=("Helvetica", 25, "bold"), bg="White", fg="Red")
        Account_Management_lbl.place(x=97, y=5, width=400, height=55)

# ========================================================================================================================================================
        # Variables
        self.var_student_ID = StringVar()
        self.var_date_of_birth = StringVar()
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_semester = StringVar()
        self.var_div = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()
        self.var_radio2 = StringVar()
# ========================================================================================================================================================
        # Student Information frame: This will contain all the information
        Student_Information_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Student Details", font=("Helvetica", 12, "bold"))
        Student_Information_Frame.place(x=10, y=70, width=570, height=580)
# ========================================================================================================================================================
        # Adding in the student related text boxes and labels
        # Adding a student id label and textbox
        studentID_label = Label(Student_Information_Frame, text = "Student ID: ", font=("Helvetica", 11, "bold"), bg = "White")
        studentID_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        studentID_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_student_ID, width=20, font=("Helvetica", 11, "bold"))
        studentID_textbox.grid(row=0, column=1, padx=4, pady=5, sticky=W)

        # Adding a date of birth label and textbox
        date_of_birth_label = Label(Student_Information_Frame, text = "Date of Birth: ", font=("Helvetica", 11, "bold"), bg = "White")
        date_of_birth_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        date_of_birth_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_date_of_birth, width=20, font=("Helvetica", 11, "bold"))
        date_of_birth_textbox.grid(row=0, column=3, padx=4, pady=5, sticky=W)

        # Adding a first name label and textbox
        first_name_label = Label(Student_Information_Frame, text = "First Name: ", font=("Helvetica", 11, "bold"), bg = "White")
        first_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        first_name_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_first_name, width=20, font=("Helvetica", 11, "bold"))
        first_name_textbox.grid(row=2, column=1, padx=4, pady=5, sticky=W)

        # Adding a last label and textbox
        last_name_label = Label(Student_Information_Frame, text = "Last Name: ", font=("Helvetica", 11, "bold"), bg = "White")
        last_name_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        
        last_name_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_last_name, width=20, font=("Helvetica", 11, "bold"))
        last_name_textbox.grid(row=2, column=3, padx=4, pady=5, sticky=W)



    
    

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Account_Management(root)
    root.mainloop()
