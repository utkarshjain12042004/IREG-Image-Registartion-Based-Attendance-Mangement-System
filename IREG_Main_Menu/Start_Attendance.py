# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk


# Creating a class for the UI
class Start_Attendance:
    # This is the constructor of the class Face_Recognition_System
    def __init__(self, root):
        self.root = root
        self.root.geometry("1090x645+75+70")
        self.root.resizable(width=False, height=False)
        self.root.title("IREG: Start Attendance")
        
        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="Light Yellow", relief = RIDGE)
        mainFrame.place(x=2, y=2, width=1086, height=640) 

        # Label Frame
        Start_Attendance_lbl = Label(mainFrame, text="IREG: Start Attendance", font=("Segoe UI Variable", 45, "bold"), bg="Light Yellow", fg="Black")
        Start_Attendance_lbl.place(x=108, y=0, width=870, height=75)
# ======Creating Frames=================================================================================================================================== #
        # Creating separate frames which will have the buttons to the different classes the teacher will have on those days. 
        # Monday Label Frame
        Monday_Frame  = Frame(mainFrame, bd=2, bg="Light Yellow", relief=RIDGE)
        Monday_Frame.place(x=5, y=70, width=1072, height=112)

        # Tuesday Label Frame
        Tuesday_Frame  = Frame(mainFrame, bd=2, bg="Light Yellow", relief=RIDGE)
        Tuesday_Frame.place(x=5, y=182, width=1072, height=112)

        # Wednesday Label Frame
        Wednesday_Frame  = Frame(mainFrame, bd=2, bg="Light Yellow", relief=RIDGE)
        Wednesday_Frame.place(x=5, y=294, width=1072, height=112)

        # Thursday Label Frame
        Thursday_Frame  = Frame(mainFrame, bd=2, bg="Light Yellow", relief=RIDGE)
        Thursday_Frame.place(x=5, y=406, width=1072, height=112)

        # Friday Label Frame
        Friday_Frame  = Frame(mainFrame, bd=2, bg="Light Yellow", relief=RIDGE)
        Friday_Frame.place(x=5, y=518, width=1072, height=112)
# ======Adding Day Labels in the Frames=================================================================================================================================== #
        # Monday Label 
        Monday_lbl = Label(Monday_Frame, text="Monday", font=("Segoe UI Variable", 20, "bold"), bg="Light Yellow", fg="Black")
        Monday_lbl.place(x=2, y=2, width=150, height=105)

        # Tuesday Label 
        Tuesday_lbl = Label(Tuesday_Frame, text="Tuesday", font=("Segoe UI Variable", 20, "bold"), bg="Light Yellow", fg="Black")
        Tuesday_lbl.place(x=2, y=2, width=150, height=105)

        # Wednesday Label 
        Wednesday_lbl = Label(Wednesday_Frame, text="Wednesday", font=("Segoe UI Variable", 20, "bold"), bg="Light Yellow", fg="Black")
        Wednesday_lbl.place(x=2, y=2, width=150, height=105)

        # Thursday Label 
        Thursday_lbl = Label(Thursday_Frame, text="Thursday", font=("Segoe UI Variable", 20, "bold"), bg="Light Yellow", fg="Black")
        Thursday_lbl.place(x=2, y=2, width=150, height=105)

        # Friday Label
        Friday_lbl = Label(Friday_Frame, text="Friday", font=("Segoe UI Variable", 20, "bold"), bg="Light Yellow", fg="Black")
        Friday_lbl.place(x= 2, y=2, width=150, height=105)
# ======Placing the buttons in the individual frames=================================================================================================================================== #
        

        # Adding buttons in the monday frame------------------------------------------------------------------------------------------------------------------------------------------- #
        





# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Start_Attendance(root)
    root.mainloop()