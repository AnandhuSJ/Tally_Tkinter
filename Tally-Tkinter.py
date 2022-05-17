from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk

# def account():
#     global Canvas1
#     Canvas1 = tk.Canvas( background="#3a646b", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
#     Canvas1.place(relx=0, rely=0.10, relheight=0.800, relwidth=.850)


#     global Canvas2
#     Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
#     Canvas2.place(relx=0.15, rely=0.105, relheight=0.8, relwidth=0.700)

#     global Canvas3
#     Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
#     Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

def chartofaccountsgroups():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas3
    Canvas2 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    Label1 = Label(Canvas2,text='List of masters', background="white",foreground="black",font="-family {Segoe UI} -size 15 -weight bold ").place(relx=0, rely=0.07,relwidth=.100)
    b1 = Button(Canvas2,text = "Groups/Divisions",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.12)
    b2 = Button(Canvas2,text = "Capital Account",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.15)
    b3 = Button(Canvas2,text = "Reserves & Surplus",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.18)
    b4 = Button(Canvas2,text = "Current Assets",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.21)
    b5 = Button(Canvas2,text = "Bank Accounts",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.24)
    b6 = Button(Canvas2,text = "Cash in Hand",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.27)
    b7 = Button(Canvas2,text = "Deposits (Asset)",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.30)
    b8 = Button(Canvas2,text = "Loans & Advances (Asset)",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.33)
    b9 = Button(Canvas2,text = "Stock-in-Hand",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.36)
    b10 = Button(Canvas2,text = "Sundry Debtors",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.39)
    b11 = Button(Canvas2,text = "Current Liabilities",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.42)
    b12 = Button(Canvas2,text = "Duties & Taxes",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.45)
    b13 = Button(Canvas2,text = "Provisions",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.48)
    b14 = Button(Canvas2,text = "Sundry Creditors",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.51)
    b15 = Button(Canvas2,text = "Direct Expenses",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.54)
    b16 = Button(Canvas2,text = "Direct Incomes",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.57)
    b17 = Button(Canvas2,text = "Fixed Assets",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.60)
    b18 = Button(Canvas2,text = "Inderect Expenses",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.63)
    b19 = Button(Canvas2,text = "Inderect Incomes",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.66)
    b20 = Button(Canvas2,text = "Investments",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.69)
    b21 = Button(Canvas2,text = "Loans (Liability)",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.72)
    b22 = Button(Canvas2,text = "Bank OD A/c",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.75)
    b23 = Button(Canvas2,text = "Secured Loans",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.78)
    b24 = Button(Canvas2,text = "Unsecured Loans",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.81)
    b21 = Button(Canvas2,text = "Misc Expenses (ASSET)",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.84)
    b21 = Button(Canvas2,text = "Purchase Accounts",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.87)
    b21 = Button(Canvas2,text = "Sales Accounts",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.90)
    b21 = Button(Canvas2,text = "Suspense A/c",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.93)
   


def banking():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white").place(relx=0.850, rely=0.07, relheight=0.9, relwidth=0.150)

    global canvas4
    Canvas4 = tk.Canvas( background="lightblue", relief="sunken").place(relx=0.35, rely=0.3, relheight=0.500, relwidth=.200)

    Label1 = Label(Canvas3,text='Banking', background="#3385ff",foreground="#ffffff",font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.35, rely=0.29,relwidth=.200)
    # Label2 = Label(Canvas3,text='Accounting masters', background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.550, rely=0.450,relwidth=.150)
    # Label3 = Label(Canvas3,text='Inventory masters', background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.550, rely=0.402,relwidth=.150)
    Label2 = Label(Canvas3,text='CHEQUE', background="Lightblue",foreground="#52a0ff",font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.35, rely=0.33,relwidth=.200)
    b1 = Button(Canvas3,text = "Cheque Printing",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10'),command=chartofaccountsgroups).place(relx=0.35, rely=0.36,relwidth=.200)
    b2 = Button(Canvas3,text = "Cheque Register",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10')).place(relx=0.35, rely=0.39,relwidth=.200)
    b3 = Button(Canvas3,text = "PosT-dated Summary",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10')).place(relx=0.35, rely=0.42,relwidth=.200)
    Label3 = Label(Canvas3,text='STATEMENTS', background="Lightblue",foreground="#52a0ff",font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.35, rely=0.46,relwidth=.200)
    b4 = Button(Canvas3,text = "Deposit Slip",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10')).place(relx=0.35, rely=0.50,relwidth=.200)
    b5 = Button(Canvas3,text = "Payment Advice",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10')).place(relx=0.35, rely=0.53,relwidth=.200)
    b6 = Button(Canvas3,text = "Bank Reconciliation",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10')).place(relx=0.35, rely=0.58,relwidth=.200)
    b7 = Button(Canvas3,text = "Quit",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10')).place(relx=0.35, rely=0.65,relwidth=.200)

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

global Canvas1
Canvas1 = tk.Canvas( background="#ffffff", relief="ridge")
Canvas1.place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

global Canvas3
Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas3.place(relx=0.850, rely=0.07, relheight=0.9, relwidth=0.150)

global canvas4
Canvas4 = tk.Canvas( background="#ffffff", relief="ridge")
Canvas4.place(relx=0.550, rely=0.4, relheight=0.400, relwidth=.150)

name = Label(screen, text="TallyPrime", fg='pink',bg='#3a646b',font=("Arial", 13),anchor='w').place(x = 1,y = 0)

b1 = Button(screen,text = "Company",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=120,y=33)
b2 = Button(screen,text = "Data",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=275,y=33)
b3 = Button(screen,text = "Exchange",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=395,y=33)
b4 = Button(screen,text = " Go To ",activeforeground = "black", activebackground = "white",fg='black',bg='white',borderwidth=0,underline=2,font=('Arial 10 bold'),).place (x=565,y=33)
b5 = Button(screen,text = "Import",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=825,y=33)
b6 = Button(screen,text = "Export",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=925,y=33)
b7 = Button(screen,text = "E-mail",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=1025,y=33)
b8 = Button(screen,text = "Print",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=1127,y=33)
b9 = Button(screen,text = "Help",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=1227,y=33)

Label6 = Label(screen,text='Gateway of tally', background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.550, rely=0.400,relwidth=.150)
Label2 = Label(screen,text='TRANSACTIONS',foreground="#00254a",font="-family {Segoe UI=} -size 10 -weight normal ").place(relx=0.551, rely=0.450,relwidth=.148)
b10 = Button(screen,text = "Day BooK",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.480,relwidth=.148)
Label3 = Label(screen,text='UTILITIES',foreground="#00254a",font="-family {Segoe UI=} -size 10 -weight normal ").place(relx=0.551, rely=0.540,relwidth=.148)
b11 = Button(screen,text = "BaNking",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10'),command=banking).place(relx=0.551, rely=0.580,relwidth=.148)
Label4 = Label(screen,text='REPORTS',foreground="#00254a",font="-family {Segoe UI=} -size 10 -weight normal ").place(relx=0.551, rely=0.620,relwidth=.148)
b12 = Button(screen,text = "Balance Sheet",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.660,relwidth=.148)
b13 = Button(screen,text = "Quit",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.700,relwidth=.148)

# Chart of accounts section


screen.mainloop()