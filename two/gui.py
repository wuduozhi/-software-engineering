# -*- coding: UTF-8 -*-
 
import tkinter as tk
from tkinter import ttk

# Create instance
window = tk.Tk()

# Add a title
window.title("My First Python GUI")

# Adding a Label that will get modified
a_label = ttk.Label(window, text = 'A Label')
a_label.grid(column=0, row=0)


# Modified Button click Event Function
def click_me():
	action.configure(text='Hello ' + name.get())

# Changing our Label
ttk.Label(window, text='Enter a name: ').grid(column=0, row=0)

# Adding a Text Box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(window, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(window, text="Click Me!", command=click_me)   
action.grid(column=1, row=1)

# Start GUI
window.mainloop()