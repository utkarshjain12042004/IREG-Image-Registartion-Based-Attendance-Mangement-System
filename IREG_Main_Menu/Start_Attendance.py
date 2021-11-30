# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import mysql.connector
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
        self.root.resizable(width=False, height=False)

############################################################################################################################################
#==========================================================================================================================================#
#                                                                UI DESIGN
# ========================================================================================================================================================
        # Main Frame: This will contain all the buttons
        self.mainFrame = Frame(bd=2, bg="Light Yellow", relief = RIDGE)
        self.mainFrame.place(x=2, y=2, width=1086, height=640) 

        # Label Frame
        Start_Attendance_lbl= Label(self.mainFrame, text="Start Attendance", font=("Segoe UI Variable", 45, "bold"), bg="Light Yellow", fg="Black")
        Start_Attendance_lbl.place(x=108, y=5, width=870, height=75)

        # Obtaining the current Date and time labels
        current_date_and_time = datetime.now()

        # Current Day Label
        Current_Day_lbl = Label(self.mainFrame, text = datetime.today().strftime("%A"), font = ("Calibri", 12, "bold"), bg = "Light Yellow", fg = "Black")
        Current_Day_lbl.place(x = 1016, y = 71, width = 65, height = 15)

        # Current date label
        Current_Date_lbl =  Label(self.mainFrame, text = current_date_and_time.strftime("%d/%m/%y"), font = ("Calibri", 12, "bold"), bg = "Light Yellow", fg = "Black")
        Current_Date_lbl.place(x = 1016, y = 91, width = 65, height = 15)

        # Current time label
        Current_Time_lbl =  Label(self.mainFrame, text = current_date_and_time.strftime("%H:%M:%S"), font = ("Calibri", 12, "bold"), bg = "Light Yellow", fg = "Black")
        Current_Time_lbl.place(x = 1016, y = 111, width = 65, height = 15) 

        # Button Frame
        Button_Frame= LabelFrame(self.mainFrame, bd=2, bg="Light Yellow", relief=RIDGE)
        Button_Frame.place(x=332, y=260, width=413, height=120)

        #======================================== Adding in the buttons ========================================#

        # Manual Attendance Method Button
        manual_attendance_method_button = Button(Button_Frame, text="Manual Attendance Method", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="Light Yellow")
        manual_attendance_method_button.place(x=5,y=5, width=400, height=50)

        # Automated Attendance Method Button
        automated_attendance_method_Button =  Button(Button_Frame, text="Automated Attendance Method", cursor="hand2", command=lambda:[ self.automated_attendance_method_button(), self.clearFrame()], font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="Light Yellow")
        automated_attendance_method_Button.place(x=5,y=60, width=400, height=50)

    
# ==Button implementations=================================================================================================================================================#
    # Clear frame function: This will get rid of all the widgets which have been previously created.
    def clearFrame(self):
        for widgets in self.mainFrame.winfo_children():
            widgets.destroy()

    # Automated Attendance Method button implementation
    def automated_attendance_method_button(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text, clf,):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbour)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0 ,255, 0), 3)
                id,predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="ireg")
                my_cursor = conn.cursor()


                my_cursor.execute("SELECT * FROM tbl_Student WHERE Student_ID=" + str(id))
                data = my_cursor.fetchall()
                fetch_student_id = data[0][0]
                fetch_first_name = data[0][1]
                fetch_last_name = data[0][2]

                # Confidence is the percentage of difference from the original image. Lower the confidence, the result is more 
                # accurate and vice versa
                if confidence > 77:
                    cv2.putText(img, f"Student ID: {fetch_student_id}", (x, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 3)
                    cv2.putText(img, f"First Name: {fetch_first_name}", (x, y-35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 3)
                    cv2.putText(img, f"Last Name: {fetch_last_name}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 3)
                    self.mark_attendance(fetch_student_id, fetch_first_name, fetch_last_name)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0 , 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (000, 000, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognise(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img


        faceCascade = cv2.CascadeClassifier("C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/Trained_Faces.xml")

        video_Capture = cv2.VideoCapture(0)

        while True:
            ret, img = video_Capture.read()
            img = recognise(img, clf, faceCascade)
            cv2.imshow("Welcome to IREG", img)

            if cv2.waitKey(1)==13:
                break
            
        video_Capture.release()
        cv2.destroyAllWindows()

    # This function will mark the students who have been recognised in the video frame as presnet. 
    def mark_attendance(self, student_id, first_name, last_name):
        with open("C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance.csv","r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []

            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])

            if ((student_id not in name_list) and (first_name not in name_list) and (last_name not in name_list)):
                now = datetime.now()
                attendance_time = now.strftime("%d/%m/%Y")
                attendance_date = now.strftime("%H:%M:%S")
                f.writelines(f"\n{student_id},{first_name},{last_name},{attendance_date},{attendance_time},Present")






# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Start_Attendance(root)
    root.mainloop()