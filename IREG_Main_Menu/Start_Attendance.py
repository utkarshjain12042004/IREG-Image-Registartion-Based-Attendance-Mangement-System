# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk


class Start_Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x700+0+0")
        self.root.title("Start Attendance")

        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="White", relief = RIDGE)
        mainFrame.place(x=2, y=2, width=595, height=695)

        # Start Attendance Label Frame
        Start_Attendance_lbl = Label(mainFrame, text="Start Attendance", font=("Helvetica", 25, "bold"), bg="White", fg="Red")
        Start_Attendance_lbl.place(x=122, y=0, width=150, height=55)

# ========================================================================================================================================================
        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()
        self.var_radio2 = StringVar()
# ========================================================================================================================================================
        # Student Information frame: This will contain all the information




    
    

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Start_Attendance(root)
    root.mainloop()
