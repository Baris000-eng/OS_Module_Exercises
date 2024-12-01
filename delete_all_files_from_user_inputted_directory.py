import os

def delete_files_in_directory(directory):
    """Delete all files in the given directory (including subdirectories)."""
    try:
        # Walk through the directory tree
        for dirpath, dirnames, filenames in os.walk(directory, topdown=False):
            # Delete all files
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                try:
                    # Remove file
                    os.remove(file_path)  
                    print(f"Deleted file: {file_path}")
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")
    
    except Exception as e:
        print(f"Error with directory {directory}: {e}")


def main():
    # Ask the user for a directory to delete files from
    directory = input("Please enter the directory path to delete all files: ")

    directory = directory.strip()
    
    if os.path.isdir(directory):
        delete_files_in_directory(directory)
    else:
        print("The provided directory does not exist. Please check the path and try again.")

if __name__ == "__main__":
    main()
