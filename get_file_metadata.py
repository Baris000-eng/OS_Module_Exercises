import os
import time

def get_file_metadata(file_path):
    if os.path.exists(file_path):
        # Get the file statistics
        stat_info = os.stat(file_path)

        # Birth time is the actual creation time (if available)
        birth_time = time.ctime(stat_info.st_birthtime) if hasattr(stat_info, 'st_birthtime') else "N/A"
        
        # Change time (metadata change time) - last time the file metadata or content was modified
        change_time = time.ctime(stat_info.st_ctime)
        
        # Output the times clearly
        print(f"File created: {birth_time}")  # Birth time is creation time
        print(f"File is last modified at: {change_time}")  # Change time is the last metadata or content change
    else:
        print(f"File {file_path} does not exist.")

# Input the file path from the user
file_path = input("Enter the file path: ")
get_file_metadata(file_path)

