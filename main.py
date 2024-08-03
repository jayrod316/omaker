import tkinter as tk
from tkinter import filedialog
import os
import tkinter.ttk as ttk
import script


def input_dialog():
    input_dir = filedialog.askdirectory()


def output_dialog():
    output_dir = filedialog.askdirectory()


def submit():
    pass


root = tk.Tk()
root.title("O Maker")
root.minsize(width=500, height=500)
root.config(padx=25, pady=25)

input_label = ttk.Label(text="Input Directory:")
input_label.grid(column=0, row=0)

input_entry = ttk.Entry(width=25)
input_entry.grid(column=1, row=0)

in_button = ttk.Button(text="Browse", command=input_dialog)
in_button.grid(column=2, row=0)

output_label = ttk.Label(text="Output Directory:")
output_label.grid(column=0, row=1)

output_entry = ttk.Entry(width=25)
output_entry.grid(column=1, row=1)

out_button = ttk.Button(text="Browse", command=output_dialog)
out_button.grid(column=2, row=1)

submit_button = ttk.Button(text="Submit", command=submit)
submit_button.grid(column=1, row=2)

root.mainloop()
