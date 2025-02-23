import os

def get_file_extension(file_path):
    if os.path.exists(file_path):
        path, extension = os.path.splitext(file_path)
        print(f"Extension: {extension}")
    else:
        print(f"File {file_path} does not exist.")

file_path = input("Enter the file path: ")
get_file_extension(file_path)
