# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import numpy as np
import cv2

# Creating a class for the UI
class Settings:
    # This is the constructor of the class Face_Recognition_System
    def __init__(self, root):
        self.root = root
        self.root.geometry("1090x645+0+0")
        self.root.title("Settings")

############################################################################################################################################
#==========================================================================================================================================#
#                                                                UI DESIGN
# ========================================================================================================================================================
        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="Light Yellow", relief = RIDGE)
        mainFrame.place(x=2, y=2, width=1086, height=640) 


        # Label Frame
        IREG_Settings_lbl= Label(mainFrame, text="IREG Settings", font=("Segoe UI Variable", 45, "bold"), bg="Light Yellow", fg="Black")
        IREG_Settings_lbl.place(x=108, y=5, width=870, height=75)

        # Button Frame
        Button_Frame= LabelFrame(mainFrame, bd=2, bg="Light Yellow", relief=RIDGE)
        Button_Frame.place(x=393, y=166, width=300, height=228)
        

        #======================================== Adding in the buttons ========================================#
        # Train Data Button
        train_data_button = Button(Button_Frame, text="Train Data", cursor="hand2", command=self.train_data_button, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="Light Yellow")
        train_data_button.place(x=5,y=5, width=287, height=50)

        # Student Faces
        student_faces_Button =  Button(Button_Frame, text="Student Faces", cursor="hand2",command=self.student_faces_button, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="Light Yellow")
        student_faces_Button.place(x=5,y=60, width=287, height=50)

        # Account Management Button
        # account_Management_Button = Button(Button_Frame, text="Account Management", command = self.Account_Management, cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="Light Yellow")
        # account_Management_Button.place(x=5,y=115, width=287, height=50)
          
        # Exit Button
        # exit_Button = Button(Button_Frame, text="Exit", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="Light Yellow")
        # exit_Button.place(x=5,y=170, width=287, height=50)
#                                                            END OF UI DESIGN
#===========================================================================================================================================#
#############################################################################################################################################
#===========================================================================================================================================#
#                                                      BUTTON IMPLEMENTATION FUNCTIONS
# ------------------------------------------------------------------------------------------------------------------------------------------#
    # Function for adding in the student faces to a file on the computer
    def student_faces_button(sellf):
        os.startfile("C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/Data")
    # ----------------------------------------------------------------------------------------------------------------------- #
    def train_data_button(self):
        data_dir = ("C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/Data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for face in path:
            img = Image.open(face).convert("L") # Grey Scale Image
            imageNP = np.array(img, 'uint8') # Converting gray scale image to an array of data type uint
            face_ID = int(os.path.split(face)[1].split(".")[1])

            faces.append(imageNP)
            ids.append(face_ID)
            cv2.imshow("Training", imageNP)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        # Train Classifier and Save
        train_classifier = cv2.face.LBPHFaceRecognizer_create()
        train_classifier.train(faces, ids)
        train_classifier.write("C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/Trained_Faces.xml")
        cv2.destroyWindow("Training")
        messagebox.showinfo("Training Success", "Datasets have been trained successfully.")


# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Settings(root)
    root.mainloop()