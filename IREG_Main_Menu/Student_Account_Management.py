# iporting all the required modules to create the UI
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk


class Student_Account_Management:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x700+0+0")
        self.root.title("Student_Account Management")

        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="White", relief = RIDGE)
        mainFrame.place(x=2, y=2, width=596, height=696)

        # Account Management Label Frame
        Student_Account_Management_lbl= Label(mainFrame, text="Student Account Management", font=("Segoe UI Variable", 25, "bold"), bg="White", fg="Red")
        Student_Account_Management_lbl.place(x=48, y=5, width=500, height=55)

# ========================================================================================================================================================
        # Variables related to the students
        self.var_student_ID = StringVar()
        self.var_student_email = StringVar()
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_year_of_admission = StringVar()
        self.var_date_of_birth = StringVar()
        
        # Variables related to the father
        self.var_father_first_name = StringVar()
        self.var_father_last_name = StringVar()
        self.var_father_email = StringVar()

        # Variables related to the mother
        self.var_mother_first_name = StringVar()
        self.var_mother_last_name = StringVar()
        self.var_mother_email = StringVar()
# ========================================================================================================================================================
        # Student Information frame: This will contain all the information
        Student_Information_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Student Details", font=("Segoe UI Variable", 12, "bold"))
        Student_Information_Frame.place(x=5, y=70, width=583, height=170)
# ========================================================================================================================================================
        # Adding in the student related text boxes and labels
        # Adding a student id label and textbox
        studentID_label = Label(Student_Information_Frame, text = "Student ID: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        studentID_label.grid(row=0, column=0, padx=2, pady=5, sticky=W)

        studentID_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_student_ID, width=18, font=("Segoe UI Variable", 11, "bold"))
        studentID_textbox.grid(row=0, column=1, padx=3, pady=5, sticky=W)

        # Adding a Student Email label and textbox
        student_email_label = Label(Student_Information_Frame, text = "Student Email: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        student_email_label.grid(row=0, column=2, padx=4, pady=5, sticky=W)
        
        student_email_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_student_email, width=18, font=("Segoe UI Variable", 11, "bold"))
        student_email_textbox.grid(row=0, column=3, padx=3, pady=5, sticky=W)

        # Adding a first name label and textbox
        first_name_label = Label(Student_Information_Frame, text = "First Name: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        first_name_label.grid(row=2, column=0, padx=2, pady=5, sticky=W)

        first_name_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_first_name, width=18, font=("Segoe UI Variable", 11, "bold"))
        first_name_textbox.grid(row=2, column=1, padx=3, pady=5, sticky=W)

        # Adding a last label and textbox
        last_name_label = Label(Student_Information_Frame, text = "Last Name: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        last_name_label.grid(row=2, column=2, padx=4, pady=5, sticky=W)
        
        last_name_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_last_name, width=18, font=("Segoe UI Variable", 11, "bold"))
        last_name_textbox.grid(row=2, column=3, padx=3, pady=5, sticky=W)

        # Adding a Student Year of Admission label and textbox
        year_of_admission_label = Label(Student_Information_Frame, text = "Year of Admission: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        year_of_admission_label.grid(row=3, column=0, padx=2, pady=5, sticky=W)
        
        year_of_admission_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_year_of_admission, width=18, font=("Segoe UI Variable", 11, "bold"))
        year_of_admission_textbox.grid(row=3, column=1, padx=3, pady=5, sticky=W)

        # Adding a date of birth label and textbox
        date_of_birth_label = Label(Student_Information_Frame, text = "Date of Birth: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        date_of_birth_label.grid(row=3, column=2, padx=4, pady=5, sticky=W)

        date_of_birth_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_date_of_birth, width=18, font=("Segoe UI Variable", 11, "bold"))
        date_of_birth_textbox.grid(row=3, column=3, padx=3, pady=5, sticky=W)

        # Adding a student face label and a button which when clicked will direct the user to another page which will show the video footage
        student_face_label = Label(Student_Information_Frame, text = "Student Face: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        student_face_label.grid(row=4, column=0, padx=4, pady=5, sticky=W)

        take_photo_sample_button = Button(Student_Information_Frame, text="Take Photo Sample", cursor="hand2", font=("Segoe UI Variable", 11, "bold"), bg="Dark Blue", fg="White")
        take_photo_sample_button.grid(row=4, column=1, columnspan=2, padx=3, pady=5, sticky=W)
# ========================================================================================================================================================
        # Parent Information Frame: This frame have the fields asking information for the student's parents
        Parent_Information_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Parent Details", font=("Segoe UI Variable", 12, "bold"))
        Parent_Information_Frame.place(x=5, y=250, width=583, height=163)
# ========================================================================================================================================================
        # Adding a subframe for fathers details
        Father_Information_Frame= LabelFrame(Parent_Information_Frame, bd=2, bg="White", relief=RIDGE, text="Father's Details", font=("Segoe UI Variable", 12, "bold"))
        Father_Information_Frame.place(x=5, y=4, width=280, height=130)
# ========================================================================================================================================================
        # Adding the information labels and text boxes
        # Adding father's first name label and text box
        father_first_name_label = Label(Father_Information_Frame, text = "First Name: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        father_first_name_label.grid(row=0, column=0, padx=4, pady=5, sticky=W)

        father_first_name_textbox = ttk.Entry(Father_Information_Frame, textvariable=self.var_father_first_name, font=("Segoe UI Variable", 11, "bold"))
        father_first_name_textbox.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        # Adding father's last name label and text box
        father_last_name_label = Label(Father_Information_Frame, text = "Last Name: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        father_last_name_label.grid(row=1, column=0, padx=4, pady=5, sticky=W)

        father_last_name_textbox = ttk.Entry(Father_Information_Frame, textvariable=self.var_father_last_name, font=("Segoe UI Variable", 11, "bold"))
        father_last_name_textbox.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        # Adding father's email label and text box
        father_email_label = Label(Father_Information_Frame, text = "Email: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        father_email_label.grid(row=2, column=0, padx=4, pady=5, sticky=W)

        father_email_textbox = ttk.Entry(Father_Information_Frame, textvariable=self.var_father_email, font=("Segoe UI Variable", 11, "bold"))
        father_email_textbox.grid(row=2, column=1, padx=5, pady=5, sticky=W)

# ========================================================================================================================================================
        # Adding a subframe for mothers details
        Mother_Information_Frame= LabelFrame(Parent_Information_Frame, bd=2, bg="White", relief=RIDGE, text="Mother's Details", font=("Segoe UI Variable", 12, "bold"))
        Mother_Information_Frame.place(x=295, y=4, width=280, height=130)
# ========================================================================================================================================================
        # Adding the information labels and text boxes
        # Adding mother's first name label and text box
        mother_first_name_label = Label(Mother_Information_Frame, text = "First Name: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        mother_first_name_label.grid(row=0, column=0, padx=4, pady=5, sticky=W)

        mother_first_name_textbox = ttk.Entry(Mother_Information_Frame, textvariable=self.var_mother_first_name, font=("Segoe UI Variable", 11, "bold"))
        mother_first_name_textbox.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        # Adding mother's last name label and text box
        mother_last_name_label = Label(Mother_Information_Frame, text = "Last Name: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        mother_last_name_label.grid(row=1, column=0, padx=4, pady=5, sticky=W)

        mother_last_name_textbox = ttk.Entry(Mother_Information_Frame, textvariable=self.var_mother_last_name, font=("Segoe UI Variable", 11, "bold"))
        mother_last_name_textbox.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        # Adding mother's email label and text box
        mother_email_label = Label(Mother_Information_Frame, text = "Email: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        mother_email_label.grid(row=2, column=0, padx=4, pady=5, sticky=W)

        mother_email_textbox = ttk.Entry(Mother_Information_Frame, textvariable=self.var_mother_email, font=("Segoe UI Variable", 11, "bold"))
        mother_email_textbox.grid(row=2, column=1, padx=5, pady=5, sticky=W)
# ========================================================================================================================================================





    
    

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Student_Account_Management(root)
    root.mainloop()
