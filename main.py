#!/usr/bin/env python
import sys
import os
import time
from tkinter import filedialog, ttk, messagebox
from tkinter import Tk


class Window(Tk):

    BUTTONS = {"Video": [".mp4", ".avi", ".mov"],
               "Audio": [".mp3", ".wav", ".flac", ".ogg", ".aac", ".wma"],
               "Image": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".psd", ".webp", ".heic", ".heif", ".svg", ".ico", ".PNG", ".JPG", ".JPEG", ".GIF", ".BMP", ".TIFF", ".PSD", ".WEBP", ".HEIC", ".HEIF", ".SVG", ".ICO"],
               "Document": [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".rtf", ".csv", ".html", ".htm", ".xml", ".json", ".yml", ".yaml", ".md", ".markdown"],
               "Compressed": [".zip", ".rar", ".img", ".dng", ".tar", ".7z"],
               "Program": [".exe", ".msi", ".app", ".deb", ".apk", ],
               "Photoshop": [".psd"],
               "Illustrator": [".ai", ".eps"], }
    OS = sys.platform
    PATH: str

    def __init__(self):
        super().__init__()
        self.title("Folder Organizer")
        self.resizable(False, False)
        globals()

        folder = ttk.Button(self, text="Select Folder", command=self.getPath)
        folder.grid(row=0, padx=5, pady=5, sticky="NSEW")

        self.content()

        self.exit = ttk.Button(self, text="Exit", command=self.destroy)
        self.exit.grid(row=4, padx=5, pady=5, sticky="NSEW")

    def getPath(self):
        if self.OS == "win32":
            self.PATH = filedialog.askdirectory(initialdir="C:\\Users")
        elif self.OS == "linux":
            self.PATH = filedialog.askdirectory(initialdir="/home")
        elif self.OS == "darwin":
            self.PATH = filedialog.askdirectory(initialdir="/Users")
        else:
            print("Unsupported OS")
            self.destroy()

        if self.PATH == 'C:/Users' or self.PATH == '/home' or self.PATH == '/Users':
            text = "Please select a foldel different than the default one."
            messagebox.showerror("Error", text)
            return

        # globals() config state of buttons to be enabled
        for button in self.BUTTONS:
            globals()[button].config(state="enabled")

        self.textPath = ttk.Label(self, text=self.PATH)
        self.textPath.grid(row=1, padx=5, pady=5, sticky="NSEW")

        # create folders
        for button in self.BUTTONS:
            if button != "All":
                if not os.path.exists(self.PATH + "\\" + button):
                    os.makedirs(self.PATH + "\\" + button)

    def organize(self, type):
        # get files
        files = os.listdir(self.PATH)
        ext = self.BUTTONS[type]
        start = time.time()

        for file in files:
            if file.endswith(tuple(ext)):
                # move file
                os.rename(self.PATH + "\\" + file, self.PATH +
                          "\\" + type + "\\" + file)
        
        end = time.time()
        text = "Organization completed in " + str(end - start) + " seconds."
        messagebox.showinfo("Completed", text)
            

    def content(self):
        self.frame = ttk.LabelFrame(self, text="File Groups")
        self.frame.grid(row=2, padx=5, pady=5, sticky="NSEW")
        r = 0
        c = 0
        for button in self.BUTTONS:
            globals()[button] = ttk.Button(
                self.frame, text=button, state="disabled", command=lambda button=button: self.organize(button))
            globals()[button].grid(row=r, column=c, padx=3, pady=3)
            c += 1
            if c == 4:
                r += 1
                c = 0


if __name__ == "__main__":
    app = Window()
    app.mainloop()
