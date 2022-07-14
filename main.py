#!/usr/bin/env python
import sys
from PIL import Image
import os
import time
from tkinter import filedialog, ttk, messagebox
from tkinter import Tk


class Window(Tk):
    BUTTONS = {"Video": [".mp4", ".avi", ".mov", ".MP4", ".AVI", ".MOV"],
               "Audio": [".mp3", ".wav", ".flac", ".ogg", ".aac", ".wma"],
               "Image": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".heic", ".heif", ".svg",
                         ".ico", ".PNG", ".JPG", ".JPEG", ".GIF", ".BMP", ".TIFF", ".WEBP", ".HEIC", ".HEIF",
                         ".SVG", ".ICO", ".TIFF"],
               "Document": [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".rtf", ".csv", ".html",
                            ".htm", ".xml", ".json", ".yml", ".yaml", ".md", ".markdown"],
               "Compressed": [".zip", ".rar", ".img", ".dmg", ".tar", ".7z", ".bin"],
               "Program": [".exe", ".msi", ".app", ".deb", ".apk", ".jar", ".py", ".bat", ".java"]}
    OS = sys.platform
    PATH: str

    # path protected
    protected: list = ['C:/', 'C:/Users', '/home', '/Users', '/']

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
        username: str
        typeOS = {'win32': 'C:/Users', 'linux': '/home', 'darwin': '/Users'}
        error = 'Please select a folder different than the default one.'
        for element in typeOS:
            if self.OS == element:
                self.PATH = filedialog.askdirectory(initialdir=typeOS[element])
                for i in self.protected:
                    if i == self.PATH:
                        messagebox.showerror('Error', error)
                        return
                if self.OS == 'win32':
                    username = self.PATH.split('/')[2]
                else:
                    username = self.PATH.split('/')[1]
                self.protected.append(str(typeOS[element]) + '/' + str(username))

        for i in self.protected:
            if self.PATH == i:
                messagebox.showerror('Error', error)
                return

        for button in self.BUTTONS:
            globals()[button].config(state="enabled")

        message = ttk.Label(self, text=self.PATH)
        message.grid(row=1, padx=5, pady=5, sticky="NSEW")

    def organize(self, type: str):
        # get files
        files = os.listdir(self.PATH)
        ext = self.BUTTONS[type]
        start = time.time()

        if not os.path.exists(self.PATH + "/" + type):
            os.makedirs(self.PATH + "/" + type)

        for file in files:
            if file.endswith(tuple(ext)):
                # move file
                os.rename(self.PATH + "/" + file, self.PATH +
                          "/" + type + "/" + file)

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
    Window().mainloop()
