import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import script


def input_dialog():
    input_dir = filedialog.askdirectory()
    input_entry.delete(0, "end")
    input_entry.insert(0, input_dir)


def output_dialog():
    output_dir = filedialog.askdirectory()
    output_entry.delete(0, "end")
    output_entry.insert(0, output_dir)


def submit():
    input_dir = input_entry.get()
    output_dir = output_entry.get()
    script.main(input_dir, output_dir)


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
