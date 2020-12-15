from tkinter import *
from tkinter import ttk

class EMI_CAL:
    def __init__(self, calculator):
        self.font = ("Times New Roman", 12, "bold")
        self.P = Label(calculator, text="Loan Amount", font=self.font, relief=SOLID)
        self.R = Label(calculator, text="Rate of interest", font=self.font, relief=SOLID)
        self.n = Label(calculator, text="No. of years", font=self.font, relief=SOLID)
        self.E = Label(calculator, text="EMI", font=self.font, relief=SOLID)
        self.I = Label(calculator, text="Total Payable Interest", font=self.font, relief=SOLID)
        self.T = Label(calculator, text="Total Payable Amount", font=self.font, relief=SOLID)
        self.p = Entry(bd=3)
        self.r = Entry(bd=3)
        self.N = Entry(bd=4)
        self.e = Entry(bd=4)
        self.i = Entry(bd=4)
        self.t = Entry(bd=4)
        self.b1 = Button(calculator, text='Calculate', font=self.font, relief=SOLID)#, command=self.Calculate)
        # self.b1 = Button.bind('< b1 >', self.Calculate)
        self.b1.bind('<Button-1>', self.Calculate)
        self.P.place(x=100, y=50)
        self.p.place(x=270, y=50)
        self.R.place(x=100, y=100)
        self.r.place(x=270, y=100)
        self.n.place(x=100, y=150)
        self.N.place(x=270, y=150)
        self.b1.place(x=220, y=200)
        self.E.place(x=100, y=250)
        self.e.place(x=270, y=250)
        self.I.place(x=100, y=300)
        self.i.place(x=270, y=300)
        self.T.place(x=100, y=350)
        self.t.place(x=270, y=350)
        

    def Calculate(self, event):
        """
        calculates the EMI for a given period of time and rate of interest
        P -> Loan Amount
        R -> Rate of interest
        n -> # years
        x = (1 + (R/1200))
        """
        self.e.delete(0, 'end')
        self.i.delete(0, 'end')
        self.t.delete(0, 'end')
        P = float(self.p.get())
        R = float(self.r.get())
        n = float(self.N.get())
        try:
            x = (1 + (R/1200))
            m = x**(12*n)
            E = (P * m * (x-1)) / (m - 1)
            I = E * n
            T = P + I
            self.e.insert(END, str(E))
            self.i.insert(END, str(I))
            self.t.insert(END, str(T))
            # l.config(text=E, font=("Times New Roman", 12, "bold"), relief=SUNKEN)
            # l.configure(background="white")
        except:
            pass


root = Tk()

myRoot = EMI_CAL(root)
root.title("EMI Calculator") #, font=("Times New Roman", 12, "bold")
root.geometry("600x420+50+70")
root.configure(background="Lightblue")

root.mainloop()



# # Principal loan amount
# frame1 = Frame(root)
# frame1.pack()

# # Rate of interest
# frame2 = Frame(root)
# frame2.pack()

# # Number of years
# frame3 = Frame(root)
# frame3.pack()

# # output frame
# frame4 = Frame(root)
# frame4.pack()

# Nextframe = Frame(root)
# Nextframe.pack( side = BOTTOM )
# # relief must be -> flat, groove, raised, ridge, solid, or sunken

# # -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
# E = Label(frame4, text="EMI", font=("Times New Roman", 12, "bold"), relief=GROOVE, anchor="center")
# E.pack(side=LEFT, pady=20, padx=10, ipadx=10, ipady=5)

# l = Label(frame4, text="", anchor="center")
# l.pack(side=LEFT, pady=20, ipadx=20, ipady=5)

# button = Button(Nextframe, text="Calculate EMI", command=Calculate(1000, 2, 3))
# # button.config(foregroundcolor="green")
# button.pack(side = BOTTOM, pady = 20)

