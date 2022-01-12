# Dropdown (combobox in Tkinter) and Entry

'''


'''
import tkinter as tk
from tkinter import ttk


# initializing for main window
root = tk.Tk()
root.geometry("600x300")
root.resizable(False, False)


def do_something(event):

    print(algorithm_list.current())
    if algorithm_list.current() == 0:
        # where you will add your algorithm for SVM]
        parameters = tk.Label(root, text = "Select Gamma")
        parameters.grid(column = 0, row = 3)
        select_gamma = ttk.Combobox(root, values = [0, 1])
        select_gamma.grid(column = 0, row = 4)
        
    else:
        # second cnn (use rest API) - you basically host your model somewhere and you reference via api call
        parameters = tk.Label(root, text = "Select mumber of deep networks")
        parameters.grid(column = 0, row = 3)
        select_gamma = ttk.Combobox(root, values = [0, 1])
        select_gamma.grid(column = 0, row = 4)

# label and fixing the size        
algorithm = tk.Label(root, text = "Select an algorithm")
algorithm.grid(column=0, row=0)

# writing combobox widget method and providing it with values
algorithm_list = ttk.Combobox(root, values = ["SVM", "CNN"])
algorithm_list.grid(column = 1, row = 0) # I am placing it side by side of previous label


# set initial value for combobox - not necessary
algorithm_list.current(0)


# get current selection and perform action if required
algorithm_list.bind("<<ComboboxSelected>>", do_something)


# exit button - to terminate the window
tk.Button(root, text = "Exit", command = root.destroy).grid(column = 4, row = 4)


# always remember to write this line
root.mainloop() # infinite loop to keep gui connected with underlying shell, sometimes to log output


# break, continue
'''
Button(root, text = "Exit", command = root.destroy).pack()

'''
