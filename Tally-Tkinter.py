from cProfile import label
from textwrap import fill
from tkinter import *
from tkinter import ttk
from cProfile import label
from dataclasses import field
from textwrap import fill
from tkinter import *
from tkinter import ttk

from colorama import Style

top = Tk()


w = top.winfo_screenwidth()
h = top.winfo_screenheight()
top.geometry("%dx%d" % (w, h))

#function on trial balance

def home():
    name = Label(top, text="Select Stock Item", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=0, y=60, width=1866, height=13)
    home = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1309, height=600)
        
    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=444, height=900)

    menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=863, y=250, width=252, height=400)

    menuname = Label(top,text="Banking", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='center').place(x=863, y=250, width=252, height=19)

    menuname = Label(top,text="CHEQUE", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 7 '), anchor='center').place(x=900, y=288, width=70, height=19)

    menuname = Label(top,text="STATEMENTS", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 7 '), anchor='center').place(x=900, y=470, width=70, height=19)


    b10 = Button(top,text = "Cheque Printing",command=trialbalance,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.390,relwidth=.148)
    b11 = Button(top,text = "Cheque Register",command=banking,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.500,relwidth=.148)
    b12 = Button(top,text = "Balance Sheet",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.600,relwidth=.148)
    b13 = Button(top,text = "Quit",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.640,relwidth=.148)



def banking():
    name = Label(top, text="Select Stock Item", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=0, y=60, width=1866, height=13)
    home = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1309, height=600)
        
    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=444, height=900)

    menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=863, y=250, width=252, height=400)

    menuname = Label(top,text="Gateway of Tally", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='center').place(x=863, y=250, width=252, height=19)

    menuname = Label(top,text="TRANSACTIONS", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 7 '), anchor='center').place(x=900, y=288, width=70, height=19)

    menuname = Label(top,text="UTILITIES", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 7 '), anchor='center').place(x=900, y=380, width=70, height=19)

    menuname = Label(top,text="REPORTS", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 7 '), anchor='center').place(x=900, y=470, width=70, height=19)


    b10 = Button(top,text = "Day BooK",command=trialbalance,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.390,relwidth=.148)
    b11 = Button(top,text = "BaNking",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.500,relwidth=.148)
    b12 = Button(top,text = "Balance Sheet",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.600,relwidth=.148)
    b13 = Button(top,text = "Quit",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.640,relwidth=.148)






def trialbalance():
    trialbalanc = Label(top, text="Select Stock Item", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    trialbalanceform = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1298, height=604)
    b4 = Button(top, text="x", command=home, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    Label1 = Label(top,text='Name of item',borderwidth="0", width=3, background="#faf8d7",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ",anchor="n",bd=2,)
    Label1.place(relx=0.35, rely=0.09, relheight=0.10, relwidth=0.150)
    Entry1 = Entry(top,width=8,borderwidth="3",bg="#f7d065")
    Entry1.place(relx=0.36, rely=0.14, relheight=0.03, relwidth=0.132)


    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=315, height=900)

    menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=504, y=180, width=300, height=400)

    menuname = Label(top,text="List Of Stock Items", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='center').place(x=504, y=160, width=300, height=19)



    b9 = Button(top,text = "Create",command=create,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.450, rely=0.220,relwidth=0.070,anchor="nw")
    b10 = Button(top,text = "Pen",command=trialbalance,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.250,relwidth=.148)
    b11 = Button(top,text = "Soap",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.280,relwidth=.148)
    b12 = Button(top,text = "Shampoo",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.310,relwidth=.148)
    b13 = Button(top,text = "Cream",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.340,relwidth=.148)
    


def create():
    trialbalanc = Label(top, text="Create", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    trialbalanceform = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1298, height=604)
    b4 = Button(top, text="x", command=home, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    Label1 = Label(top,text='',borderwidth="0", width=3, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ",anchor="n",bd=2,)
    Label1.place(x=0,y=75, height=600, width=900)

    name = Label(top, text = "Name",fg='black',bg='white').place(x = 10,y = 100,width=60,height=30)
    alias = Label(top, text = "(alias)",fg='black',bg='white').place(x = 10, y =140,width=60,height=30)  
    
    e1 = Entry(top,fg='black',bg='#ffeb7d').place(x = 80, y = 100,width=300,height=30)
    e2 = Entry(top,fg='black',bg='white').place(x = 80, y = 140,width=300,height=30)  

   
  



# NavBar Start
name = Label(top, text="TallyPrime", fg='pink', bg='#3a646b', font=(
    "Arial", 13), anchor='w').place(x=0, y=0, width=1600, height=60)
name = Label(top, text="Gate WayOf Tally", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=0, y=60, width=1600, height=13)
name = Label(top, text="MANAGE", fg='#00c8ff', bg='#3a646b', font=(
    'Arial 9 underline'), anchor='w').place(x=110, y=9, width=206, height=10)

b1 = Button(top, text="K:Company", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=120, y=33)
b2 = Button(top, text="Y:Data", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=275, y=33)
b3 = Button(top, text="Z:Exchange", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=395, y=33)
b4 = Button(top, text="  G:Go To  ", activeforeground="black", activebackground="white",
            fg='black', bg='white', borderwidth=0, underline=2, font=('Arial 10 bold'),).place(x=565, y=33)
b5 = Button(top, text="O:Import", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=825, y=33)
b6 = Button(top, text="E:Export", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=925, y=33)
b7 = Button(top, text="M:E-mail", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=1025, y=33)
b8 = Button(top, text="P:Print", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=1127, y=33)
b9 = Button(top, text="F1:Help", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=1227, y=33)

# NavBar End



name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=555, height=900)

menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=863, y=250, width=252, height=400)

menuname = Label(top,text="Gateway of Tally", fg='white', bg='#0851a8', borderwidth=2, font=(
    'Arial 9 '), anchor='center').place(x=863, y=250, width=252, height=19)

menuname = Label(top,text="TRANSACTIONS", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
    'Arial 7 '), anchor='center').place(x=900, y=288, width=70, height=19)

menuname = Label(top,text="UTILITIES", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
    'Arial 7 '), anchor='center').place(x=900, y=380, width=70, height=19)

menuname = Label(top,text="REPORTS", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
    'Arial 7 '), anchor='center').place(x=900, y=470, width=70, height=19)


b10 = Button(top,text = "Day BooK",command=trialbalance,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.390,relwidth=.148)
b11 = Button(top,text = "BaNking",command=banking,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.500,relwidth=.148)
b12 = Button(top,text = "Balance Sheet",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.600,relwidth=.148)
b13 = Button(top,text = "Quit",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.640,relwidth=.148)
top.mainloop()







def selected_groups():
        f1.destroy()
        f3.destroy()
        sgaf1.destroy()
        Canvas2.destroy()
        global selected_groups_frame
        selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
        selected_groups_frame.place(x=10,y=35,width=1300,height=650)

        f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=0)
        f11.grid(row=1,column=0,columnspan=3,ipadx=200)
        l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,width=23,height=7)
        l1f1.pack(fill=X)
        f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f12.place(x=613,y=0,width=682,height=80)
        l1f2=Label(f12,text="PRODUCT NAME",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
        l1f2.place(x=305,y=10,anchor="center")
        l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
        l1f3.place(x=305,y=30,anchor="center")
        l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
        l1f4.place(x=305,y=50,anchor="center")

        tree0=ttk.Treeview(selected_groups_frame, column=("c1", "c2","c3","c4","c5","c6","c7"), show='headings',height=22)

        tree0.column("#1", anchor=tk.W,width=610)

        tree0.column("#2", anchor=tk.W,width=110)

        tree0.column("#3",anchor=tk.W,width=110)

        tree0.column("#4", anchor=tk.W,width=120)

        tree0.column("#5", anchor=tk.W,width=110)

        tree0.column("#6", anchor=tk.W,width=110)

        tree0.column("#7", anchor=tk.W,width=122)


        tree0.place(x=1,y=139)

        tree0.insert("",'end',values=("C-Name","12 BTL","13","14","15","16","17"))
        f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f14.place(x=614,y=81,width=340,height=58)
        l1f5=Label(f14,text="INWARDS",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
        l1f5.place(x=0,y=0,anchor="nw")
        l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f6.place(x=0,y=30,anchor="nw")
        l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f7.place(x=110,y=30,anchor="nw")
        l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f8.place(x=225,y=30,anchor="nw")



        f15=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f15.place(x=955,y=81,width=340,height=58)
        l2f5=Label(f15,text="OUTWARDS",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
        l2f5.place(x=0,y=0,anchor="nw")
        l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f6.place(x=0,y=30,anchor="nw")
        l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f7.place(x=110,y=30,anchor="nw")
        l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f8.place(x=225,y=30,anchor="nw")
        f18=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f18.place(x=0,y=598,width=607,height=48)
        l5f6=Label(f18,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l5f6.place(x=1,y=0,anchor="nw")

        f19=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f19.place(x=610,y=598,width=340,height=48)
        l6f6=Label(f19,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l6f6.place(x=0,y=0,anchor="nw")

        f20=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f20.place(x=950,y=598,width=345,height=48)
        l7f6=Label(f20,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l7f6.place(x=0,y=0,anchor="nw")







def create():
    trialbalanc = Label(top, text="Create", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    trialbalanceform = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1298, height=604)
    b4 = Button(top, text="x", command=home, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    Label1 = Label(top,text='',borderwidth="0", width=3, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ",anchor="n",bd=2,)
    Label1.place(x=0,y=75, height=600, width=900)

    name = Label(top, text = "Name",fg='black',bg='white').place(x = 10,y = 100,width=60,height=30)
    alias = Label(top, text = "(alias)",fg='black',bg='white').place(x = 10, y =140,width=60,height=30)  
    
    e1 = Entry(top,fg='black',bg='#ffeb7d').place(x = 80, y = 100,width=300,height=30)
    e2 = Entry(top,fg='black',bg='white').place(x = 80, y = 140,width=300,height=30)  

    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.31, relheight=0, relwidth=0.845)

    separator = ttk.Separator(top, orient='vertical')
    separator.place(relx=0.40, rely=0.31, relheight=0.490, relwidth=0)


   
    name2 = Label(top, text = "Under",fg='black',bg='white').place(x = 10,y = 300,width=60,height=30)
    name3 = Label(top, text = "Units",fg='black',bg='white').place(x = 10,y = 340,width=60,height=30)
    b14 = Button(top,text = "Primary",command=listofgroup,activeforeground = "black", activebackground = "#ffeb7d",bg='#ffeb7d',borderwidth=0,font=('Arial 10')).place(relx=0.200, rely=0.360,relwidth=.198)
    b15 = Button(top,text = "Not Applicable",activeforeground = "black", activebackground = "#ffeb7d",bg='#ffeb7d',borderwidth=0,font=('Arial 10')).place(relx=0.200, rely=0.400,relwidth=.198)
    

    name3 = Label(top, text = "Statuatary Details",fg='black',bg='white').place(x = 625,y = 300,width=100)
    separator = ttk.Separator(top, orient='vertical')
    separator.place(x = 625,y = 325,width=100)


    name4 = Label(top, text = "GST Applicable",fg='black',bg='white').place(x = 625,y = 330,width=100)
    top.option_add('*TCombobox*Listbox*Background', ebg)
    top.option_add('*TCombobox*Listbox*Foreground', fg)
    top.option_add('*TCombobox*Listbox*selectBackground', fg)
    top.option_add('*TCombobox*Listbox*selectForeground', ebg)
    course=['Applicable','Not Applicable','Undenied']
    cmb=ttk.Combobox(state="readonly",value=course,width=50,height=30)
    
    cmb.place(x=870,y=330)
    style.map('TCombobox', fieldbackground=[('readonly', ebg)])
    style.map('TCombobox', selectbackground=[('readonly', ebg)])
    style.map('TCombobox', selectforeground=[('readonly', fg)])
    style.map('TCombobox', background=[('readonly', ebg)])
    style.map('TCombobox', foreground=[('readonly', fg)])

    name5 = Label(top, text = "Types Of Supply",fg='black',bg='white').place(x = 625,y = 370,width=100)
    top.option_add('*TCombobox*Listbox*Background', ebg)
    top.option_add('*TCombobox*Listbox*Foreground', fg)
    top.option_add('*TCombobox*Listbox*selectBackground', fg)
    top.option_add('*TCombobox*Listbox*selectForeground', ebg)
    course=['Goods','Services']
    cmb=ttk.Combobox(state="readonly",value=course,width=50,height=30)
    
    cmb.place(x=870,y=370)
    style.map('TCombobox', fieldbackground=[('readonly', ebg)])
    style.map('TCombobox', selectbackground=[('readonly', ebg)])
    style.map('TCombobox', selectforeground=[('readonly', fg)])
    style.map('TCombobox', background=[('readonly', ebg)])
    style.map('TCombobox', foreground=[('readonly', fg)])

    name6 = Label(top, text = "Rate Of Duty (eg 5)",fg='black',bg='white').place(x = 625,y = 410,width=120)
    e5 = Entry(top,fg='black',bg='#ffeb7d').place(x = 870, y = 410,width=200,height=30)






def item_values():
    
    global item_nm
    item_nm=Frame(Canvas1,height=200,width=1308,bg="white",relief=RAISED,bd=2)

    item_nm.place(x=0,y=21)
    lb1=Label(item_nm,text="Stock Item:",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    lb1.place(x=0,y=0,anchor="nw")
    lb2=Label(item_nm,text="Item Name",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    lb2.place(x=80,y=0,anchor="nw")
    lb3=Label(item_nm,text="Inwards under ledger:",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    lb3.place(x=0,y=20,anchor="nw")
    lb4=Label(item_nm,text="Item Name",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    lb4.place(x=150,y=20,anchor="nw")
    lb5=Label(item_nm,text="for apr-10-22",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    lb5.place(x=1200,y=0,anchor="nw")
    



    global item_val
    item_val=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
    item_val.place(x=0,y=70,width=1308,height=650)
    global tree
    tree = ttk.Treeview(item_val, column=("c1", "c2", "c3","c4", "c5", "c6","c7", "c8"), show='headings', height=650)

    tree.column("#1", anchor=tk.CENTER,width=50)

    tree.heading("#1", text="Date")

    tree.column("#2", anchor=tk.CENTER,width=830)

    tree.heading("#2", text="Perticulars")

    tree.column("#3", anchor=tk.CENTER,width=70)

    tree.heading("#3", text="Quantity")

    tree.column("#4", anchor=tk.CENTER,width=70)

    tree.heading("#4", text="Basic Rate")

    tree.column("#5", anchor=tk.CENTER,width=70)

    tree.heading("#5", text="Basic value")

    tree.column("#6", anchor=tk.CENTER,width=70)

    tree.heading("#6", text="Added cost")

    tree.column("#7", anchor=tk.CENTER,width=70)

    tree.heading("#7", text="Total value")

    tree.column("#8", anchor=tk.CENTER,width=70)

    tree.heading("#8", text="Eff.rate")
    tree.pack()
    tree.bind("<Double-1>",OnDoubleClick)
    




    horizontal =Frame(item_val, bg='white', height=100,width=1308)
    horizontal.place(x=0, y=520)
    horizontal1 =Frame(item_val, bg='black', height=1,width=1308)
    horizontal1.place(x=0, y=520)
    horizontal1 =Frame(item_val, bg='black', height=1,width=1308)
    horizontal1.place(x=0, y=545)
    l4f6=Label(horizontal,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f6.place(x=0,y=5,anchor="nw")

    l4f11=Label(horizontal,text="10 Nos",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f11.place(x=900,y=5,anchor="nw")
    l4f10=Label(horizontal,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f10.place(x=1000,y=5,anchor="nw")
    l4f9=Label(horizontal,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f9.place(x=1060,y=5,anchor="nw")
    l4f8=Label(horizontal,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f8.place(x=1130,y=5,anchor="nw")
    l4f7=Label(horizontal,text="1000",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f7.place(x=1190,y=5,anchor="nw")
    l4f8=Label(horizontal,text="10000",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f8.place(x=1250,y=5,anchor="nw")   