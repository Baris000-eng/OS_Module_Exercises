import os

def change_permissions(file_path, mode):
    if os.path.exists(file_path):
        os.chmod(file_path, mode)
        print(f"Changed permissions for {file_path}")
    else:
        print(f"File {file_path} does not exist.")

file_path = input("Enter the file path: ")
mode = int(input("Enter the mode (e.g., 0o755): "), 8)
change_permissions(file_path, mode)
