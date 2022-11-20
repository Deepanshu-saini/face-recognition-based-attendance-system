import tkinter as tk
from gui import *
from gui1 import *

window = tk.Tk()
window.geometry("720x720")
window.resizable(False,False)
window.title("Attendance System")
window.configure(background='#262523')
frame2 = tk.Frame(window, bg="#00aeff")
frame2.place(relx=0.2, rely=0.18, relwidth=0.7, relheight=0.5)

message3 = tk.Label(window, text="Welcome to Attendance system" ,fg="white",bg="#262523" ,width=55 ,height=1,font=('times', 29, ' bold '))
message3.place(relx=-0.3, rely=0)
head2 = tk.Label(frame2, text="                          Attendance System                          ", fg="black",bg="#3ece48" ,font=('times', 17, ' bold ') )
head2.grid(row=0,column=0)
tImg = tk.Button(frame2, text="Take Attendance", command=take_att  ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
tImg.place(x=30, y=100)
trImg = tk.Button(frame2, text="Add Profile", command=A_profile ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trImg.place(x=30, y=180)
window.mainloop()