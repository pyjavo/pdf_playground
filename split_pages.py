#!/usr/bin/env python3

import sys
import os
from PyPDF2 import PdfFileReader, PdfFileWriter



INPUT_DIR = 'assets/inputs/'
OUTPUT_DIR = 'assets/outputs/'


def pdf_splitter(filename):
    #filename = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(INPUT_DIR+'splits/'+filename)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output_filename = OUTPUT_DIR +'splits/' + f'{filename}_page_{page+1}.pdf'

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Successfully splitted: {}'.format(output_filename))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename.pdf>")
        sys.exit(1)

    filename = sys.argv[1]
    pdf_splitter(filename)

