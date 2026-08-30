#Combo Box in Python
from tkinter import*
from tkinter import ttk #ttk=themed tool kit, so more advanced or modern controls
win=Tk()
win.geometry('200x200')
win.configure(bg='green')
course=["Java","Python","C++"]
l1=Label(win,text="select Your Favourite Language",bg='green',fg='yellow')
l1.grid(column=0, row=0)

cb=ttk.Combobox(win,values=course,width=10)
cb.grid(column=0, row=1)
cb.current(0)

win.mainloop()
