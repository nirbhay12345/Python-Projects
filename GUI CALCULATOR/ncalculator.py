from tkinter import * 
import tkinter as tk


class Calc:
    # set label 
    def set_label(self, event, name):
        self.label.config(text=self.label['text']+name)  

    def clear(self):
        self.label.config(text="")

    def equate(self, event):
        try: 
            total = str(eval(self.label['text'])) 
            self.label.config(text=total) 
        except: 
            self.label.config(text="math error ") 

    def __init__(self, calc, font):
        self.font = font

        self.label = Label(calc, text="", font=self.font)

        self.add = Button(calc, text="+", font=self.font)
        self.add.bind('<Button-1>', lambda e,n = self.add['text'] : self.set_label(e,n))

        self.sub = Button(calc, text="-", font=self.font)
        self.sub.bind('<Button-1>', lambda e,n = self.sub['text'] : self.set_label(e,n))

        self.mul = Button(calc, text="*", font=self.font)
        self.mul.bind('<Button-1>', lambda e,n = self.mul['text'] : self.set_label(e,n))

        self.div = Button(calc, text="/", font=self.font)
        self.div.bind('<Button-1>', lambda e,n = self.div['text'] : self.set_label(e,n))

        self.eql = Button(calc, text="=", font=self.font)
        self.eql.bind('<Button-1>', self.equate)

        self.clear = Button(calc, text="C", font=self.font, command=self.clear)

        self.zero = Button(calc, text="0", font=self.font)
        self.zero.bind('<Button-1>', lambda e,n = self.zero['text'] : self.set_label(e,n))

        self.one = Button(calc, text="1", font=self.font)
        self.one.bind('<Button-1>', lambda e,n = self.one['text'] : self.set_label(e,n))

        self.two = Button(calc, text="2", font=self.font)
        self.two.bind('<Button-1>', lambda e,n = self.two['text'] : self.set_label(e,n))

        self.three = Button(calc, text="3", font=self.font)
        self.three.bind('<Button-1>', lambda e,n = self.three['text'] : self.set_label(e,n))

        self.four = Button(calc, text="4", font=self.font)
        self.four.bind('<Button-1>', lambda e,n = self.four['text'] : self.set_label(e,n))

        self.five = Button(calc, text="5", font=self.font)
        self.five.bind('<Button-1>', lambda e,n = self.five['text'] : self.set_label(e,n))

        self.six = Button(calc, text="6", font=self.font)
        self.six.bind('<Button-1>', lambda e,n = self.six['text'] : self.set_label(e,n))

        self.seven = Button(calc, text="7", font=self.font)
        self.seven.bind('<Button-1>', lambda e,n = self.seven['text'] : self.set_label(e,n))

        self.eight = Button(calc, text="8", font=self.font)
        self.eight.bind('<Button-1>', lambda e,n = self.eight['text'] : self.set_label(e,n))

        self.nine = Button(calc, text="9", font=self.font)
        self.nine.bind('<Button-1>', lambda e,n = self.nine['text'] : self.set_label(e,n))

        # calculator ui
        # row zero
        self.label.grid(row=0, column=0, columnspan=4, sticky=N+W+E+S)
        self.label.configure(background='#ffffff', height=7)
        # row one
        self.seven.grid(row=1, column=0, sticky=E+W+N+S)
        self.seven.configure(height=3, width=5)
        
        self.eight.grid(row=1, column=1, sticky=E+W+N+S)
        self.eight.configure(height=3, width=5)
        
        self.nine.grid(row=1, column=2, sticky=E+W+N+S)
        self.nine.configure(height=3, width=5)

        self.add.grid(row=1, column=3, sticky=E+W+N+S)
        self.add.configure(height=3, width=5)
        # row two
        self.four.grid(row=2, column=0, sticky=E+W+N+S)
        self.four.configure(height=3, width=5)
        
        self.five.grid(row=2, column=1, sticky=E+W+N+S)
        self.five.configure(height=3, width=5)
        
        self.six.grid(row=2, column=2, sticky=E+W+N+S)
        self.six.configure(height=3, width=5)

        self.sub.grid(row=2, column=3, sticky=E+W+N+S)
        self.sub.configure(height=3, width=5)
        # row three
        self.one.grid(row=3, column=0, sticky=E+W+N+S)
        self.one.configure(height=3, width=5)
        
        self.two.grid(row=3, column=1, sticky=E+W+N+S)
        self.two.configure(height=3, width=5)
        
        self.three.grid(row=3, column=2, sticky=E+W+N+S)
        self.three.configure(height=3, width=5)

        self.mul.grid(row=3, column=3, sticky=E+W+N+S)
        self.mul.configure(height=3, width=5)
        #row four
        self.zero.grid(row=4, column=0, sticky=E+W+N+S)
        self.zero.configure(height=3, width=5)
        
        self.div.grid(row=4, column=1, sticky=E+W+N+S)
        self.div.configure(height=3, width=5)

        self.clear.grid(row=4, column=2, sticky=E+W+N+S)
        self.clear.configure(height=3, width=5)

        self.eql.grid(row=4, column=3, sticky=E+W+N+S)
        self.eql.configure(height=3, width=5)
  



root = Tk()
font = ("Times", "20", "bold")

root.geometry("400x500+500+100")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(2, weight=1)

root.grid_columnconfigure(3, weight=1)
root.grid_rowconfigure(3, weight=1)

root.grid_rowconfigure(4, weight=1)

photo = PhotoImage(file = 'cal.png')
root.iconphoto(False, photo)

MyCal = Calc(root, font)

root.mainloop()