import os
import platform
from tkinter import *
from tkinter.filedialog import askopenfilename

def open_filepath():
    """Open a JSON file."""
    filepath = askopenfilename(
        filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
    )
    if filepath:
        return filepath
    else:
        return

# def open_file():
#     """Open a JSON file."""
#     filepath = askopenfilename(
#         filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
#     )
#     if filepath:
#         # For macOS/Linux and Windows
#         if platform.system() == 'Linux' or platform.system() == 'Darwin':
#             os.system(f"open {filepath}")
#         else:
#             os.startfile(filepath)
#         return filepath
#     else:
#         pass