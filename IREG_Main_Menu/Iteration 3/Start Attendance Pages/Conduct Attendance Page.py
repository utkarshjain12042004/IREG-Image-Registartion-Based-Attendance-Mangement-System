# Importing all the required library modules to create the UI
from tkinter import *
from tkinter import ttk

class Conduct_Attendance:
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
        Automated_Attendace_Method_lbl= Label(mainFrame, text="Conduct Attendance", font=("Segoe UI Variable", 45, "bold"), bg="White", fg="Black")
        Automated_Attendace_Method_lbl.place(x=1, y=5, width=1270, height=75) # Specifying the coordinates along with the dimensions of the frame

        # Face Frame: This frame will show the real time video footage captured by the camera
        Face_Frame= Frame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Face_Frame.place(x=915, y=85, width=350, height=325) # Specifying the coordinates along with the dimensions of the frame

        # ================================================================================================= # 
        # Button Frame: This frame will contain the buttons required to conduct the attendance automatically
        Button_Frame= Frame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Button_Frame.place(x=915, y=415, width=350, height=325) # Specifying the coordinates along with the dimensions of the frame

        # ------------------------------------- Adding in the buttons ------------------------------------- #
        start_capture_Button = Button(Button_Frame, text="Start Capture", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White", width=27, height=3)
        start_capture_Button.grid(row=0, column=0, padx=6, pady=(10,5)) # Specifying the coordinates along with the dimensions of the button

        stop_capture_Button = Button(Button_Frame, text="Stop Capture", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White", width=27, height=3)
        stop_capture_Button.grid(row=1, column=0, padx=6, pady=(10,5)) # Specifying the coordinates along with the dimensions of the button

        store_attendance_Button = Button(Button_Frame, text="Store Attendance", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White", width=27, height=3)
        store_attendance_Button.grid(row=2, column=0, padx=6, pady=(10,5)) # Specifying the coordinates along with the dimensions of the button

        # ================================================================================================= # 
        # Attendance  Frame: This frame will contain a table which will show the students who have been marked present or absent in real time. 
        Attendance_Frame= Frame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Attendance_Frame.place(x=5, y=85, width=905, height=655) # Specifying the coordinates along with the dimensions of the frame

        # Adding a search bar
        search_label = Label(Attendance_Frame, text="Search By:", font=("Segoe UI Variable", 12, "bold"), bg="White", fg="Black")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Adding a Search by combo box
        search_combobox=ttk.Combobox(Attendance_Frame, font=("Segoe UI Variable", 12, "bold"), width=15, state="readonly")
        search_combobox["values"] = ("--Search By--", "Student ID", "First Name", "Last Name","Date of Birth")
        search_combobox.current(0)
        search_combobox.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Adding an entry field textbox
        search_entry_textbox = ttk.Entry(Attendance_Frame, width=20, font=("Segoe UI Variable", 12, "bold"))
        search_entry_textbox.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        # Adding a Sort by combo box
        sort_by_combobox=ttk.Combobox(Attendance_Frame, font=("Segoe UI Variable", 12, "bold"), width=10, state="readonly")
        sort_by_combobox["values"] = ("--Sort By--", "Student ID", "First Name", "Last Name")
        sort_by_combobox.current(0)
        sort_by_combobox.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Adding a Search button
        search_button = Button(Attendance_Frame, width=13, text="Search", cursor="hand2", font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="White")
        search_button.grid(row=0, column=4,padx=5, pady=5, sticky=W)
        
        # Adding a Show All button
        mark_all_present_button = Button(Attendance_Frame, width=14, text="Mark All Present", cursor="hand2", font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="White")
        mark_all_present_button.grid(row=0, column=5, padx=5, pady=5, sticky=W)

        #========================================================================================#
        # Scroll Bar
        # Table Frame
        Table_Frame= Frame(Attendance_Frame, bd=2, bg="White", relief=RIDGE)
        Table_Frame.place(x=0, y=45, width=901, height=606)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        
        self.attendance_table = ttk.Treeview(Table_Frame, column=("student_ID", "first_name", "last_name", "attendance_status", "date_of_attendance", "time_of_attendance"), 
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("student_ID", text="Student ID")
        self.attendance_table.heading("first_name", text="First Name")
        self.attendance_table.heading("last_name", text="Last Name")
        self.attendance_table.heading("attendance_status", text="Attendance Status")
        self.attendance_table.heading("date_of_attendance", text="Attendance Data")
        self.attendance_table.heading("time_of_attendance", text="Attendance Time")
        self.attendance_table["show"] = "headings"
        
        self.attendance_table.column("student_ID", width=68)
        self.attendance_table.column("first_name", width=130)
        self.attendance_table.column("last_name", width=130)
        self.attendance_table.column("attendance_status", width=130)
        self.attendance_table.column("date_of_attendance", width=120)
        self.attendance_table.column("time_of_attendance", width=120)

        self.attendance_table.pack(fill=BOTH, expand=1)

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Conduct_Attendance(root)
    root.mainloop()