import os

def check_exists(path):
    if os.path.exists(path):
        print(f"{path} exists.")
    else:
        print(f"{path} does not exist.")

path = input("Enter the path to check: ")
check_exists(path)
