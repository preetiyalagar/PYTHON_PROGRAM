from tkinter import*
import tkinter as tk
window=tk.Tk()
window.geometry('350x280')
window.title('My GUI Form')
head=Label(window, text='Radio and Check Form', font='sans 18 bold', fg='red', bg='yellow').pack(fill='both')

v=IntVar()
gender=Label(window, text='Select Gender', font='sans 14 bold').pack()
m=Radiobutton(window, text='Male', variable=v, value=1).pack()
f=Radiobutton(window, text='Female', variable=v, value=2).pack()

hobbies=Label(window, text='Select Hobbies', font='sans 14 bold').pack()
c1=Checkbutton(window, text='Music').pack()
c2=Checkbutton(window, text='Movies').pack()
c3=Checkbutton(window, text='Sports').pack()
c4=Checkbutton(window, text='Reading').pack()
