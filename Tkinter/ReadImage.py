import tkinter as tk
from tkinter import ttk
from test import get_image
from tkinter import *


root = tk.Tk()
root.geometry("1000x600+6+6")
root.resizable(True, True)


button = ttk.Button(root)

img = PhotoImage(file=r"C:/Users/Laptop/Desktop/a.png")

label = ttk.Label(root, image = img)
label.grid(row = 0, column = 0)

label.mainloop()
