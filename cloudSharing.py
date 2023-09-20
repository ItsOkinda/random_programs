#Bear- author
# make sure you install the imported libraries 




import gofile as go
from tkinter import filedialog
import tkinter as tk



def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Selected File: {file_path}")
        return file_path

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        print(f"Selected Folder: {folder_path}")
        return folder_path
    
def store(file_path):
    server = go.getServer()
    print(server)
    url = go.uploadFile(file_path)
    if 'downloadpage' in url:
        print("Download link:", url["downloadpage"])
    else:
        print("Download link not found in the response:", url)



root = tk.Tk()
root.title("File and Folder Selection")

# Create buttons to select file or folder
file_button = tk.Button(root, text="Select File", command=select_file)
folder_button = tk.Button(root, text="Select Folder", command=select_folder)




file_button.pack(pady=10)
folder_button.pack(pady=10)
if select_file:
    store(select_file())
else :
    store(select_folder())

root.mainloop()
