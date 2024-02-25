import os
import shutil

# Get the input from the user for the directory path
file_path = input("Enter the path: ")

# List all files in the specified directory
files = os.listdir(file_path)

# Iterate through each file in the directory
for i in files:
    # Split the filename and extension
    filename, extension = os.path.splitext(i)
    extension = extension[1:]  # Remove the leading dot from the extension

    # Check if a directory with the same extension exists
    if os.path.exists(file_path + '/' + extension):
        # Move the file to the directory with the corresponding extension
        shutil.move(file_path + '/' + i, file_path + '/' + extension + '/' + i)
        print("Files Moved")
    else:
        # If the directory doesn't exist, create it
        os.makedirs(file_path + '/' + extension)
        # Move the file to the newly created directory with the corresponding extension
        shutil.move(file_path + '/' + i, file_path + '/' + extension + '/' + i)
        print("Folder created. Files Moved.")
