from PyPDF2 import PdfFileWriter, PdfFileReader
from decouple import config


INPUT_DIR = 'assets/inputs/'
OUTPUT_DIR = 'assets/outputs/'


def pdf_decrypter(path, filename):
    '''Remove password of a single file.'''

    # Create a PdfFileWriter object
    out = PdfFileWriter()

    # Open encrypted PDF file with the PdfFileReader
    file = PdfFileReader(path+filename)

    # Store correct password in a variable password.
    password = config('PASSWORD')

    # Check if the opened file is actually Encrypted
    if file.isEncrypted:

        # If encrypted, decrypt it with the password
        file.decrypt(password)

        # Now, the file has been unlocked.
        # Iterate through every page of the file
        # and add it to our new file.
        for idx in range(file.numPages):
            # Get the page at index idx
            page = file.getPage(idx)

            # Add it to the output file
            out.addPage(page)

        # Open a new file "myfile_decrypted.pdf"
        path_new_file = OUTPUT_DIR + f'decrypt/{filename}'
        with open(path_new_file, "wb") as f:
            # Write our decrypted PDF to this file
            out.write(f)
        # Print success message when Done
        print(f"File decrypted Successfully in {path_new_file}.")

    else:
        # If file is not encrypted, print the
        # message
        print("File already decrypted.")

if __name__ == '__main__':
    filename = 'mi_archivo.pdf'
    path = INPUT_DIR+filename
    pdf_decrypter(path, filename)

