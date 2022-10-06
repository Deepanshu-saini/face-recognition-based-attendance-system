import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import os
import csv
def A_profile():
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
    filemenu.add_command(label='Change Password', command = window.destroy)
    filemenu.add_command(label='Contact Us', command = window.destroy)
    filemenu.add_command(label='Exit',command = window.destroy)
    menubar.add_cascade(label='Help',font=('times', 29, ' bold '),menu=filemenu)

    ###################### BUTTONS ##################################

    clearButton = tk.Button(frame2, text="Clear", command=window.destroy  ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    clearButton.place(x=335, y=86)
    clearButton2 = tk.Button(frame2, text="Clear", command=window.destroy  ,fg="black"  ,bg="#ea2a2a"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
    clearButton2.place(x=335, y=172)    
    takeImg = tk.Button(frame2, text="Take Images", command=window.destroy  ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
    takeImg.place(x=30, y=300)
    trainImg = tk.Button(frame2, text="Save Profile", command=window.destroy ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
    trainImg.place(x=30, y=380)

    ##################### END ######################################

    window.configure(menu=menubar)
    window.mainloop()