import shutil

def copy_file(src, dest):
    shutil.copy(src, dest)
    print(f"Copied {src} to {dest}")

src = input("Enter the source file path: ")
dest = input("Enter the destination file path: ")
copy_file(src, dest)
