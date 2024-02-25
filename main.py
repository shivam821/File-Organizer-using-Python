import os
import shutil

file_path = input("Enter the path : ")

files = os.listdir(file_path)

for i in files : 
    filename,extention = os.path.splitext(i)
    extention = extention[1:]

    if os.path.exists(file_path + '/' + extention) : 
        shutil.move(file_path + '/' + i, file_path + '/' + extention + '/' + i)
        print("Files Moved")
    else :
        os.makedirs(file_path + '/' + extention)
        shutil.move(file_path + '/' + i, file_path + '/' + extention + '/' + i)
        print("Folder created. Files Moved.")
