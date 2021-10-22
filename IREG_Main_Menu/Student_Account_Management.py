# importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import mysql.connector


class Student_Account_Management:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1090x645+0+0")
        self.root.title("Student_Account Management")

        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="White", relief = RIDGE)
        mainFrame.place(x=2, y=2, width=1086, height=640)                                                           

        # Account Management Label Frame
        Student_Account_Management_lbl= Label(mainFrame, text="Student Account Management", font=("Segoe UI Variable", 25, "bold"), bg="White", fg="Red")
        Student_Account_Management_lbl.place(x=293, y=5, width=500, height=55)

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
############################################################################################################################################
#==========================================================================================================================================#
#                                                                UI DESIGN
# ========================================================================================================================================================
        # Student Information frame: This will contain all the information
        Student_Information_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Student Details", font=("Segoe UI Variable", 11, "bold"))
        Student_Information_Frame.place(x=5, y=70, width=615, height=135)
# ========================================================================================================================================================
        # Adding in the student related text boxes and labels
        # Adding a student id label and textbox
        studentID_label = Label(Student_Information_Frame, text = "Student ID: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        studentID_label.grid(row=0, column=0, padx=2, pady=5, sticky=W)

        studentID_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_student_ID, font=("Segoe UI Variable", 11, "bold"))
        studentID_textbox.grid(row=0, column=1, padx=3, pady=5, sticky=W)

        # Adding a Student Email label and textbox
        student_email_label = Label(Student_Information_Frame, text = "Student Email: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        student_email_label.grid(row=0, column=2, padx=4, pady=5, sticky=W)
        
        student_email_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_student_email, font=("Segoe UI Variable", 11, "bold"))
        student_email_textbox.grid(row=0, column=3, padx=3, pady=5, sticky=W)

        # Adding a first name label and textbox
        first_name_label = Label(Student_Information_Frame, text = "First Name: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        first_name_label.grid(row=2, column=0, padx=2, pady=5, sticky=W)

        first_name_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_first_name, font=("Segoe UI Variable", 11, "bold"))
        first_name_textbox.grid(row=2, column=1, padx=3, pady=5, sticky=W)

        # Adding a last label and textbox
        last_name_label = Label(Student_Information_Frame, text = "Last Name: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        last_name_label.grid(row=2, column=2, padx=4, pady=5, sticky=W)
        
        last_name_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_last_name, font=("Segoe UI Variable", 11, "bold"))
        last_name_textbox.grid(row=2, column=3, padx=3, pady=5, sticky=W)

        # Adding a Student Year of Admission label and textbox
        year_of_admission_label = Label(Student_Information_Frame, text = "Year of Admission: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        year_of_admission_label.grid(row=3, column=0, padx=2, pady=5, sticky=W)
        
        year_of_admission_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_year_of_admission, font=("Segoe UI Variable", 11, "bold"))
        year_of_admission_textbox.grid(row=3, column=1, padx=3, pady=5, sticky=W)

        # Adding a date of birth label and textbox
        date_of_birth_label = Label(Student_Information_Frame, text = "Date of Birth: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        date_of_birth_label.grid(row=3, column=2, padx=4, pady=5, sticky=W)

        date_of_birth_textbox = ttk.Entry(Student_Information_Frame, textvariable=self.var_date_of_birth, font=("Segoe UI Variable", 11, "bold"))
        date_of_birth_textbox.grid(row=3, column=3, padx=3, pady=5, sticky=W)
# ========================================================================================================================================================
        # Parent Information Frame: This frame have the fields asking information for the student's parents
        Parent_Information_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Parent Details", font=("Segoe UI Variable", 11, "bold"))
        Parent_Information_Frame.place(x=5, y=210, width=615, height=163)
# ========================================================================================================================================================
        # Adding a subframe for fathers details
        Father_Information_Frame= LabelFrame(Parent_Information_Frame, bd=2, bg="White", relief=RIDGE, text="Father's Details", font=("Segoe UI Variable", 11, "bold"))
        Father_Information_Frame.place(x=10, y=4, width=290, height=130)
# ========================================================================================================================================================
        # Adding the information labels and text boxes
        # Adding father's first name label and text box
        father_first_name_label = Label(Father_Information_Frame, text = "First Name: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        father_first_name_label.grid(row=0, column=0, padx=4, pady=5, sticky=W)

        father_first_name_textbox = ttk.Entry(Father_Information_Frame, width=21, textvariable=self.var_father_first_name, font=("Segoe UI Variable", 11, "bold"))
        father_first_name_textbox.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        # Adding father's last name label and text box
        father_last_name_label = Label(Father_Information_Frame, text = "Last Name: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        father_last_name_label.grid(row=1, column=0, padx=4, pady=5, sticky=W)

        father_last_name_textbox = ttk.Entry(Father_Information_Frame, width=21, textvariable=self.var_father_last_name, font=("Segoe UI Variable", 11, "bold"))
        father_last_name_textbox.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        # Adding father's email label and text box
        father_email_label = Label(Father_Information_Frame, text = "Email: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        father_email_label.grid(row=2, column=0, padx=4, pady=5, sticky=W)

        father_email_textbox = ttk.Entry(Father_Information_Frame, width=21, textvariable=self.var_father_email, font=("Segoe UI Variable", 11, "bold"))
        father_email_textbox.grid(row=2, column=1, padx=5, pady=5, sticky=W)

# ========================================================================================================================================================
        # Adding a subframe for mothers details
        Mother_Information_Frame= LabelFrame(Parent_Information_Frame, bd=2, bg="White", relief=RIDGE, text="Mother's Details", font=("Segoe UI Variable", 11, "bold"))
        Mother_Information_Frame.place(x=310, y=4, width=290, height=130)
# ========================================================================================================================================================
        # Adding the information labels and text boxes
        # Adding mother's first name label and text box
        mother_first_name_label = Label(Mother_Information_Frame, text = "First Name: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        mother_first_name_label.grid(row=0, column=0, padx=4, pady=5, sticky=W)

        mother_first_name_textbox = ttk.Entry(Mother_Information_Frame, width=21, textvariable=self.var_mother_first_name, font=("Segoe UI Variable", 11, "bold"))
        mother_first_name_textbox.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        # Adding mother's last name label and text box
        mother_last_name_label = Label(Mother_Information_Frame, text = "Last Name: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        mother_last_name_label.grid(row=1, column=0, padx=4, pady=5, sticky=W)

        mother_last_name_textbox = ttk.Entry(Mother_Information_Frame, width=21, textvariable=self.var_mother_last_name, font=("Segoe UI Variable", 11, "bold"))
        mother_last_name_textbox.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        # Adding mother's email label and text box
        mother_email_label = Label(Mother_Information_Frame, text = "Email: ", font=("Segoe UI Variable", 11, "bold"), bg = "White")
        mother_email_label.grid(row=2, column=0, padx=4, pady=5, sticky=W)

        mother_email_textbox = ttk.Entry(Mother_Information_Frame, width=21, textvariable=self.var_mother_email, font=("Segoe UI Variable", 11, "bold"))
        mother_email_textbox.grid(row=2, column=1, padx=5, pady=5, sticky=W)
# ========================================================================================================================================================
        # Adding a search frame which will have all the functions required to conduct a search
        Search_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Search System", font=("Segoe UI Variable", 11, "bold"))
        Search_Frame.place(x=5, y=380, width=860, height=250)

        # Adding a search bar
        search_label = Label(Search_Frame, text="Search By:", font=("Segoe UI Variable", 12, "bold"), bg="White", fg="Black")
        search_label.grid(row=0, column=0, padx=25, pady=5, sticky=W)

        # Adding a Search by combo box
        search_combobox=ttk.Combobox(Search_Frame, font=("Segoe UI Variable", 12, "bold"), width=17, state="readonly")
        search_combobox["values"] = ("Select", "Student ID", "Student Name", "Date of Birth")
        search_combobox.current(0)
        search_combobox.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Adding an entry field textbox
        search_entry_textbox = ttk.Entry(Search_Frame, width=26, font=("Segoe UI Variable", 12, "bold"))
        search_entry_textbox.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # Adding a Search button
        search_button = Button(Search_Frame, width=9, text="Search", cursor="hand2", font=("Segoe UI Variable", 12, "bold"), bg="Blue", fg="White")
        search_button.grid(row=0, column=3,padx=10, pady=5, sticky=W)
        
        # Adding a Show All button
        show_all_button = Button(Search_Frame, width=9, text="Show All", cursor="hand2", font=("Segoe UI Variable", 12, "bold"), bg="Blue", fg="White")
        show_all_button.grid(row=0, column=4, padx=10, pady=5, sticky=W)
#============================================================================================================================================================================================================
        # Table Frame
        Table_Frame= Frame(Search_Frame, bd=2, bg="White", relief=RIDGE)
        Table_Frame.place(x=5, y=45, width=845, height=180)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(Table_Frame, column=("std_ID", "first_name", "last_name", "year_of_admission", "date_of_birth", "father_first_name", "father_last_name", "father_email", "mother_first_name", "mother_last_name", "mother_email"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("std_ID", text="Student ID")
        self.student_table.heading("first_name", text="First Name")
        self.student_table.heading("last_name", text="Last Name")
        self.student_table.heading("year_of_admission", text="Year Of Admission")
        self.student_table.heading("date_of_birth", text="Date Of Birth")
        self.student_table.heading("father_first_name", text="Father's First Name")
        self.student_table.heading("father_last_name", text="Father's Last Name")
        self.student_table.heading("father_email", text="Father Email")
        self.student_table.heading("mother_first_name", text="Mother's First Name")
        self.student_table.heading("mother_last_name", text="Mother's Last Name")
        self.student_table.heading("mother_email", text="Mother Email")
        self.student_table["show"] = "headings"

        
        self.student_table.column("std_ID", width=70)
        self.student_table.column("first_name", width=130)
        self.student_table.column("last_name", width=130)
        self.student_table.column("year_of_admission", width=120)
        self.student_table.column("date_of_birth", width=120)
        self.student_table.column("father_first_name", width=130) 
        self.student_table.column("father_last_name", width=130)
        self.student_table.column("father_email", width=150)
        self.student_table.column("mother_first_name", width=130)
        self.student_table.column("mother_last_name", width=130)
        self.student_table.column("mother_email", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
# ==========================================================================================================================================#
        # Adding a student face frame. This frame will show the video footage
        Student_Face_Capture_Frame = Frame(mainFrame, bd=2, bg="White", relief = RIDGE)
        Student_Face_Capture_Frame.place(x=630, y=79, width=446, height=295)
# ==========================================================================================================================================#
        # Adding a camera footage frame which is labelled as student face frame. This will show the real time camera footage when a 
        # button is clicked
        Student_Face_Frame = Frame(Student_Face_Capture_Frame, bd=2, bg="White", relief = RIDGE)
        Student_Face_Frame.place(x=5, y=5, width=281, height=281)

        # Adding a student face label
        student_face_label = Label(Student_Face_Capture_Frame, text="Student Face", font=("Segoe UI Variable", 12, "bold"), bg="White", fg="Black")
        student_face_label.place(x=300, y=5)

        # Adding a capture face button below the label
        capture_face_button = Button(Student_Face_Capture_Frame, width=14, cursor="hand2", text="Capture Face", font=("Segoe UI Variable", 12, "bold"), bg="Blue", fg="White")
        capture_face_button.place(x=290, y=30)
# ==========================================================================================================================================#
        # Adding a button frame which will have the save, update and delete button
        Button_Frame = Frame(mainFrame, bd=2, relief=RIDGE, bg="White")               
        Button_Frame.place(x=873, y=385, width=203, height=247 )

        # Add Student button
        add_student_button = Button(Button_Frame, width=18, height=3, text="Add Student", font=("Segoe UI Variable", 12, "bold"), bg="Blue", fg="White")
        add_student_button.grid(row=0, padx=5, pady=5)
        
        # Update button
        update_button = Button(Button_Frame, width=18, height=3, text="Update Student Details", font=("Segoe UI Variable", 12, "bold"), bg="Blue", fg="White")
        update_button.grid(row=1, padx=5, pady=5)
        
        # Delete button
        delete_button = Button(Button_Frame, width=18, height=3, text="Delete Student", font=("Segoe UI Variable", 12, "bold"), bg="Blue", fg="White")
        delete_button.grid(row=2, padx=5, pady=5)
#                                                            END OF UI DESIGN
#===========================================================================================================================================#
#############################################################################################################################################
#===========================================================================================================================================#
#                                                      BUTTON IMPLEMENTATION FUNCTIONS

    # Function for adding in the data when the user clicks on the add student button
    #def add_student_button(self):
    #    if self.var_student_ID.get()=="" or self.var_student_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_year_of_admission.get()=="" or self.var_date_of_birth.get()=="" or self.var_father_first_name.get()=="" or self.var_father_last_name.get()=="" or self.var_father_email.get()=="" or self.var_mother_first_name.get()=="" or self.var_mother_last_name.get()=="" or self.var_mother_email.get()=="":
    #        messagebox.showerror("Error", "All fields are required", parent=self.root)
    #    else:
    #        try:
    #            conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="advance_face_recognition_project")
    #            my_cursor = conn.cursor()




# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Student_Account_Management(root)
    root.mainloop()
