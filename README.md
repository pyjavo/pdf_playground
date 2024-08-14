# PDF Jargon 0.1

Jugar con archivos PDFs en Python para desencriptarlos o dividirlos

Este proyecto corre en Python 3.9.

- decrypt.py recibe un PDF con contraseña y devuelve uno sin contraseña
- main.py separa un PDF de múltiples páginas en varios archivos PDF. Uno por página.

## Run locally

1. Create .env file with your secret password. See `.env.sample` for an example
2. Make sure the assets/ directory is created successfully
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run your desired script

## To DOs:
1. Make a try/except or a bash file that validades "mi_archivo.pdf" exists before running the script
2. Allow decrypt_pdfs.py to receive the file name as an argument (also add a shebang)
3. Same as before for the main.py file
