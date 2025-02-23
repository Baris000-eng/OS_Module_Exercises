import os

def check_if_empty(file_path):
    if os.path.exists(file_path):
        if os.path.getsize(file_path) == 0:
            print(f"{file_path} is empty.")
        else:
            print(f"{file_path} is not empty.")
    else:
        print(f"File {file_path} does not exist.")

file_path = input("Enter the file path: ")
check_if_empty(file_path)
