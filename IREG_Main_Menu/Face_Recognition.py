# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import numpy as np
import cv2
import mysql.connector
from time import strftime
from datetime import datetime

# Creating a class for the UI
class Face_Recognition:
    # This is the constructor of the class Face_Recognition_System
    def __init__(self, root):
        self.root = root
        self.root.geometry("1090x645+0+0")
        self.root.title("Face Recognition")
        
        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="Light Yellow", relief = RIDGE)
        mainFrame.place(x=2, y=2, width=1086, height=640) 

        # Label Frame
        Face_Recognition_lbl= Label(mainFrame, text="Face Recognition", font=("Segoe UI Variable", 45, "bold"), bg="Light Yellow", fg="Black")
        Face_Recognition_lbl.place(x=108, y=5, width=870, height=75)

        face_recognition_Button = Button(mainFrame, text="Face Recognition", cursor="hand2", command=self.face_recognition, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="Light Yellow")
        face_recognition_Button.place(x=5,y=5, width=287, height=50)
# ========================================================================================================================================= #
    #def mark_attendance(self, fetch_student_id, fetch_first_name, fetch_last_name):
    #    with open("C:/Users/utkarshjain120/Desktop/IREG-Image-Registartion-Based-Attendance-Mangement-System/Attendance.csv","r+", newline="/n") as f:
    #        myDataList = f.readlines()
    #        name_list = []

    #        for line in myDataList:
    #            entry = line.split(",")
    #            name_list.append(entry[0])
    #        if ((fetch_student_id not in name_list) and (fetch_first_name not in name_list) and (fetch_last_name not in name_list)):
    #            now = datetime.now()
    #            attendance_time = now.strftime("%d/%m/%Y")
    #            attendane_date = now.strftime("%H:%M:%S")
    #            f.writelines(f"/n{fetch_student_id},{fetch_first_name},{fetch_last_name},{attendane_date},{attendance_time},Preset")

# ========================================================================================================================================= #
    # Button Implementation
    def face_recognition(self):
        # Corresponding Functions
        #def grayscaling_image(img):
        #    pixel_array = asarray(img)

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


                my_cursor.execute("SELECT Student_ID FROM tbl_Student WHERE Student_ID=" + str(id))
                fetch_student_id = str(my_cursor.fetchone())
                fetch_student_id = "+".join(fetch_student_id)

                my_cursor.execute("SELECT First_Name FROM tbl_Student WHERE Student_ID=" + str(id))
                fetch_first_name = str(my_cursor.fetchone())
                fetch_first_name = "+".join(fetch_first_name)

                my_cursor.execute("SELECT Last_Name FROM tbl_Student WHERE Student_ID=" + str(id))
                fetch_last_name = str(my_cursor.fetchone()) 
                fetch_last_name = "+".join(fetch_last_name)

                # Confidence is the percentage of difference from the original image. Lower the confidence, the result is more 
                # accurate and vice versa
                if confidence > 50:
                    cv2.putText(img, f"Student ID: {fetch_student_id}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"First Name: {fetch_first_name}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Last Name: {fetch_last_name}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    #self.mark_attendance(fetch_student_id, fetch_first_name, fetch_last_name)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0 , 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

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
            img = video_Capture.read()
            img = recognise(img, clf, faceCascade)
            cv2.imshow("Welcome to IREG", img)

            if cv2.waitKey(1)==13:
                break
            video_Capture.release()
            cv2.destroyAllWindows()
# ========================================================================================================================================= #

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()