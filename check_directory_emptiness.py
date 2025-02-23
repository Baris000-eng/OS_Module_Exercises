import os

def check_if_directory_empty(directory):
    if not os.listdir(directory):
        print(f"{directory} is empty.")
    else:
        print(f"{directory} is not empty.")

directory = input("Enter the directory path: ")
check_if_directory_empty(directory)
