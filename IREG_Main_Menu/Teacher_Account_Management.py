# importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import mysql.connector


class Teacher_Account_Management:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1114x449+0+0")
        self.root.title("Teacher_Account Management")

        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="White", relief = RIDGE)
        mainFrame.place(x=2, y=2, width=1110, height=445)                                                           

        # Account Management Label Frame
        teacher_Account_Management_lbl= Label(mainFrame, text="Teacher Account Management", font=("Segoe UI Variable", 25, "bold"), bg="White", fg="Red")
        teacher_Account_Management_lbl.place(x=300, y=5, width=500, height=55)
# ========================================================================================================================================================
        # Variables related to the teachers
        self.var_teacher_ID = StringVar()
        self.var_subject = StringVar()
        self.var_teacher_email = StringVar()
        self.var_phone_number = StringVar()
        self.var_gender = StringVar()
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_date_of_hiring = StringVar()
        self.var_date_of_birth = StringVar()
############################################################################################################################################
#==========================================================================================================================================#
#                                                                UI DESIGN
# ========================================================================================================================================================
        # teacher Information frame: This will contain all the information
        Teacher_Information_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Teacher Details", font=("Segoe UI Variable", 12, "bold"))
        Teacher_Information_Frame.place(x=5, y=70, width=888, height=100)
# ========================================================================================================================================================
        # Adding in the teacher related text boxes and labels
        # Adding a teacher Id label and textbox
        teacherID_label = Label(Teacher_Information_Frame, text = "Teacher ID: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        teacherID_label.grid(row=0, column=0, padx=3, pady=5, sticky=W)

        teacherID_textbox = ttk.Entry(Teacher_Information_Frame, textvariable=self.var_teacher_ID, font=("Segoe UI Variable", 11, "bold"))
        teacherID_textbox.grid(row=0, column=1, padx=3, pady=5, sticky=W)

        # Adding a subject taught label and combobox
        subject_taught_label = Label(Teacher_Information_Frame, text = "Subject Taught: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        subject_taught_label.grid(row=0, column=2, padx=3, pady=5, sticky=W)

        subject_taught_combobox=ttk.Combobox(Teacher_Information_Frame, font=("Segoe UI Variable", 11, "bold"), width=18, state="readonly")
        subject_taught_combobox["values"] = ("Select", "Math", "Physics", "Chemistry", "Biology")
        subject_taught_combobox.current(0)
        subject_taught_combobox.grid(row=0, column=3, padx=3, pady=5, sticky=W)

        # Adding a teacher Email label and textbox
        teacher_email_label = Label(Teacher_Information_Frame, text = "Email: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        teacher_email_label.grid(row=0, column=4, padx=3, pady=5, sticky=W)
        
        teacher_email_textbox = ttk.Entry(Teacher_Information_Frame, textvariable=self.var_teacher_email, font=("Segoe UI Variable", 11, "bold"))
        teacher_email_textbox.grid(row=0, column=5, padx=3, pady=5, sticky=W)
        
        # Adding a first name label and textbox
        first_name_label = Label(Teacher_Information_Frame, text = "First Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        first_name_label.grid(row=1, column=0, padx=3, pady=5, sticky=W)

        first_name_textbox = ttk.Entry(Teacher_Information_Frame, textvariable=self.var_first_name, font=("Segoe UI Variable", 11, "bold"))
        first_name_textbox.grid(row=1, column=1, padx=3, pady=5, sticky=W)

        # Adding a last label and textbox
        last_name_label = Label(Teacher_Information_Frame, text = "Last Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        last_name_label.grid(row=1, column=2, padx=3, pady=5, sticky=W)
        
        last_name_textbox = ttk.Entry(Teacher_Information_Frame, textvariable=self.var_last_name, font=("Segoe UI Variable", 11, "bold"))
        last_name_textbox.grid(row=1, column=3, padx=3, pady=5, sticky=W)

        # Adding a date of birth label and textbox
        date_of_birth_label = Label(Teacher_Information_Frame, text = "Date of Birth: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        date_of_birth_label.grid(row=1, column=4, padx=3, pady=5, sticky=W)

        date_of_birth_textbox = ttk.Entry(Teacher_Information_Frame, textvariable=self.var_date_of_birth, font=("Segoe UI Variable", 11, "bold"))
        date_of_birth_textbox.grid(row=1, column=5, padx=3, pady=5, sticky=W)

        # Adding a teacher Gender Label and a combobox
        #teacher_gender_label = Label(Teacher_Information_Frame, text = "Gender: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        #teacher_gender_label.grid(row=0, column=2, padx=3, pady=5, sticky=W)

        #teacher_gender_combobox=ttk.Combobox(Teacher_Information_Frame, font=("Segoe UI Variable", 11, "bold"), width=18, state="readonly")
        #teacher_gender_combobox["values"] = ("Select", "Male", "Female", "Other")
        #teacher_gender_combobox.current(0)
        #teacher_gender_combobox.grid(row=0, column=3, padx=3, pady=5, sticky=W)

        # Adding a teacher phone number label and textbox
        #teacher_phone_number_label = Label(Teacher_Information_Frame, text = "Phone Number: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        #teacher_phone_number_label.grid(row=2, column=2, padx=3, pady=5, sticky=W)

        #teacher_phone_number_textbox = ttk.Entry(Teacher_Information_Frame, textvariable=self.var_teacher_email, font=("Segoe UI Variable", 11, "bold"))
        #teacher_phone_number_textbox.grid(row=2, column=3, padx=3, pady=5, sticky=W)
# ========================================================================================================================================================
        # Adding a search frame which will have all the functions required to conduct a search
        Search_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Search System", font=("Segoe UI Variable", 12, "bold"))
        Search_Frame.place(x=5, y=180, width=888, height=255)

        # Adding a search bar
        search_label = Label(Search_Frame, text="Search By:", font=("Segoe UI Variable", 12, "bold"), bg="White", fg="Black")
        search_label.grid(row=0, column=0, padx=25, pady=5, sticky=W)
        
        # Adding a Search by combo box
        search_combobox=ttk.Combobox(Search_Frame, font=("Segoe UI Variable", 12, "bold"), width=17, state="readonly")
        search_combobox["values"] = ("Select", "Teacher ID", "Teacher Name", "Subject Taught")
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
        Table_Frame.place(x=5, y=45, width=873, height=180)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        
        self.teacher_table = ttk.Treeview(Table_Frame, column=("teacher_ID", "gender", "first_name", "last_name", "email", "phone_number", "subject_taught", "date_of_birth"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.teacher_table.xview)
        scroll_y.config(command=self.teacher_table.yview)

        self.teacher_table.heading("teacher_ID", text="Teacher ID")
        self.teacher_table.heading("gender", text="Gender")
        self.teacher_table.heading("first_name", text="First Name")
        self.teacher_table.heading("last_name", text="Last Name")
        self.teacher_table.heading("email", text="Email")
        self.teacher_table.heading("phone_number", text="Phone Number")
        self.teacher_table.heading("subject_taught", text="Subject Taught")
        self.teacher_table.heading("date_of_birth", text="Date Of Birth")
        self.teacher_table["show"] = "headings"


        self.teacher_table.column("teacher_ID", width=70)
        self.teacher_table.column("gender", width=130)
        self.teacher_table.column("first_name", width=130)
        self.teacher_table.column("last_name", width=130)
        self.teacher_table.column("email", width=120)
        self.teacher_table.column("phone_number", width=130) 
        self.teacher_table.column("subject_taught", width=130)
        self.teacher_table.column("date_of_birth", width=120)

        self.teacher_table.pack(fill=BOTH, expand=1)
# ==========================================================================================================================================#
        # Adding a button frame which will have the save, update and delete button
        Button_Frame = Frame(mainFrame, bd=2, relief=RIDGE, bg="White")
        Button_Frame.place(x=895, y=103, width=203, height=305)

        # Add Student button
        add_teacher_button = Button(Button_Frame, width=18, height=4, text="Add Teacher", font=("Segoe UI Variable", 12, "bold"), bg="Blue", fg="White")
        add_teacher_button.grid(row=0, padx=5, pady=5)
        
        # Update button
        update_button = Button(Button_Frame, width=18, height=4, text="Update Teacher Details", font=("Segoe UI Variable", 12, "bold"), bg="Blue", fg="White")
        update_button.grid(row=1, padx=5, pady=5)
        
        # Delete button
        delete_button = Button(Button_Frame, width=18, height=4, text="Delete Teacher", font=("Segoe UI Variable", 12, "bold"), bg="Blue", fg="White")
        delete_button.grid(row=2, padx=5, pady=5)
#                                                            END OF UI DESIGN
# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Teacher_Account_Management(root)
    root.mainloop()
