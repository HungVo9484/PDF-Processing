# -----PdfFileMerger merges multiple PDFs into a single PDF---------------------
# Syntax: $python3 mergePDF.py pdf_file1 pdf_file2 pdf_file3 ...

import sys
from PyPDF2 import PdfFileMerger

def mergePDFs(files_list):
    # Create merge object
    merge = PdfFileMerger()

    # Loop through all the pdf files and concatiate to merge
    for pdf_file in files_list:
        merge.append(pdf_file)
    
    # Write the pdf output file
    merge.write('pdf-output.pdf')
    print('Succesfully')
    merge.close()

if __name__ == '__main__':
    files_list = sys.argv[1:]
    print(files_list)
    mergePDFs(files_list)

