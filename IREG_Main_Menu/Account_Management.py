# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk


class Account_Management:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1090x645+75+70")
        self.root.resizable(width=False, height=False)
        self.root.title("Account Management")

        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="Light Yellow", relief = RIDGE)
        mainFrame.place(x=2, y=2, width=1086, height=640) 

        # Account Management Label Frame
        Account_Management_lbl= Label(mainFrame, text="Account Management", font=("Segoe UI Variable", 45, "bold"), bg="Light Yellow", fg="Black")
        Account_Management_lbl.place(x=108, y=5, width=870, height=75)
#==========================================================================================================================================#
        # Account Management Frame frame: This frame will have the option to select what type of account is to be managed
        Account_Management_Frame = Frame(mainFrame, bd=2, bg="Light Yellow", relief = RIDGE)
        Account_Management_Frame.place(x=371, y=213, width=344, height=134)
#==========================================================================================================================================#
        # Adding in Manage Student Accounts Button
        manage_student_accounts_button = Button(Account_Management_Frame, command=self.Manage_Student_Account_Button, text="Manage Student Accounts", cursor="hand2", font=("Segoe UI Variable", 18, "bold"), bg="Black", fg="Light Yellow")
        manage_student_accounts_button.grid(row=0, padx=7, pady=7, sticky=W)
#==========================================================================================================================================#
        # Adding in Manage Teacher Accounts Button
        # manage_teacher_accounts_button = Button(Account_Management_Frame, text="Manage Teacher Accounts", cursor="hand2", font=("Segoe UI Variable", 18, "bold"), bg="Black", fg="Light Yellow")
        # manage_teacher_accounts_button.grid(row=1, padx=7, pady=7, sticky=W)
#==========================================================================================================================================#
        # Adding a back button
        go_back_button = Button(mainFrame, text="Back", cursor="hand2", font=("Segoe UI Variable", 18, "bold"), bg="Black", fg="Light Yellow")
        go_back_button.place(x=1000, y=583)
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

