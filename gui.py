import tkinter as tk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
from function import *

def A_profile():


    def clear():
        txt.delete(0, 'end')
        res = "1)Take Images  >>>  2)Save Profile"
        message1.configure(text=res)


    def clear2():
        txt2.delete(0, 'end')
        res = "1)Take Images  >>>  2)Save Profile"
        message1.configure(text=res)

    def check_haarcascadefile():
        exists = os.path.isfile("haarcascade_frontalface_default.xml")
        if exists:
            pass
        else:
            mess._show(title='Some file missing', message='Please contact us for help')
            window.destroy()

    def TakeImages():
        check_haarcascadefile()
        columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
        assure_path_exists("StudentDetails/")
        assure_path_exists("TrainingImage/")
        serial = 0
        exists = os.path.isfile("StudentDetails\StudentDetails.csv")
        if exists:
            with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                    serial = serial + 1
            serial = (serial // 2)
            csvFile1.close()
        else:
            with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(columns)
                serial = 1
            csvFile1.close()
        Id = (txt.get())
        name = (txt2.get())
        if ((name.isalpha()) or (' ' in name)):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            sampleNum = 0
            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # incrementing sample number
                    sampleNum = sampleNum + 1
                    # saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])
                    # display the frame
                    cv2.imshow('Taking Images', img)
                # wait for 100 miliseconds
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum > 100:
                    break
            cam.release()
            cv2.destroyAllWindows()
            res = "Images Taken for ID : " + Id
            row = [serial, '', Id, '', name]
            with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            message1.configure(text=res)
        else:
            if (name.isalpha() == False):
                res = "Enter Correct name"
                message.configure(text=res)

    def TrainImages():
        check_haarcascadefile()
        assure_path_exists("TrainingImageLabel/")
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        faces, ID = getImagesAndLabels("TrainingImage")
        try:
            recognizer.train(faces, np.array(ID))
        except:
            mess._show(title='No Registrations', message='Please Register someone first!!!')
            return
        recognizer.save("TrainingImageLabel\Trainner.yml")
        res = "Profile Saved Successfully"
        message1.configure(text=res)
        message.configure(text='Total Registrations till now  : ' + str(ID[0]))


    def getImagesAndLabels(path):
        # get the path of all the files in the folder
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        # create empth face list
        faces = []
        # create empty ID list
        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            ID = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(ID)
        return faces, Ids
    def psw():
        assure_path_exists("TrainingImageLabel/")
        exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
        if exists1:
            tf = open("TrainingImageLabel\psd.txt", "r")
            key = tf.read()
        else:
            new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
            if new_pas == None:
                mess._show(title='No Password Entered', message='Password not set!! Please try again')
            else:
                tf = open("TrainingImageLabel\psd.txt", "w")
                tf.write(new_pas)
                mess._show(title='Password Registered', message='New password was registered successfully!!')
                return
        password = tsd.askstring('Password', 'Enter Password', show='*')
        if (password == key):
            TrainImages()
        elif (password == None):
            pass
        else:
            mess._show(title='Wrong Password', message='You have entered wrong password')

    window = tk.Tk()
    window.geometry("720x720")
    window.resizable(False,False)
    window.title("Attendance System")
    window.configure(background='#262523')

    frame2 = tk.Frame(window, bg="#00aeff")
    frame2.place(relx=0.2, rely=0.18, relwidth=0.7, relheight=0.80)

    message3 = tk.Label(window, text="Enter details" ,fg="white",bg="#262523" ,width=55 ,height=1,font=('times', 29, ' bold '))
    message3.place(relx=-0.3, rely=0)

    head2 = tk.Label(frame2, text="                       For New Registrations                       ", fg="black",bg="#3ece48" ,font=('times', 17, ' bold ') )
    head2.grid(row=0,column=0)

    lbl = tk.Label(frame2, text="Enter ID",width=20  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold ') )
    lbl.place(x=80, y=55)

    txt = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold '))
    txt.place(x=30, y=88)

    lbl2 = tk.Label(frame2, text="Enter Name",width=20  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
    lbl2.place(x=80, y=140)

    txt2 = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold ')  )
    txt2.place(x=30, y=173)

    message1 = tk.Label(frame2, text="1)Take Images  >>>  2)Save Profile" ,bg="#00aeff" ,fg="black"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
    message1.place(x=7, y=230)

    message = tk.Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
    message.place(x=7, y=450)

    res=0
    exists = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists:
        with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                res = res + 1
        res = (res // 2) - 1
        csvFile1.close()
    else:
        res = 0
    message.configure(text='Total Registrations till now  : '+str(res))

    ##################### MENUBAR #################################

    menubar = tk.Menu(window,relief='ridge')
    filemenu = tk.Menu(menubar,tearoff=0)
    filemenu.add_command(label='Change Password', command = change_pass)
    filemenu.add_command(label='Contact Us', command = contact)
    filemenu.add_command(label='Exit',command = window.destroy)
    menubar.add_cascade(label='Help',font=('times', 29, ' bold '),menu=filemenu)

    ###################### BUTTONS ##################################

    clearButton = tk.Button(frame2, text="Clear", command=clear ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    clearButton.place(x=335, y=86)
    clearButton2 = tk.Button(frame2, text="Clear", command=clear2  ,fg="black"  ,bg="#ea2a2a"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
    clearButton2.place(x=335, y=172)    
    takeImg = tk.Button(frame2, text="Take Images", command=TakeImages  ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
    takeImg.place(x=30, y=300)
    trainImg = tk.Button(frame2, text="Save Profile", command=psw ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
    trainImg.place(x=30, y=380)

    ##################### END ######################################

    window.configure(menu=menubar)
    window.mainloop()