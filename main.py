import os
import csv
from tkinter import Frame, Tk
from tkinter import ttk

app = Tk()
app.title("Folder Organizer")
app.resizable(False, False)

main = Frame(app)
main.pack()

# Buttons Organizer, Videos, Audios, Pictures, Compresseds, Documents, Programs, Others
buttons = ["Videos", "Audios", "Pictures", "Compresseds", "Documents", "Programs", "Others"]

for i in buttons:
    # Create a button in column 3, button i
    btn = ttk.Button(main, text=i)
    btn.grid(row=0, column=buttons.index(i), padx=5, pady=5)

app.mainloop()