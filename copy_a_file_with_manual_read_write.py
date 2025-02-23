import os

def copy_file(src, dest):
    if os.path.exists(src):
        with open(src, 'rb') as fsrc:
            with open(dest, 'wb') as fdest:
                fdest.write(fsrc.read())
        print(f"Copied {src} to {dest}")
    else:
        print(f"File {src} does not exist.")

src = input("Enter the source file path: ")
dest = input("Enter the destination file path: ")
copy_file(src, dest)
