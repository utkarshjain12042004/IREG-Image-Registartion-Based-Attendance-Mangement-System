# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
from Start_Attendance import Start_Attendance
from View_Attendance import View_Attendance
from Account_Management import Account_Management
from Settings import Settings


# Creating a class for the UI
class Face_Recognition_System:
    # This is the constructor of the class Face_Recognition_System
    def __init__(self, root):
        self.root = root
        self.root.geometry("1090x645+75+70")
        self.root.resizable(width=False, height=False)
        self.root.title("IREG")
        
        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="Light Yellow", relief = RIDGE)
        mainFrame.place(x=2, y=2, width=1086, height=640) 


        # Label Frame
        Image_Registration_lbl= Label(mainFrame, text="IREG: Image Registration", font=("Segoe UI Variable", 45, "bold"), bg="Light Yellow", fg="Black")
        Image_Registration_lbl.place(x=108, y=5, width=870, height=75)

        # Label Frame 2
        # title_lbl = Label(mainFrame, text="Image Registration", font=("Segoe UI Variable", 30, "bold"), bg="Light Yellow", fg="Black")
        # title_lbl.place(x=45, y=45, width=300, height=50)

        # Button Frame
        Button_Frame= LabelFrame(mainFrame, bd=2, bg="Light Yellow", relief=RIDGE)
        Button_Frame.place(x=393, y=166, width=300, height=228)
        

        #======================================== Adding in the buttons ========================================#
        # Start Attendance Button
        start_Attendance_Button = Button(Button_Frame, text="Start Attendance", cursor="hand2",command=self.Start_Attendance, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="Light Yellow")
        start_Attendance_Button.place(x=5,y=5, width=287, height=50)

        # View Attendance
        view_Attendance_Button =  Button(Button_Frame, text="View Attendance", cursor="hand2",command=self.View_Attendance, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="Light Yellow")
        view_Attendance_Button.place(x=5,y=60, width=287, height=50)

        # Account Management Button
        account_Management_Button = Button(Button_Frame, text="Account Management", command = self.Account_Management, cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="Light Yellow")
        account_Management_Button.place(x=5,y=115, width=287, height=50)

        # Exit Button
        exit_Button = Button(Button_Frame, text="Exit", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="Light Yellow")
        exit_Button.place(x=5,y=170, width=287, height=50)
        
        # Settings Button
        settings_Button = Button(mainFrame, text="Settings", cursor="hand2",command=self.Settings, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="Light Yellow")
        settings_Button.place(x=981,y=595, width=100, height=40)

# =======================================================================================================#
    # This method calls the Start attendance page and allows it to be displayed on the screen
    def Start_Attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Start_Attendance(self.new_window)
        self.root.withdraw()
        

    def View_Attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = View_Attendance(self.new_window)
        self.root.withdraw()

    def Account_Management(self):
        self.new_window = Toplevel(self.root)
        self.app = Account_Management(self.new_window)
        self.root.withdraw()

    def Settings(self):
        self.new_window = Toplevel(self.root)
        self.app = Settings(self.new_window)
        self.root.withdraw()

                                  
# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()





