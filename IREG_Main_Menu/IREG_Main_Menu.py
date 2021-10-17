# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from Account_Management import Account_Management


# Creating a class for the UI
class Face_Recognition_System:
    # This is the constructor of the class Face_Recognition_System
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x500+0+0")
        self.root.title("IREG")
        
        # Main frame
        mainFrame = Frame(bd=2, bg="White", relief = RIDGE)
        mainFrame.place(x=2, y=2, width=395, height=495)


        # Label Frame
        Image_Registration_lbl = Label(mainFrame, text="IREG", font=("Segoe UI Variable", 25, "bold"), bg="White", fg="Red")
        Image_Registration_lbl.place(x=122, y=0, width=150, height=55)

        # Label Frame 2
        title_lbl = Label(mainFrame, text="Image Registration", font=("Segoe UI Variable", 25, "bold"), bg="White", fg="Red")
        title_lbl.place(x=45, y=45, width=300, height=50)

        # Button Frame
        Button_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Button_Frame.place(x=46, y=150, width=300, height=228)
        

        #======================================== Adding in the buttons ========================================#
        # Start Attendance Button
        start_Attendance_Button = Button(Button_Frame, text="Start Attendance", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Dark Blue", fg="White")
        start_Attendance_Button.place(x=5,y=5, width=287, height=50)

        # View Attendance
        view_Attendance_Button =  Button(Button_Frame, text="View Attendance", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Dark Blue", fg="White")
        view_Attendance_Button.place(x=5,y=60, width=287, height=50)

        # Account Management Button
        account_Management_Button = Button(Button_Frame, text="Account Management", command = self.Account_Management, cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Dark Blue", fg="White")
        account_Management_Button.place(x=5,y=115, width=287, height=50)

        # Exit Button
        exit_Button = Button(Button_Frame, text="Exit", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Dark Blue", fg="White")
        exit_Button.place(x=5,y=170, width=287, height=50)   
        
        # Settings Button
        settings_Button = Button(mainFrame, text="Settings", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Dark Blue", fg="White")
        settings_Button.place(x=285,y=445, width=100, height=40)

# =======================================================================================================#
    # This method calls the Start attendance page and allows it to be displayed on the screen
    def Account_Management(self):
        self.new_window = Toplevel(self.root)
        self.app = Account_Management(self.new_window)



                                  
# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()





