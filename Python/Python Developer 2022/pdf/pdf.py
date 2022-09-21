import PyPDF2
import os

pdfFile = os.path.join(os.getcwd(), 'Python/Python Developer 2022/pdf/dummy.pdf')

with open(pdfFile, 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    text = page.extract_text()
    print(text)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)