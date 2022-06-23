#!/usr/bin/env python
import sys
import os
import base64
import json
import re
import subprocess
import time
from tkinter import filedialog, ttk, messagebox
from tkinter import Tk


class Window(Tk):

    BUTTONS = {"Video": [], "Audio": [], "Image": [], "Document": [],
               "Compressed": [], "Program": [], "Other": [], "All": ["All"]}
    ADOBE = {
        "Photoshop": [".psd"],
        "Illustrator": [".ai", ".eps", ".pdf"]
    }
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

        for button in self.ADOBE:
            globals()[button].config(state="enabled")

        self.textPath = ttk.Label(self, text=self.PATH)
        self.textPath.grid(row=1, padx=5, pady=5, sticky="NSEW")

        # create folders
        for button in self.BUTTONS:
            if button != "All":
                if not os.path.exists(self.PATH + "\\" + button):
                    os.makedirs(self.PATH + "\\" + button)

    def content(self):
        self.frame = ttk.LabelFrame(self, text="File Groups")
        self.frame.grid(row=2, padx=5, pady=5, sticky="NSEW")
        r = 0
        c = 0
        for button in self.BUTTONS:
            globals()[button] = ttk.Button(
                self.frame, text=button, state="disabled")
            globals()[button].grid(row=r, column=c, padx=3, pady=3)
            c += 1
            if c == 4:
                r += 1
                c = 0

        self.adobe = ttk.LabelFrame(self, text="Adobe")
        self.adobe.grid(row=3, padx=5, pady=5, sticky="NSEW")
        r = 0
        c = 0
        for button in self.ADOBE:
            globals()[button] = ttk.Button(
                self.adobe, text=button, state="disabled")
            globals()[button].grid(row=r, column=c, padx=3, pady=3)
            c += 1
            if c == 4:
                r += 1
                c = 0


if __name__ == "__main__":
    app = Window()
    app.mainloop()
