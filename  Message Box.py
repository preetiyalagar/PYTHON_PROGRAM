from tkinter import messagebox
import tkinter as tk
from tkinter import *
root=tk.Tk()
root.geometry('500x200')

lb=tk.Label(root, text="Messagebox demo", fg='teal', bg='white', font='sans 14').grid(row=0, column=0, columnspan=6, sticky='nsew')

def info():
    messagebox.showinfo('info', 'Thank you')

b1=tk.Button(root,text='Information',font='sans 14', bg='skyblue', command=info).grid(row=1, column=0, padx=10, pady=10)

def error():
    messagebox.showerror('Error', 'Oh its error!')

b2=tk.Button(root,text='Error',font='sans 14', bg='red', command=error).grid(row=1, column=1, padx=10, pady=10)

def warn():
    messagebox.showwarning('Warning', 'Hello its Warning!')

b3=tk.Button(root,text='Warning',font='sans 14', bg='orange', command=warn).grid(row=1, column=2, padx=10, pady=10)

def askq():
    messagebox.askquestion('What!', 'Are you sure?')

b4=tk.Button(root,text='Are you sure?',font='sans 14', bg='magenta', command=askq).grid(row=2, column=0, padx=10, pady=10)

def okcan():
    messagebox.askokcancel('askokcancel', 'Want to continue?')

b5=tk.Button(root,text='What?',font='sans 14', bg='lightgreen', command=okcan).grid(row=2, column=1, padx=10, pady=10)

def askyes():
    messagebox.askyesno('askyesno', 'Find the value?')

b6=tk.Button(root,text='YesNo',font='sans 14', bg='skyblue', command=askyes).grid(row=2, column=2, padx=10, pady=10)

def retry():
    messagebox.askretrycancel('askretrycancel', 'Try again?')

b7=tk.Button(root,text='Re-try',font='sans 14', bg='green', command=retry).grid(row=2, column=3, padx=10, pady=10)











