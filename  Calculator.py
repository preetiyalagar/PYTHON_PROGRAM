import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.configure(bg="#2c2c2c")

# String variable to store the current expression
expression = ""

# Function to update expression in the entry box
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    global expression
    try:
        # eval evaluates the string expression directly
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Variable to track text input
equation = tk.StringVar()

# Display screen
display = tk.Entry(
    root, 
    textvariable=equation, 
    font=("Arial", 24, "bold"), 
    bd=10, 
    insertwidth=4, 
    width=14, 
    borderwidth=0, 
    justify="right"
)
display.grid(columnspan=4, ipady=15, padx=10, pady=10)

# Button styling configuration
btn_config = {
    "font": ("Arial", 18, "bold"),
    "bg": "#8e8e8e",
    "fg": "black",
    "activebackground": "#a0a0a0",
    "borderwidth": 1,
    "relief": "raised"
}

# Button layout grid
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('.', 4, 2), ('/', 4, 3)
]

# Create and place standard buttons
for (text, row, col) in buttons:
    if text == 'C':
        action = clear
    else:
        action = lambda x=text: press(x)
        
    btn = tk.Button(root, text=text, command=action, **btn_config)
    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Equals button spanning across the bottom
equal_btn = tk.Button(root, text="=", command=equalpress, **btn_config)
equal_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

# Configure row and column weights so the UI scales nicely
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(1, 6):
    root.rowconfigure(i, weight=1)

# Start the application loop
root.mainloop()           
            
