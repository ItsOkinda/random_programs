#please install the imports for the script to work

import os
from pdf2docx import Converter
import tkinter as tk
from tkinter import filedialog

def select_file():
    try:
        file_path = filedialog.askopenfilename()
        if file_path:
         print(f"Selected File: {file_path}")
    except Exception as k:
        print(f"An error occured{k}")
        return file_path

def converter(input_file_path, output_file_path):
    cv = Converter(input_file_path)
    cv.convert(output_file_path, start=0, end=None)
    cv.close()

# Create a Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window


pdf_path = select_file()

if pdf_path:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(script_dir, "output.docx")
    
    converter(pdf_path, output_file_path)
    print("Conversion complete. Output saved in the script's directory.")
