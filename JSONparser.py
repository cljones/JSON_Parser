import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import *
from fileoperations import *
from parser_actions import *

    
# Window Frame
window = Tk()
menu = Menu(window)
message = Message(window, text='Welcome to the Parser')

# Window configuration
window.resizable(False, False)
window.title('JSON Parser')
window.config(menu=menu)
window.geometry("600x300")

# Menu
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=window.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command= lambda: about(window))

var = StringVar()
var.set("Welcome to the JSON Parser.")

label = tk.Label(window, text="Enter key data you want to clean:")
label.pack()

entry = tk.Entry(window)
entry.pack()

# Buttons and their configurations
parse_btn = Button(window, 
                 text="Parse",
                 anchor="center",
                 font=("Arial", 12),
                 height=1,
                 width=7,
                 cursor="hand2",
                 disabledforeground="gray",
                 command=lambda: run(entry))

parse_btn.place(x=255, y = 200)

window.mainloop()
