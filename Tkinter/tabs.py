# to add tabs inside window using Notebook widget in Tkinter

# importing modules
import tkinter as tk
from  tkinter import ttk


# root window - initializing main window
root = tk.Tk()
root.geometry('600x300')
root.title('Notebook Demo')
root.resizable(False, False)


# Notebook
notebook = ttk.Notebook(root)
notebook.pack(pady = 10)


# create frame:
frame1 = ttk.Frame(notebook, width = 550, height = 300)
frame2 = ttk.Frame(notebook, width = 550, height = 300)


# add frames to notebook
notebook.add(frame1, text = "Screen 1")
notebook.add(frame2, text = "Screen 2")


# add content to each tab
ttk.Label(frame1, text = "welcome").grid(column = 0, row = 0, padx = 0, pady = 3)
ttk.Label(frame2, text = "welcome22").grid(column = 0, row = 0, padx = 0, pady = 3)

root.mainloop()
