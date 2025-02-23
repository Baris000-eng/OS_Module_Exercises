import os

def get_absolute_path(file_path):
    if os.path.exists(file_path):
        absolute_path = os.path.abspath(file_path)
        print(f"Absolute path: {absolute_path}")
    else:
        print(f"File {file_path} does not exist.")

file_path = input("Enter the file path: ")
get_absolute_path(file_path)
