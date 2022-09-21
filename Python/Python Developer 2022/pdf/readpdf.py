import os
from pdfreader import SimplePDFViewer

pdfFile = os.path.join(os.getcwd(), 'Python/Python Developer 2022/pdf/dummy.pdf')
fd = open(pdfFile, 'rb')
viewer = SimplePDFViewer(fd)
viewer.render()
print(viewer.canvas.strings)
