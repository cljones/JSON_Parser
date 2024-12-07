import json
import os
import platform
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import *
from tkinter import messagebox
import re
from fileoperations import *


def about(window):
    a_text = """JSON data can be sometimes have wrong datatypes in certain key\nelements. For example, the key "Some Number" can have the value string of\n"9.0" instead of double value of 9.0. This JSON Parser program cleans up\nJSON files with problems like that. This was inspired by a real problem\nI face numerous times as a Contract Software Engineer."""
    
    about = Toplevel(window)
    about.geometry("650x450")
    about.resizable(False, False)
    about.title('About')
    
    a_widget = Text(about, height=400, width=500)
    a_widget.insert(tk.END, a_text)
    a_widget.config(state=DISABLED)
    a_widget.pack()
    
    
def is_float(string):
    # Compile a regular expression pattern to match valid float values
    pattern = r"^[-+]?[0-9]*\.?[0-9]+$"
    match = re.match(pattern, string)
    return bool(match)


def run(entry):
    # Opening JSON file    
    path = open_filepath()
    f = open(path)

    # returns JSON object as a dictionary
    data = json.load(f)

    # Iterating through the json list
    for i in range(len(data['emp_details'])):
         if entry.get() not in data['emp_details'][i]:     #Check if key is present
            messagebox.showerror('Error', 'Key not found!')
            break
        
         else:
            d = data['emp_details'][i][entry.get()]
            
            if d == 'N/A' or d=='n/A' or d=='N/a' or d=='n/a':
                data['emp_details'][i][entry.get()] = 0
                # Write to the file
                with open(path, 'w') as file:
                    json.dump(data, file, indent=4)

            else:                        
                if str(d).isdigit() == True and str(d).isdecimal()==True:
                    data['emp_details'][i][entry.get()]=int(d)
                    # Write to the file
                    with open(path, 'w') as file:
                        json.dump(data, file, indent=4)
                elif is_float(str(d)) == True:
                    data['emp_details'][i][entry.get()]=float(d)
                    # Write to the file
                    with open(path, 'w') as file:
                        json.dump(data, file, indent=4)
                else:
                    pass
    
    messagebox.showinfo("Updated JSON File", "All data keys have been corrected!")   
    
    # For macOS/Linux and Windows
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system(f"open {path}")
    else:
        os.startfile(path)                
 
    f.close()
    return data