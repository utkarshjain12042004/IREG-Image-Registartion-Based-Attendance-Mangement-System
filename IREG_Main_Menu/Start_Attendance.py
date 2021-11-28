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
        # Frame for displaying what method to be used for attendance


        # Adding buttons in the monday frame------------------------------------------------------------------------------------------------------------------------------------------- #
        





# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Start_Attendance(root)
    root.mainloop()