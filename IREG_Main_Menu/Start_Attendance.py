# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import numpy as np
import cv2

# Creating a class for the UI
class Start_Attendance:
    # This is the constructor of the class Face_Recognition_System
    def __init__(self, root):
        self.root = root
        self.root.geometry("1090x645+0+0")
        self.root.title("IREG: Start Attendance")

############################################################################################################################################
#==========================================================================================================================================#
#                                                                UI DESIGN
# ========================================================================================================================================================
        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="Light Yellow", relief = RIDGE)
        mainFrame.place(x=2, y=2, width=1086, height=640) 

        # Label Frame
        Start_Attendance_lbl= Label(mainFrame, text="Start Attendance", font=("Segoe UI Variable", 45, "bold"), bg="Light Yellow", fg="Black")
        Start_Attendance_lbl.place(x=108, y=5, width=870, height=75)

        # Obtaining the current Date and time labels
        current_date_and_time = datetime.now()

        # Current Day Label
        Current_Day_lbl = Label(mainFrame, text = datetime.today().strftime("%A"), font = ("Calibri", 12, "bold"), bg = "Light Yellow", fg = "Black")
        Current_Day_lbl.place(x = 1016, y = 71, width = 65, height = 15)

        # Current date label
        Current_Date_lbl =  Label(mainFrame, text = current_date_and_time.strftime("%d/%m/%y"), font = ("Calibri", 12, "bold"), bg = "Light Yellow", fg = "Black")
        Current_Date_lbl.place(x = 1016, y = 91, width = 65, height = 15)

        # Current time label
        Current_Time_lbl =  Label(mainFrame, text = current_date_and_time.strftime("%H:%M:%S"), font = ("Calibri", 12, "bold"), bg = "Light Yellow", fg = "Black")
        Current_Time_lbl.place(x = 1016, y = 111, width = 65, height = 15) 

        # Button Frame
        Button_Frame= LabelFrame(mainFrame, bd=2, bg="Light Yellow", relief=RIDGE)
        Button_Frame.place(x=332, y=260, width=413, height=120)

        #======================================== Adding in the buttons ========================================#
        # Manual Attendance Method Button
        manual_attendance_method_button = Button(Button_Frame, text="Manual Attendance Method", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="Light Yellow")
        manual_attendance_method_button.place(x=5,y=5, width=400, height=50)

        # Automated Attendance Method Button
        automated_attendance_method_Button =  Button(Button_Frame, text="Automated Attendance Method", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="Light Yellow")
        automated_attendance_method_Button.place(x=5,y=60, width=400, height=50)

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Start_Attendance(root)
    root.mainloop()