import os

def count_files_in_directory(directory):
    # This is a list comprehension that creates a new list. It adds an entry f to the list only if it is a file.
    files_in_directory = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    file_count = len(files_in_directory)
    print(f"Number of files: {file_count}")

directory = input("Enter the directory path: ")
count_files_in_directory(directory)
