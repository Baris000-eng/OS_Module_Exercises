import os

def check_if_directory(path):
    if os.path.isdir(path):
        print(f"{path} is a directory.")
    else:
        print(f"{path} is not a directory.")

path = input("Enter the path: ")
check_if_directory(path)
