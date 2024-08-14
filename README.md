# PDF Jargon 0.1

Play with PDF files in Python.

For now it decrypt and split files.

Runs with Python 3.9 or greater.

- decrypt.py receives a PDF locked with a password and returns the same file unlocked.
- split_pages.py splits the pages of a PDF file in multiple files. One file per page.

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
2. Allow decrypt.py to receive the file name as an argument (also add a shebang)
3. Same as before for the main.py file
4. Create a config file that manages the directory structure information (thinking in JSON).
