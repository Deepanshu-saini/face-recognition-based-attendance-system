import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import cv2,os
import csv
import pandas as pd
import datetime
import time
from function import *

global key
key = ''
def take_att():

      def TrackImages():
            check_haarcascadefile()
            assure_path_exists("Attendance/")
            assure_path_exists("StudentDetails/")
            for k in tv.get_children():
                  tv.delete(k)
            msg = ''
            i = 0
            j = 0
            recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
            exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
            if exists3:
                  recognizer.read("TrainingImageLabel\Trainner.yml")
            else:
                  mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
                  return
            harcascadePath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(harcascadePath);

            cam = cv2.VideoCapture(0)
            font = cv2.FONT_HERSHEY_SIMPLEX
            col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
            exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
            if exists1:
                  df = pd.read_csv("StudentDetails\StudentDetails.csv")
            else:
                  mess._show(title='Details Missing', message='Students details are missing, please check!')
                  cam.release()
                  cv2.destroyAllWindows()
                  window.destroy()
            while True:
                  ret, im = cam.read()
                  gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                  faces = faceCascade.detectMultiScale(gray, 1.2, 5)
                  for (x, y, w, h) in faces:
                        cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                        serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
                        if (conf < 50):
                              ts = time.time()
                              date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                              timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                              aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                              ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                              ID = str(ID)
                              ID = ID[1:-1]
                              bb = str(aa)
                              bb = bb[2:-2]
                              attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]

                        else:
                              Id = 'Unknown'
                              bb = str(Id)
                              cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
                  cv2.imshow('Taking Attendance', im)
                  if (cv2.waitKey(1) == ord('q')):
                        break
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
            exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")
            if exists:
                  with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
                        writer = csv.writer(csvFile1)
                        writer.writerow(attendance)
                  csvFile1.close()
            else:
                  with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
                        writer = csv.writer(csvFile1)
                        writer.writerow(col_names)
                        writer.writerow(attendance)
                  csvFile1.close()
            with open("Attendance\Attendance_" + date + ".csv", 'r') as csvFile1:
                  reader1 = csv.reader(csvFile1)
                  for lines in reader1:
                        i = i + 1
                        if (i > 1):
                              if (i % 2 != 0):
                                    iidd = str(lines[0]) + '   '
                                    tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
            csvFile1.close()
            cam.release()
            cv2.destroyAllWindows()

      def check_haarcascadefile():
            exists = os.path.isfile("haarcascade_frontalface_default.xml")
            if exists:
                  pass
            else:
                  mess._show(title='Some file missing', message='Please contact us for help')
                  window.destroy()

      ts = time.time()
      date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
      day,month,year=date.split("-")

      mont={'01':'January',
            '02':'February',
            '03':'March',
            '04':'April',
            '05':'May',
            '06':'June',
            '07':'July',
            '08':'August',
            '09':'September',
            '10':'October',
            '11':'November',
            '12':'December'
            }

      window = tk.Tk()
      window.geometry("720x720")
      window.resizable(False,False)
      window.title("Attendance System")
      window.configure(background='#262523')

      frame1 = tk.Frame(window, bg="#00aeff")
      frame1.place(relx=0.11, rely=0.17, relwidth=0.7, relheight=0.80)

      message3 = tk.Label(window, text="Take Attendance" ,fg="white",bg="#262523" ,width=55 ,height=1,font=('times', 29, ' bold '))
      message3.place(relx=-0.4, rely=0)

      head1 = tk.Label(frame1, text="                       For Already Registered                       ", fg="black",bg="#3ece48" ,font=('times', 17, ' bold ') )
      head1.place(x=0,y=0)


      lbl3 = tk.Label(frame1, text="Attendance",width=20  ,fg="black"  ,bg="#00aeff"  ,height=1 ,font=('times', 17, ' bold '))
      lbl3.place(x=100, y=115)


      menubar = tk.Menu(window,relief='ridge')
      filemenu = tk.Menu(menubar,tearoff=0)
      filemenu.add_command(label='Contact Us', command = contact)
      filemenu.add_command(label='Exit',command = window.destroy)
      menubar.add_cascade(label='Help',font=('times', 29, ' bold '),menu=filemenu)


      tv= ttk.Treeview(frame1,height =13,columns = ('name','date','time'))
      tv.column('#0',width=82)
      tv.column('name',width=130)
      tv.column('date',width=133)
      tv.column('time',width=133)
      tv.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
      tv.heading('#0',text ='ID')
      tv.heading('name',text ='NAME')
      tv.heading('date',text ='DATE')
      tv.heading('time',text ='TIME')

      scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
      scroll.grid(row=2,column=4,padx=(0,100),pady=(150,0),sticky='ns')
      tv.configure(yscrollcommand=scroll.set)

      trackImg = tk.Button(frame1, text="Take Attendance", command=TrackImages  ,fg="black"  ,bg="yellow"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
      trackImg.place(x=30,y=50)
      quitWindow = tk.Button(frame1, text="Quit", command=window.destroy  ,fg="black"  ,bg="red"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
      quitWindow.place(x=30, y=450)


      window.configure(menu=menubar)
      window.mainloop()