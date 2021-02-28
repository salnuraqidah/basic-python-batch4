import os

file_path = "file.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print("File " + file_path + " deleted")
else :
    print("file not exists")