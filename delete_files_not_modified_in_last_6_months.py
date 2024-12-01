import os
import time

def delete_old_files(directory, months=6):
    """Delete files in the given directory (and subdirectories) that haven't been modified in the last 'months'."""

    # Calculate the time threshold (6 months ago)
    current_time = time.time()
    time_6_months_ago = current_time - (months * 30 * 24 * 60 * 60)  

    try:
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)

                try:
                    # Get the last modification time of the file
                    file_modification_time = os.path.getmtime(file_path)

                    # Check if the file is older than the time 6 months ago
                    if file_modification_time < time_6_months_ago:

                        # Delete the file
                        os.remove(file_path)  
                        print(f"Deleted old file: {file_path}")
                except Exception as e:
                    print(f"Error accessing or deleting {file_path}: {e}")
    
    except Exception as e:
        print(f"Error walking through the directory {directory}: {e}")

def main():
    # Ask the user for a directory to delete old files from
    directory = input("Please enter the directory path to delete old files: ")

    directory = directory.strip()
    
    if os.path.isdir(directory):
        delete_old_files(directory)
    else:
        print("The provided directory does not exist. Please check the path and try again.")

# Run the script
if __name__ == "__main__":
    main()
