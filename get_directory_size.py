import os

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    print(f"Total directory size: {total_size} bytes")

directory = input("Enter the directory path: ")
get_directory_size(directory)
