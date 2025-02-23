import os

def rename_file(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed {old_name} to {new_name}")
    else:
        print(f"File {old_name} not found.")

old_name = input("Enter the old file name: ")
new_name = input("Enter the new file name: ")
rename_file(old_name, new_name)
