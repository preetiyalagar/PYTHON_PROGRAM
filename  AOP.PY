#AOP using GUI-Event
from tkinter import*
#object on class Tk
window=Tk()
window.title("Welcome to GUI Python")
window.geometry('350x200')

#declaring controls
lbl=Label(window, text="", bg="yellow", font=('tahoma 14 bold'))
txt1=Entry(window,width=10,font=('tahoma 14 bold'))
txt2=Entry(window,width=10,font=('tahoma 14 bold'))

l1=Label(window, text="Num1:", font=('tahoma 14 bold'))
l2=Label(window, text="Num2:", font=('tahoma 14 bold'))
#placing controls, using grid
l1.grid(column=0, row=0)
l2.grid(column=0, row=1)
txt1.grid(column=1, row=0)
txt2.grid(column=1, row=1)
lbl.grid(column=0, row=3, columnspan=4, sticky='nsew')

#normal function
def add():
    res="sum", int(txt1.get())+int(txt2.get())
    lbl.configure(text=res)

btn=Button(window, text="Add",font=('tahoma 14 bold'), command=add)
btn.grid(column=0, row=4)

def sub():
    res="SUB", int(txt1.get())-int(txt2.get())
    lbl.configure(text=res)

btn=Button(window, text="SUB",font=('tahoma 14 bold'), command=sub)
btn.grid(column=1, row=4)

def mul():
    res="sum", int(txt1.get())*int(txt2.get())
    lbl.configure(text=res)

btn=Button(window, text="MUL",font=('tahoma 14 bold'), command=mul)
btn.grid(column=2, row=4)

def div():
    res="sum", int(txt1.get())/int(txt2.get())
    lbl.configure(text=res)

btn=Button(window, text="div",font=('tahoma 14 bold'), command=div)
btn.grid(column=2, row=5)

window.mainloop()










