import os

def get_file_size(file_path):
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        print(f"Size of {file_path}: {size} bytes")
    else:
        print(f"File {file_path} does not exist.")

file_path = input("Enter the file path: ")
get_file_size(file_path)
