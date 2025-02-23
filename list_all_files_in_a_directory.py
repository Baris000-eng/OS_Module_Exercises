import os

def list_files(directory):
    for filename in os.listdir(directory):
        print(filename)

directory = input("Enter the directory path: ")
list_files(directory)
