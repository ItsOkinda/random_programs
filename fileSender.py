import socket
import zipfile
import os
from tkinter import Tk, filedialog, Button, Label
from flask import Flask, send_file
import threading

app = Flask(__name__)
selected_files = []
zip_filename = 'files.zip'

def zip_files(file_paths, output_filename):
    with zipfile.ZipFile(output_filename, 'w') as zipf:
        for file in file_paths:
            zipf.write(file, os.path.basename(file))
    print(f"Files zipped into {output_filename}")

@app.route('/download')
def download_file():
    return send_file(zip_filename, as_attachment=True)

def start_flask():
    app.run(host='0.0.0.0', port=5000)

def select_files():
    global selected_files
    selected_files = filedialog.askopenfilenames(title="Select files to share")
    label.config(text=f"Selected {len(selected_files)} files")

def start_server():
    if selected_files:
        zip_files(selected_files, zip_filename)
        threading.Thread(target=start_flask).start()
        label.config(text=f"Server started. Access files at http://{socket.gethostbyname(socket.gethostname())}:5000/download")
    else:
        label.config(text="No files selected.")

# Create a GUI for file selection
root = Tk()
root.title("File Sender")

label = Label(root, text="Select files to share")
label.pack()

select_button = Button(root, text="Select Files", command=select_files)
select_button.pack()

start_button = Button(root, text="Start Server", command=start_server)
start_button.pack()

root.mainloop()

