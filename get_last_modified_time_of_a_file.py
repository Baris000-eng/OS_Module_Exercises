import os
import time

def get_last_modified_time(file_path):
    if os.path.exists(file_path):
        timestamp = os.path.getmtime(file_path)
        print(f"Last modified time: {time.ctime(timestamp)}")
    else:
        print(f"File {file_path} does not exist.")

file_path = input("Enter the file path: ")
get_last_modified_time(file_path)
