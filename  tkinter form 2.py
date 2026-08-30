#List Box in Python
from tkinter import*
top=Tk()
top.title("List Box Demo")
top.geometry('300x300')#win size
top.geometry('+200+300')#left to right and top to bottom distance
top.configure(bg='red')

Lb=Listbox(top)
Lb.insert(1,'Python')
Lb.insert(2,'Java')
Lb.insert(3,'C++')
Lb.insert(4,'PHP')
Is=Label(top, text="List of Languages:", bg="blue", fg="yellow")
Is.pack(fill='both')
Lb.pack()
top.mainloop()
