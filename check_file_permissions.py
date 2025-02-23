import os

def check_permissions(file_path):
    permissions = ""
    if os.access(file_path, os.R_OK):
        permissions += "readable "
    if os.access(file_path, os.W_OK):
        permissions += "writable "
    if os.access(file_path, os.X_OK):
        permissions += "executable"
    print(f"Permissions for {file_path}: {permissions}")

file_path = input("Enter the file path: ")
check_permissions(file_path)
