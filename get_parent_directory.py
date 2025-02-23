import os

def get_parent_directory(file_path):
    parent_dir = os.path.dirname(file_path)
    print(f"Parent directory: {parent_dir}")

file_path = input("Enter the file path: ")
get_parent_directory(file_path)
