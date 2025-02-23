import os

def organize_files_by_extension(directory):
    if not os.path.exists(directory):
        print("The directory does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(filename)[1][1:]

        if file_extension:
            extension_folder = os.path.join(directory, file_extension)
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)

            new_file_path = os.path.join(extension_folder, filename)
            os.rename(file_path, new_file_path)
            print(f'Moved: {filename} to {extension_folder}')
        else:
            print(f"Skipping file without extension: {filename}")

directory = input("Enter the path of the directory to organize: ")
organize_files_by_extension(directory)
