import os

def get_home_directory():
    home_directory = os.path.expanduser("~")
    print(f"Home directory: {home_directory}")

get_home_directory()
