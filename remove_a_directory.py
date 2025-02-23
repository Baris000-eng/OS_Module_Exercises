import os

# Get the directory path from the user
folder_path = input("Enter the path of the folder you want to remove: ")

# Check if the directory exists
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    # Remove the directory
    try:
        os.rmdir(folder_path)
        print(f"The folder '{folder_path}' has been removed.")
    except OSError as e:
        print(f"Error: {e}")
else:
    print(f"The folder '{folder_path}' does not exist or is not a directory.")
