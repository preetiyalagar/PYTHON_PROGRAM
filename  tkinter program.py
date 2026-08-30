from tkinter import *#all sub-classes
#tk=tool kit interface for GUI programs
import tkinter as tk #alias

window=tk.Tk()#creates window/form
window.geometry('300x200')#win size
window.title('My GUI Form')
head=Label(window, text='Login Form', font='sans 18 bold', fg='red', bg='cyan').pack(fill='both')

user=Label(window, text='Enter User ID', font='sans 14 bold').pack()
e1=Entry(window, font='sans 14 bold',).pack()

password=Label(window, text='Enter Password', font='sans 14 bold').pack()
e2=Entry(window, font='sans 14 bold', show='*').pack()

b1=Button(window, text='Login Here', font='sans 14 bold', bg='green', fg='white').pack()
