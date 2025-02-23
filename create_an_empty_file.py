import os

def create_empty_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass
        print(f"Created empty file: {file_path}")
    else:
        print(f"File {file_path} already exists.")

file_path = input("Enter the file path: ")
create_empty_file(file_path)
