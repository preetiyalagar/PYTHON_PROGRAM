from tkinter import *#all sub-classes
#tk=tool kit interface for GUI programs
import tkinter as tk #alias

window=tk.Tk()#creates window/form
window.geometry('300x200')#win size
window.title('Python: Simple Login Application')
head=Label(window, text='Login Form', font='sans 18 bold', fg='red', bg='cyan').grid(row=0, column=1, columnspan=2)

Username=Label(window, text='Username', font='sans 14 bold').grid(row=1, column=0)
e1=Entry(window, font='sans 14 bold').grid(row=1, column=1)

Password=Label(window, text='Password', font='sans 14 bold').grid()
e2=Entry(window, font='sans 14 bold', show='*').grid(row=2, column=1)

b1=Button(window, text='Login Here', font='sans 14 bold', bg='green', fg='white').grid(row=5, column=1)


