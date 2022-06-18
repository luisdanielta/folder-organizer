import tkinter as tk
import time
import os
import sys

# time initalization
init = time.time()  # time initalization

# type files in the folder
videos = [".mp4", ".mov", ".avi"]
audios = [".mp3", ".wav", ".flac"]
pictures = [".jpg", ".jpeg", ".png"]
compresseds = [".zip", ".rar", ".7z"]
texts = [".txt", ".doc", ".docx", ".odt", ".pdf", ".html", ".htm", ".xml"]
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
folders = ["videos", "audios", "pictures",
           "compresseds", "texts", "programs", "others"]
for each in folders:
    if not os.path.exists(path + each):
        os.makedirs(path + each)

# move files to their respective folders
for file in os.listdir(path):
    if file.endswith(tuple(pictures)):
        os.rename(path + file, path + "pictures/" + file)
    elif file.endswith(tuple(videos)):
        os.rename(path + file, path + "videos/" + file)
    elif file.endswith(tuple(audios)):
        os.rename(path + file, path + "audios/" + file)
    elif file.endswith(tuple(compresseds)):
        os.rename(path + file, path + "compresseds/" + file)
    elif file.endswith(tuple(texts)):
        os.rename(path + file, path + "texts/" + file)
    elif file.endswith(tuple(programs)):
        os.rename(path + file, path + "programs/" + file)
    else:
        if not os.path.isdir(path + file):
            os.rename(path + file, path + "others/" + file)

        else:
            if file not in folders:
                os.rename(path + file, path + "others/" + file)


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
