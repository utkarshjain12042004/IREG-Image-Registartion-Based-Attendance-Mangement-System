# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from Student_Account_Management import Student_Account_Management


class Account_Management:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x350+0+0")
        self.root.title("Account Management")

        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="White", relief = RIDGE)
        mainFrame.place(x=2, y=2, width=395, height=345)

        # Account Management Label Frame
        Account_Management_lbl = Label(mainFrame, text="Account Management", font=("Segoe UI Variable", 25, "bold"), bg="White", fg="Red")
        Account_Management_lbl.place(x=0, y=5, width=385, height=55)
#==========================================================================================================================================#
        # Account Management Frame frame: This frame will have the option to select what type of account is to be managed
        Account_Management_Frame = Frame(mainFrame, bd=2, bg="White", relief = RIDGE)
        Account_Management_Frame.place(x=25, y=100, width=344, height=134)
#==========================================================================================================================================#
        # Adding in Manage Student Accounts Button
        manage_student_accounts_button = Button(Account_Management_Frame, command=self.Manage_Student_Account_Button, text="Manage Student Accounts", cursor="hand2", font=("Segoe UI Variable", 18, "bold"), bg="Dark Blue", fg="White")
        manage_student_accounts_button.grid(row=0, padx=7, pady=7, sticky=W)
#==========================================================================================================================================#
        # Adding in Manage Teacher Accounts Button
        # manage_teacher_accounts_button = Button(Account_Management_Frame, text="Manage Teacher Accounts", cursor="hand2", font=("Segoe UI Variable", 18, "bold"), bg="Dark Blue", fg="White")
        # manage_teacher_accounts_button.grid(row=1, padx=7, pady=7, sticky=W)
#==========================================================================================================================================#
        # Adding a back button
        go_back_button = Button(mainFrame, text="Back", cursor="hand2", font=("Segoe UI Variable", 18, "bold"), bg="Dark Blue", fg="White")
        go_back_button.place(x=307, y=285)
#==========================================================================================================================================#
    # This method calls the Start attendance page and allows it to be displayed on the screen
    def Manage_Student_Account_Button(self):
        self.new_window = Toplevel(self.root)
        self.app = Student_Account_Management(self.new_window)


# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Account_Management(root)
    root.mainloop()

