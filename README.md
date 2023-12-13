# PDF Jargon 0.1

Jugar con archivos PDFs en Python para desencriptarlos o dividirlos

Este proyecto corre en Python 3.9.

- decrypt_pdfs.py recibe un PDF con contraseña y devuelve uno sin contraseña
- main.py separa un PDF de múltiples páginas en varios archivos PDF. Uno por página.


## To DOs:
1. User environment variables to set a password in decrypt_pdfs
2. Make a try/except or a bash file that validades "mi_archivo.pdf" exists before running the script
3. Make a directory destination for decrypted files
4. Allow decrypt_pdfs.py to receive the file name as an argument (also add a shebang)
5. Same as before for the main.py file
