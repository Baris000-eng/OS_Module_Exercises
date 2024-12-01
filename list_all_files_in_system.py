import os 


def list_all_files(input_path):
    file_number = 0
    for root, dirs, files in os.walk(input_path): 
        for file in files: 
            file_number+=1
            print(os.path.join(root, file))

    print()
    print('There are '+str(file_number)+' files in the system.\n')



directory_to_traverse = '/'
list_all_files(directory_to_traverse)