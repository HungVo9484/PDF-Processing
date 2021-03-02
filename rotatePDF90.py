#----------------Rotates a page clockwise by increments of 90 degrees---------------
#Syntax: python3 rotatePDF90.py pdffile
import PyPDF2
import sys

def rotatePDF90(filename):
    '''
    Rotates a page clockwise by increments of 90 degrees
    '''
    with open(filename, 'rb') as pdffile:
        # Initialize PDF reader and PDF writer
        reader = PyPDF2.PdfFileReader(pdffile)
        writer = PyPDF2.PdfFileWriter()
        
        # Loop through all PDF pages
        for page_num in range(reader.getNumPages()):
            # Rotate each page
            PDF_page = reader.getPage(page_num)
            PDF_page.rotateClockwise(90)

            # Add the page rotated to PDF writer
            writer.addPage(PDF_page)

        # Write the PDF writer to a new file    
        with open('rotated_'+filename, 'wb') as pdffile_rotated:
            writer.write(pdffile_rotated)
            print('Successfully')

if __name__ == '__main__':
    # Get PDF file name from Command Line Arguments
    pdffile = sys.argv[1]
    rotatePDF90(pdffile)
