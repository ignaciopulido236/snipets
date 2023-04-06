# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:02:12 2023

@author: ignac
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class FileSelectionGUI(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.init_ui()
        
        style=ttk.Style(self)
        style.theme_use('winnative')
        
            

    def init_ui(self):
        
        self.master.title("Shapefile Converter to Step")

        # create first file selection field
        self.file1_label = tk.Label(self.master, text="Shapefile:")
        self.file1_label.grid(row=0, column=0, padx=5, pady=5)

        self.file1_field = tk.Entry(self.master, width=50)
        self.file1_field.grid(row=0, column=1, padx=5, pady=5)

        self.file1_button = tk.Button(self.master, text="Browse", command=self.select_file1)
        self.file1_button.grid(row=0, column=2, padx=5, pady=5)

        # create second file selection field
        self.file2_label = tk.Label(self.master, text="Output Folder")
        self.file2_label.grid(row=1, column=0, padx=5, pady=5)

        self.file2_field = tk.Entry(self.master, width=50)
        self.file2_field.grid(row=1, column=1, padx=5, pady=5)

        self.file2_button = tk.Button(self.master, text="Browse", command=self.select_file2)
        self.file2_button.grid(row=1, column=2, padx=5, pady=5)

        # create button to run selected files
        self.run_button = tk.Button(self.master, text="Run All ", command=self.run_files)
        self.run_button.grid(row=2, column=1, padx=5, pady=5,sticky='nsew')
        
        self.run_button = tk.Button(self.master, text="Generate Metadata", command=self.run_files, background='#4BA55F',height=2)
        self.run_button.grid(row=4, column=1, padx=5, pady=5,sticky='nsew')
        
        self.run_button = tk.Button(self.master, text="Validate Polygons", command=self.run_files)
        self.run_button.grid(row=6, column=1, padx=5, pady=5,sticky='nsew')
        
        self.run_button = tk.Button(self.master, text="Generate Solids", command=self.run_files)
        self.run_button.grid(row=8, column=1, padx=5, pady=5,sticky='nsew')
        
        self.run_button = tk.Button(self.master, text="Join Solids", command=self.run_files)
        self.run_button.grid(row=10, column=1, padx=5, pady=5,sticky='nsew')
        
        self.run_button = tk.Button(self.master, text="Change Coordinate System", command=self.run_files)
        self.run_button.grid(row=12, column=8, padx=5, pady=5,sticky='nsew')
        
  

    def select_file1(self):
        file_path = filedialog.askopenfilename()
        self.file1_field.delete(0, tk.END)
        self.file1_field.insert(0, file_path)

    def select_file2(self):
        file_path = filedialog.askopenfilename()
        self.file2_field.delete(0, tk.END)
        self.file2_field.insert(0, file_path)

    def run_files(self):
        file1 = self.file1_field.get()
        file2 = self.file2_field.get()
        print(f"Running files: {file1} and {file2}")
    
    
    def create_widgets(self):
        self.output = tk.Text(self, height=20, width=80, state="disabled")
        self.output.pack()
        self.input = tk.Entry(self, width=80)
        self.input.pack()
        self.input.bind("<Return>", self.handle_input)

    def handle_input(self, event):
        user_input = self.input.get()
        self.input.delete(0, tk.END)
        self.print_message("> " + user_input)
        # Do something with the user's input here

    def print_message(self, message):
        self.output.configure(state="normal")
        self.output.insert(tk.END, message + "\n")
        self.output.see(tk.END)
        self.output.configure(state="disabled")
    
root = tk.Tk()
root.configure(bg='#36403E')

app = FileSelectionGUI(master=root)
app.mainloop()
