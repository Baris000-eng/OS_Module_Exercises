import os

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted {file_path}")
    else:
        print(f"File {file_path} not found.")

file_path = input("Enter the file path to delete: ")
delete_file(file_path)
