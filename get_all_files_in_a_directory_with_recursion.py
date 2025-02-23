import os

def list_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))

directory = input("Enter the directory path: ")
list_all_files(directory)
