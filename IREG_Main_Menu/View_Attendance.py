# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk


# Creating a class for the UI
class View_Attendance:
    # This is the constructor of the class Face_Recognition_System
    def __init__(self, root):
        self.root = root
        self.root.geometry("1090x645+0+0")
        self.root.title("IREG: Start Attendance")
        
        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="Light Yellow", relief = RIDGE)
        mainFrame.place(x=2, y=2, width=1086, height=640) 


        # Label Frame
        View_Attendance_lbl= Label(mainFrame, text="IREG: View Attendance", font=("Segoe UI Variable", 45, "bold"), bg="Light Yellow", fg="Black")
        View_Attendance_lbl.place(x=108, y=5, width=870, height=75)

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = View_Attendance(root)
    root.mainloop()