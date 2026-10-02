from tkinter import*
import tkinter as tk
from tkinter import ttk #themed tool kit for combo box
root=tk.Tk()
root.title('Contact Information Form')
root.geometry('445x300')

name=Label(root, text='Name:', font='sans 14 bold').grid(row=1, column=0)
e1=Entry(root, text='Enter Name:', font='sans 14 bold').grid(row=1, column=1)

email=Label(root, text='Email ID:', font='sans 14 bold').grid(row=2, column=0)
e2=Entry(root, font='sans 14 bold').grid(row=2, column=1)

phone=Label(root, text='Ph.Number:', font='sans 14 bold').grid(row=3, column=0)
e3=Entry(root, font='sans 14 bold').grid(row=3, column=1)


b1=Button(root, text='Submit',font='sans 14 bold', bg='green', fg='white').grid(row=5, column=1)
