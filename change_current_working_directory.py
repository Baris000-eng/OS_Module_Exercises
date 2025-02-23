import os

def change_directory(directory):
    try:
        os.chdir(directory)
        print(f"Changed directory to {directory}")
    except FileNotFoundError:
        print(f"Directory {directory} not found.")

directory = input("Enter the directory to change to: ")
change_directory(directory)
