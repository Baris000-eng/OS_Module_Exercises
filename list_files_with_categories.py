import os 
import platform 


os.environ["VSCODE_ENABLE_FILE_ACCESS"] = "true"


def get_root_directory():
    """Determine the appropriate root directory based on the operating system."""
    current_os = platform.system().lower()
    if current_os == "linux" or current_os == "darwin":
        return "/"
    elif current_os == "windows":
        return "C:\\"
    else:
        print("Unsupported OS.")
        return None

root_directory = get_root_directory()
txt_files = list()
csv_files = list()
powerpoint_files = list() 
word_files = list() 
excel_files = list() 

for dirpath, dirnames, filenames in os.walk(root_directory):
    for filename in filenames: 
        filename = filename.lower().strip()
        if filename.endswith('.txt'): 
            txt_files.append(filename)
        elif filename.endswith('.csv'):
            csv_files.append(filename)
        elif filename.endswith('.ppt') or filename.endswith('.pptx'): 
            powerpoint_files.append(filename) 
        elif filename.endswith('.doc') or filename.endswith('.docx'):
            word_files.append(filename) 
        elif filename.endswith('.xlsx') or filename.endswith('.xls'):
            excel_files.append(filename)


print()
print()
print('There are '+str(len(txt_files))+' txt files in the current local computer/system.') 
print('There are '+str(len(csv_files))+' csv files in the current local computer/system.') 
print('There are '+str(len(powerpoint_files))+' powerpoint files in the current local computer/system.')
print('There are '+str(len(word_files))+' word files in the current local computer/system.') 
print('There are '+str(len(excel_files))+' excel files in the current local computer/system.') 
print()
print()
