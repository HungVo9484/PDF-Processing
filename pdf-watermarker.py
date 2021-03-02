#-------------------Add watermark to PDF file------------------------
# Syntax: $python3 pdf-watermarker.py template watermark

import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def pdfWatermarker(pdf_file, watermark_file):
    template = PdfFileReader(open(pdf_file, 'rb'))
    watermark = PdfFileReader(open(watermark_file, 'rb'))
    output = PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)
    
    with open('watermarked_'+pdf_file, 'wb') as file:
        output.write(file)
    print('Successfully')

if __name__ == '__main__':
    pdf_file = sys.argv[1]
    watermark_file = sys.argv[2]
    pdfWatermarker(pdf_file, watermark_file)