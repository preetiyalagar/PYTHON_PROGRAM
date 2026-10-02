from tkinter import*
from tkinter import ttk #themed tool kit[combox]
window=Tk()
window.title("Welcome to MIT India")
window.geometry('400x300')
hd=Label(window, text="Registration form", fg='blue', font='sans 14', bg='yellow').grid(row=0, column=0, columnspan=4, sticky='nsew', padx=20, pady=20)

a=Label(window, text="First Name").grid(row=1, column=0)
b=Label(window, text="Last Name").grid(row=2, column=0)
c=Label(window, text="Email Id").grid(row=3, column=0)
d=Label(window, text="Contact Number").grid(row=4, column=0)

a1=Entry(window).grid(row=1, column=1)
b1=Entry(window).grid(row=2, column=1)
c1=Entry(window).grid(row=3, column=1)
d1=Entry(window).grid(row=4, column=1)

v=IntVar()
gen=Label(window, text="Gender").grid(row=5, column=0)
m=Radiobutton(window, text='Male',variable=v, value=1).grid(row=5, column=1)
f=Radiobutton(window, text='Female', variable=v, value=2).grid(row=5, column=2)

course=["Java","Python","C++"]#list
l1=Label(window,text="Choose Language").grid(column=0, row=6)

cb=ttk.Combobox(window, values=course, width=10)
cb.grid(column=1, row=6)
cb.current(1)

btn=Button(window, text="Submit", fg='green', font='sans 14').grid(row=7, column=1)
btn2=Button(window, text="Cancel", fg='red', font='sans 14').grid(row=7, column=2)

mainloop()


                                                                                        





                                                                                        





                                                                                        





                                                                                        
