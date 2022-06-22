import tkinter as tk
import time
import os
import sys

# time initalization
init = time.time()  # time initalization

# type files in the folder
videos = [".mp4", ".mov", ".avi"]
audios = [".mp3", ".wav", ".flac", ".ogg", ".aac", ".wma"]
pictures = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"]
compresseds = [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".img", ".dng"]
texts = [".txt", ".doc", ".docx", ".odt", ".pdf", ".html", ".htm", ".xml", ".xls", ".xlsx", ".csv"]
programs = [".exe", ".msi", ".apk", ".bat", ".jar"]

try:
    user = sys.argv[1]
    folder = sys.argv[2]
except IndexError:
    print("Error: No user or folder name given")
    sys.exit()

OS = sys.platform
if OS == "win32":
    path = "C:\\Users\\" + user + "\\" + folder + "\\"
elif OS == "linux":
    path = "/home/" + user + "/" + folder + "/"
elif OS == "darwin":
    path = "/Users/" + user + "/" + folder + "/"
else:
    print("Error: Unknown OS")
    sys.exit()

# create folders if they don't exist
folders = ["Videos", "Audios", "Pictures",
           "Compresseds", "Documents", "Programs", "Others"]
for each in folders:
    if not os.path.exists(path + each):
        os.makedirs(path + each)

# move files to their respective folders
for file in os.listdir(path):
    if file.endswith(tuple(pictures)):
        os.rename(path + file, path + "Pictures/" + file)
    elif file.endswith(tuple(videos)):
        os.rename(path + file, path + "Videos/" + file)
    elif file.endswith(tuple(audios)):
        os.rename(path + file, path + "Audios/" + file)
    elif file.endswith(tuple(compresseds)):
        os.rename(path + file, path + "Compresseds/" + file)
    elif file.endswith(tuple(texts)):
        os.rename(path + file, path + "Documents/" + file)
    elif file.endswith(tuple(programs)):
        os.rename(path + file, path + "Programs/" + file)
    else:
        if not os.path.isdir(path + file):
            os.rename(path + file, path + "Others/" + file)

        else:
            if file not in folders:
                os.rename(path + file, path + "Others/" + file)


end = time.time()

# create a tkinter window
root = tk.Tk()
root.title("Folder Organizer")
root.geometry("300x50")
label = tk.Label(root, text="Time: " + str(round(end - init, 2)) + " seconds")
label.pack()
label = tk.Label(root, text="Done!")
label.pack()
root.mainloop()
sys.exit()
