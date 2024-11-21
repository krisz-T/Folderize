import os
import shutil
import string
import argparse

def sort_files_by_letter(directory, create_all_folders):
    files = [f for f in os.listdir(directory) 
             if os.path.isfile(os.path.join(directory, f)) and f != os.path.basename(__file__)]
    
    if create_all_folders:
        for letter in string.ascii_uppercase:
            folder_path = os.path.join(directory, letter)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
    else:
        used_letters = set()
        for file in files:
            first_letter = file[0].upper()
            if first_letter in string.ascii_uppercase and first_letter not in used_letters:
                folder_path = os.path.join(directory, first_letter)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                used_letters.add(first_letter)
    
    for file in files:
        first_letter = file[0].upper()
        if first_letter in string.ascii_uppercase:
            source = os.path.join(directory, file)
            destination = os.path.join(directory, first_letter, file)
            shutil.move(source, destination)
            print(f"Moved: {file} to {first_letter}/")

def delete_script(script_path):
    """Delete the script after execution if requested."""
    try:
        os.remove(script_path)
        print("Script deleted successfully.")
    except Exception as e:
        print(f"Error deleting script: {e}")

def main():
    parser = argparse.ArgumentParser(description="Sort files in the current directory into folders based on the first letter.")
    parser.add_argument('--necessary', action='store_true', help="Create only necessary folders based on file names.")
    parser.add_argument('--delete', action='store_true', help="Delete the script after execution.")
    
    args = parser.parse_args()

    current_directory = os.getcwd()

    sort_files_by_letter(current_directory, create_all_folders=not args.necessary)

    if args.delete:
        script_path = os.path.abspath(__file__)
        delete_script(script_path)

if __name__ == "__main__":
    main()
