#Button Demo in GUI Python
import tkinter as tk #t=tool k=kit interface: GUI
r=tk.Tk()

r.title('Button Demo')
r.geometry('200x200')

button=tk.Button(r, text='Exit', bg='red', fg='white', width=15, height=2, command=r.destroy)
button.pack()
r.mainloop()
