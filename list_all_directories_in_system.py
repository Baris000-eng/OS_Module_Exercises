import os
import platform

def list_all_directories(root_dir):
    """Recursively list all directories starting from the root directory."""
    number_of_directories = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            number_of_directories+=1
            print(os.path.join(dirpath, dirname))
    
    print()
    print('There are '+str(number_of_directories)+' directories in the system.')


# For Linux or Macos (often referred as darwin) operating systems , the root directory is '/'. However, for Windows,
# the root directory is 'C::'.
def get_root_directory():
    """Determine the appropriate root directory based on the operating system."""
    current_os = platform.system().lower()
    if current_os == "linux" or current_os == "darwin":
        return "/"
    elif current_os == "windows":
        return "C:\\"
    else:
        print("Unsupported OS.")
        return None

# Get the root directory based on the current OS
root_dir = get_root_directory()

if root_dir:
    print(f"Listing all directories starting from: {root_dir}")
    list_all_directories(root_dir)
