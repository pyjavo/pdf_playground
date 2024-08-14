import os

from decrypt import pdf_decrypter


INPUT_DIR = 'assets/inputs/'
OUTPUT_DIR = 'assets/outputs/'


def list_files_in_directory(directory_path):
    '''Remove password for all files inside a given directory.'''

    try:
        # List all files in the given directory
        with os.scandir(directory_path) as entries:
            for entry in entries:
                if entry.is_file():
                    pdf_decrypter(directory_path+'/', entry.name)
    except FileNotFoundError:
        print(f"The directory {directory_path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory {directory_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    directory_path = INPUT_DIR+'decrypt'
    list_files_in_directory(directory_path)

