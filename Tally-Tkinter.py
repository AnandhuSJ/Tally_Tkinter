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










def movement_val(e):
    movement_values()

def movement_values():
    

    global movement_frame
    movement_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=1)
    movement_frame.place(x=10,y=35,width=1300,height=650)

    f11=Frame(movement_frame,bg="white",relief=RAISED,bd=1)
    f11.grid(row=1,column=0,columnspan=3,ipadx=200)
    l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="white",fg="black",width=33,height=7)
    l1f1.pack(fill=X)
    f12=Frame(movement_frame,bg="white",relief=RAISED,bd=1)
    f12.place(x=705,y=0,width=590,height=83)
    l1f2=Label(f12,text="PRODUCT NAME",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l1f2.place(x=305,y=10,anchor="center")
    l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f3.place(x=305,y=30,anchor="center")
    l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f4.place(x=305,y=50,anchor="center")

    f13=Frame(movement_frame,bg="white",relief=RAISED,bd=2)
    f13.place(x=0,y=142,width=1295,height=505)
    f13bt1=Label(f13,text="Movement inward",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    f13bt1.place(x=0,y=0,anchor="nw")
    f13bt2=Label(f13,text="Suppliers",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    f13bt2.place(x=10,y=30,anchor="nw")

    f14=Frame(movement_frame,bg="white",relief=RAISED,bd=1)
    f14.place(x=705,y=83,width=590,height=58)
    l1f5=Label(f14,text="Movement values",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f5.place(x=0,y=0,anchor="nw")
    l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f6.place(x=10,y=30,anchor="nw")
    l1f7=Label(f14,text="Basic Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f7.place(x=160,y=30,anchor="nw")
    l1f8=Label(f14,text="Effective rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f8.place(x=270,y=30,anchor="nw")
    l1f9=Label(f14,text="Values",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f9.place(x=400,y=30,anchor="nw")

    tree0=ttk.Treeview(f13, column=("c1", "c2","c3","c4","c5"), show='headings',height=3)

    tree0.column("#1", anchor=tk.CENTER,width=686)
    
    tree0.column("#2", anchor=tk.CENTER,width=120)

    tree0.column("#3",anchor=tk.CENTER,width=140)

    tree0.column("#4", anchor=tk.CENTER,width=140)

    tree0.column("#5", anchor=tk.CENTER,width=202)

    tree0.place(x=0,y=60)
    tree0.insert("",'end',values=("C-Name","12 BTL","13","14","15"))


    l4f6=Label(f13,text="10 Nos",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f6.place(x=706,y=150,anchor="nw")
    l4f8=Label(f13,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f8.place(x=860,y=150,anchor="nw")
    l4f7=Label(f13,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f7.place(x=990,y=150,anchor="nw")
    l4f8=Label(f13,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f8.place(x=1100,y=150,anchor="nw")

    horizontal =Frame(f13, bg='black', height=1,width=600)
    horizontal.place(x=705, y=175)
    tree0.bind("<Double-1>",supplier)




    f13bt4=Label(f13,text="Movement outwards",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    f13bt4.place(x=0,y=170,anchor="nw")
    f13bt5=Label(f13,text="Buyers",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    f13bt5.place(x=10,y=200,anchor="nw")
    tree1=ttk.Treeview(f13, column=("c1", "c2","c3","c4","c5"), show='headings',height=3)

    tree1.column("#1", anchor=tk.CENTER,width=686)

    
    tree1.column("#2", anchor=tk.CENTER,width=120)
    tree1.column("#3",anchor=tk.CENTER,width=140)

    tree1.column("#4", anchor=tk.CENTER,width=140)

    tree1.column("#5", anchor=tk.CENTER,width=202)

    tree1.place(x=0,y=230)
    tree1.insert("",'end',values=("C-Name","12 BTL","13","14","15"))

    l46=Label(f13,text="10 Nos",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l46.place(x=706,y=330,anchor="nw")
    l48=Label(f13,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l48.place(x=860,y=330,anchor="nw")
    l47=Label(f13,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l47.place(x=990,y=330,anchor="nw")
    l48=Label(f13,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l48.place(x=1100,y=330,anchor="nw")

    horizontal =Frame(f13, bg='black', height=1,width=600)
    horizontal.place(x=705, y=355)
    tree1.bind("<Double-1>",buyer)


    
# data = [
# 	["John", "Elder", 1, "123 Elder St.", "Las Vegas", "NV", "89137"],
# 	["Mary", "Smith", 2, "435 West Lookout", "Chicago", "IL", "60610"],
# 	["Tim", "Tanaka", 3, "246 Main St.", "New York", "NY", "12345"],
# 	["Erin", "Erinton", 4, "333 Top Way.", "Los Angeles", "CA", "90210"],
# 	["Bob", "Bobberly", 5, "876 Left St.", "Memphis", "TN", "34321"],
# 	["Steve", "Smith", 6, "1234 Main St.", "Miami", "FL", "12321"],
# 	["Tina", "Browne", 7, "654 Street Ave.", "Chicago", "IL", "60611"],
# 	["Mark", "Lane", 8, "12 East St.", "Nashville", "TN", "54345"],
# 	["John", "Smith", 9, "678 North Ave.", "St. Louis", "MO", "67821"],
# 	["Mary", "Todd", 10, "9 Elder Way.", "Dallas", "TX", "88948"],
# 	["John", "Lincoln", 11, "123 Elder St.", "Las Vegas", "NV", "89137"],
# 	["Mary", "Bush", 12, "435 West Lookout", "Chicago", "IL", "60610"],
# 	["Tim", "Reagan", 13, "246 Main St.", "New York", "NY", "12345"],
# 	["Erin", "Smith", 14, "333 Top Way.", "Los Angeles", "CA", "90210"],
# 	["Bob", "Field", 15, "876 Left St.", "Memphis", "TN", "34321"],
# 	["Steve", "Target", 16, "1234 Main St.", "Miami", "FL", "12321"],
# 	["Tina", "Walton", 17, "654 Street Ave.", "Chicago", "IL", "60611"],
# 	["Mark", "Erendale", 18, "12 East St.", "Nashville", "TN", "54345"],
# 	["John", "Nowerton", 19, "678 North Ave.", "St. Louis", "MO", "67821"],
# 	["Mary", "Hornblower", 20, "9 Elder Way.", "Dallas", "TX", "88948"]
	
# ]
def supplier(e):
   item_values()

def buyer(e):
    item_values()
    

