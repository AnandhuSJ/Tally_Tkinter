from cProfile import label
from textwrap import fill
from tkinter import *
from tkinter import ttk
from cProfile import label
from dataclasses import field
from textwrap import fill
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

    menuname = Label(top,text="Gateway of Tally", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='center').place(x=863, y=250, width=252, height=19)

    menuname = Label(top,text="TRANSACTIONS", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 7 '), anchor='center').place(x=900, y=288, width=70, height=19)

    menuname = Label(top,text="UTILITIES", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 7 '), anchor='center').place(x=900, y=380, width=70, height=19)

    menuname = Label(top,text="REPORTS", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 7 '), anchor='center').place(x=900, y=470, width=70, height=19)


    b10 = Button(top,text = "Day BooK",command=daybook,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.390,relwidth=.148)
    b11 = Button(top,text = "BaNking",command=banking,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.500,relwidth=.148)
    b12 = Button(top,text = "Balance Sheet",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.600,relwidth=.148)
    b13 = Button(top,text = "Quit",command=home,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.640,relwidth=.148)



def banking():
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
        'Arial 7 '), anchor='center').place(x=900, y=440, width=70, height=19)


    b10 = Button(top,text = "Cheque Printing",command=chequeprinting,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.390,relwidth=.148)
    b11 = Button(top,text = "Cheque Register",command=checkregister,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.420,relwidth=.148)
    b12 = Button(top,text = "PosT-dated Summary",command=Postdatedsummary,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.450,relwidth=.148)
    b13 = Button(top,text = "Deposit Slip",command=depositslip,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.560,relwidth=.148)
    b14 = Button(top,text = "Payment Advice",command=paymentadvice,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.590,relwidth=.148)
    b15 = Button(top,text = "Bank Reconciliation",command=bankreconciliation,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.630,relwidth=.148)
    b16 = Button(top,text = "Quit",command=home,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.680,relwidth=.148)




def chequeprinting():
    chequeprint = Label(top, text="Select Bank", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    chequeprintingform = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1298, height=604)
    b4 = Button(top, text="x", command=banking, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    Label1 = Label(top,text='Name of Bank',borderwidth="0", width=3, background="#faf8d7",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ",anchor="n",bd=2,)
    Label1.place(relx=0.35, rely=0.09, relheight=0.10, relwidth=0.150)
    Entry1 = Entry(top,width=8,borderwidth="3",bg="#f7d065")
    Entry1.place(relx=0.36, rely=0.14, relheight=0.03, relwidth=0.132)


    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=315, height=900)

    menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=504, y=180, width=300, height=400)

    menuname = Label(top,text="List Of Banks", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='center').place(x=504, y=160, width=300, height=19)



    b9 = Button(top,text = "Create",command=create,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.450, rely=0.220,relwidth=0.070,anchor="nw")
    b10 = Button(top,text = "All items",command=chequeprinting,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.250,relwidth=.148)
   
    

def Postdatedsummary():
    Postdatedsummar = Label(top, text="Select Bank", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    Postdatedsummaryform = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1298, height=604)
    b4 = Button(top, text="x", command=banking, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    Label1 = Label(top,text='Name of Ledger',borderwidth="0", width=3, background="#faf8d7",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ",anchor="n",bd=2,)
    Label1.place(relx=0.35, rely=0.09, relheight=0.10, relwidth=0.150)
    Entry1 = Entry(top,width=8,borderwidth="3",bg="#f7d065")
    Entry1.place(relx=0.36, rely=0.14, relheight=0.03, relwidth=0.132)


    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=315, height=900)

    menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=504, y=180, width=300, height=400)

    menuname = Label(top,text="List Of Banks", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='center').place(x=504, y=160, width=300, height=19)



    b9 = Button(top,text = "Create",command=create,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.450, rely=0.220,relwidth=0.070,anchor="nw")
    b10 = Button(top,text = "All items",command=Postdatedsummary,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.250,relwidth=.148)


def depositslip():
    deposit = Label(top, text="Select Bank", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    depositslipform = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1298, height=604)
    b4 = Button(top, text="x", command=banking, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    Label1 = Label(top,text='Name of Bank',borderwidth="0", width=3, background="#faf8d7",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ",anchor="n",bd=2,)
    Label1.place(relx=0.35, rely=0.09, relheight=0.10, relwidth=0.150)
    Entry1 = Entry(top,width=8,borderwidth="3",bg="#f7d065")
    Entry1.place(relx=0.36, rely=0.14, relheight=0.03, relwidth=0.132)


    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=315, height=900)

    menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=504, y=180, width=300, height=400)

    menuname = Label(top,text="List Of Banks", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='center').place(x=504, y=160, width=300, height=19)



    b9 = Button(top,text = "Create",command=create,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.450, rely=0.220,relwidth=0.070,anchor="nw")
    b10 = Button(top,text = "All items",command=depositslip,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.250,relwidth=.148)


def paymentadvice():
    paymentadvic = Label(top, text="Select item", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    paymentadviceform = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1298, height=604)
    b4 = Button(top, text="x", command=banking, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    Label1 = Label(top,text='Name of Ledger',borderwidth="0", width=3, background="#faf8d7",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ",anchor="n",bd=2,)
    Label1.place(relx=0.35, rely=0.09, relheight=0.10, relwidth=0.150)
    Entry1 = Entry(top,width=8,borderwidth="3",bg="#f7d065")
    Entry1.place(relx=0.36, rely=0.14, relheight=0.03, relwidth=0.132)


    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=315, height=900)

    menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=504, y=180, width=300, height=400)

    menuname = Label(top,text="List Of Ledgers", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='center').place(x=504, y=160, width=300, height=19)



    b9 = Button(top,text = "Create",command=create,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.450, rely=0.220,relwidth=0.070,anchor="nw")
    b10 = Button(top,text = "All items",command=paymentadvice,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.250,relwidth=.148)


def bankreconciliation():
    bankreconciliati = Label(top, text="Select Bank", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    bankreconciliationform = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1298, height=604)
    b4 = Button(top, text="x", command=banking, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    Label1 = Label(top,text='Name of Bank Ledger',borderwidth="0", width=3, background="#faf8d7",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ",anchor="n",bd=2,)
    Label1.place(relx=0.35, rely=0.09, relheight=0.10, relwidth=0.150)
    Entry1 = Entry(top,width=8,borderwidth="3",bg="#f7d065")
    Entry1.place(relx=0.36, rely=0.14, relheight=0.03, relwidth=0.132)


    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=315, height=900)

    menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=504, y=180, width=300, height=400)

    menuname = Label(top,text="List Of Bank Ledgers", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='center').place(x=504, y=160, width=300, height=19)



    b9 = Button(top,text = "Create",command=create,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.450, rely=0.220,relwidth=0.070,anchor="nw")
    


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

   
def LOGbranchordivision():
    global Canvas1
    Canvas1 = Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = Canvas( background="#8a8a8a", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas3
    Canvas3 = Canvas( background="white", relief="ridge").place(relx=0, rely=0.07, relheight=0.500, relwidth=.450)
    Label1 = Label(Canvas3,text='Name :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.09)
    e1=Entry(Canvas3,bg='#ffdd90').place(relx=0.25,rely=0.09,relwidth=.180)
    Label2 = Label(Canvas3,text='(alias) :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.12)
    e2=Entry(Canvas3,bg='#ffdd90').place(relx=0.25,rely=0.12,relwidth=.180)
    Label3 = Label(Canvas3,text='Under :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.18)
    Label4 = Label(Canvas3,text='◆Primary', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.10, rely=0.18)
    separator = ttk.Separator(Canvas3, orient='horizontal').place(relx=0, rely=0.23, relheight=0, relwidth=0.450)
    Label5 = Label(Canvas3,text='Nature of Group :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.26)
    Label6 = Label(Canvas3,text='Group behaves like a sub-ledger :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.31)
    Label7 = Label(Canvas3,text='Nett Debit/Credit Balances for Reporting :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.36)
    Label8 = Label(Canvas3,text='Used for calculation (for example: taxes,discounts) :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.41)
    Label9 = Label(Canvas3,text='(for sales invoice entries)', background="white",foreground="black",font="-family {Papyrus} -size 10 -weight bold ").place(relx=0.02, rely=0.46)
    Label10 = Label(Canvas3,text='Method to allocate when used in purchase invoice :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.51)
    Label11 = Label(Canvas3,text='◆Not Applicable', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.25, rely=0.51)
    # b1 = Button(Canvas2,text = "Main Location",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.13)
    b2 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=banking).place(relx=0.8, rely=0.1)


def checkregister():
    checkregisterr = Label(top, text="Cheque Register", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    checkregisterform = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1298, height=804)
    b4 = Button(top, text="x", command=banking, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    f11=Frame(top,bg="white",relief=RAISED,bd=0.5)
    f11.place(x=0,y=73,width=1298,height=100)


    l1f1=Label(f11,text="P a r t i c u l a r s",font=("Arial",11),fg="black",bg="white",anchor="w", borderwidth=0,relief=GROOVE,width=5,height=4)
    l1f1.pack(fill=X,pady=12,padx=0)

    frame=Frame(top,width=1210,)
    frame.place(x=0,y=375,width=1300)

    tablecheckregister = ttk.Treeview(frame)
    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0.40, rely=0.16, relheight=0, relwidth=0.445)

    separator = ttk.Separator(top, orient='vertical')
    separator.place(relx=0.40, rely=0.09, relheight=0.605, relwidth=0)

    separator = ttk.Separator(top, orient='vertical')
    separator.place(relx=0.55, rely=0.16, relheight=0.537, relwidth=0)

    separator = ttk.Separator(top, orient='vertical')
    separator.place(relx=0.70, rely=0.16, relheight=0.537, relwidth=0)

    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.70, relheight=0, relwidth=0.845)

    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.73, relheight=0, relwidth=0.845)



def daybook():
    daybookk = Label(top, text="Day Book", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    daybookform = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1298, height=804)
    b4 = Button(top, text="x", command=home, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    f11=Frame(top,bg="white",relief=RAISED,bd=0.5)
    f11.place(x=0,y=73,width=1298,height=100)


    l1f1=Label(f11,text="P a r t i c u l a r s",font=("Arial",11),fg="black",bg="white",anchor="w", borderwidth=0,relief=GROOVE,width=5,height=4)
    l1f1.pack(fill=X,pady=12,padx=0)

    frame=Frame(top,width=1210,)
    frame.place(x=0,y=375,width=1300)

    tabledaybook = ttk.Treeview(frame)
    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0.40, rely=0.16, relheight=0, relwidth=0.445)

    separator = ttk.Separator(top, orient='vertical')
    separator.place(relx=0.40, rely=0.09, relheight=0.605, relwidth=0)

    separator = ttk.Separator(top, orient='vertical')
    separator.place(relx=0.55, rely=0.16, relheight=0.537, relwidth=0)

    separator = ttk.Separator(top, orient='vertical')
    separator.place(relx=0.70, rely=0.16, relheight=0.537, relwidth=0)

    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.70, relheight=0, relwidth=0.845)

    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.73, relheight=0, relwidth=0.845)




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


b10 = Button(top,text = "Day BooK",command=daybook,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.390,relwidth=.148)
b11 = Button(top,text = "BaNking",command=banking,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.500,relwidth=.148)
b12 = Button(top,text = "Balance Sheet",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.600,relwidth=.148)
b13 = Button(top,text = "Quit",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.640,relwidth=.148)
top.mainloop()







