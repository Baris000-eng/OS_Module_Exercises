import os

def find_files_with_extension(extension, directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(extension):
                print(os.path.join(dirpath, filename))

find_files_with_extension('.txt', '/path/to/directory')
