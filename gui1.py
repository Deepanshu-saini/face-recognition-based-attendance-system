import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time

global key
key = ''
def take_att():
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


      ##################### MENUBAR #################################

      menubar = tk.Menu(window,relief='ridge')
      filemenu = tk.Menu(menubar,tearoff=0)
      filemenu.add_command(label='Contact Us', command = window.destroy)
      filemenu.add_command(label='Exit',command = window.destroy)
      menubar.add_cascade(label='Help',font=('times', 29, ' bold '),menu=filemenu)

      ################## TREEVIEW ATTENDANCE TABLE ####################

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

      ###################### SCROLLBAR ################################

      scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
      scroll.grid(row=2,column=4,padx=(0,100),pady=(150,0),sticky='ns')
      tv.configure(yscrollcommand=scroll.set)

      ###################### BUTTONS ##################################
      trackImg = tk.Button(frame1, text="Take Attendance", command=window.destroy  ,fg="black"  ,bg="yellow"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
      trackImg.place(x=30,y=50)
      quitWindow = tk.Button(frame1, text="Quit", command=window.destroy  ,fg="black"  ,bg="red"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
      quitWindow.place(x=30, y=450)

      ##################### END ######################################

      window.configure(menu=menubar)
      window.mainloop()