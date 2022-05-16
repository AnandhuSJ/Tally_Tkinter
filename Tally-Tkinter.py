from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox

from tkinter import ttk


def account():
    global Canvas1
    Canvas1 = tk.Canvas( background="#3a646b", insertbackground="black", relief="ridge",
                                selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.10, relheight=0.800, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",
                            selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.15, rely=0.105, relheight=0.8, relwidth=0.700)

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",
                                selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

    




global screen
screen=Tk()
w=screen.winfo_screenwidth()
h=screen.winfo_screenheight()
screen.geometry("%dx%d" %(w,h))
        
screen.title("Tally")
# p1 = PhotoImage(file='D:\\Tally\\front.jpg')
# screen.iconphoto(True, p1)
screen.configure(background="#3a646b")
screen.configure(cursor="arrow")

          
name = Label(screen, text="TallyPrime", fg='pink',bg='#3a646b',font=("Arial", 13),anchor='w').place(x = 1,y = 0)
name = Label(screen, text="Gate WayOf Tally", fg='black',bg='#00c8ff',font=('Arial 7 bold'),anchor='w').place(x = 1,y = 60)
name = Label(screen, text="MANAGE" ,fg='#00c8ff',bg='#3a646b',font=('Arial 9 underline'),anchor='w').place(x = 110,y = 9)


b1 = Button(screen,text = "K:Company",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=120,y=33)
b2 = Button(screen,text = "Y:Data",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=275,y=33)
b3 = Button(screen,text = "Z:Exchange",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=395,y=33)
b4 = Button(screen,text = "  G:Go To  ",activeforeground = "black", activebackground = "white",fg='black',bg='white',borderwidth=0,underline=2,font=('Arial 10 bold'),).place (x=565,y=33)
b5 = Button(screen,text = "O:Import",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=825,y=33)
b6 = Button(screen,text = "E:Export",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=925,y=33)
b7 = Button(screen,text = "M:E-mail",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=1025,y=33)
b8 = Button(screen,text = "P:Print",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=1127,y=33)
b9 = Button(screen,text = "F1:Help",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=1227,y=33)

global Canvas1
Canvas1 = tk.Canvas( background="#ffffff", relief="ridge")
Canvas1.place(relx=0, rely=0.07, relheight=0.800, relwidth=.850)
Label5 = Label(Canvas1,text='Select Company',borderwidth="0", width=5, background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)




# global Canvas2
# Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
# Canvas2.place(relx=0.250, rely=0.300, relheight=0.500, relwidth=0.500)

global Canvas3
Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas3.place(relx=0.850, rely=0.07, relheight=0.8, relwidth=0.150)
screen.mainloop()