import os
import time

def get_creation_time(file_path):
    if os.path.exists(file_path):
        timestamp = os.path.getctime(file_path)
        print(f"Creation time: {time.ctime(timestamp)}")
    else:
        print(f"File {file_path} does not exist.")

file_path = input("Enter the file path: ")
get_creation_time(file_path)
