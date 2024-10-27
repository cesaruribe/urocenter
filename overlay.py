import PyPDF2

def overlayFiles(basePDF,overPDF,outputPDF=None):
    basePDFReader = PyPDF2.PdfReader(open(basePDF,'rb'))
    overPDFReader = PyPDF2.PdfReader(open(overPDF,'rb'))
    overPDFPage = overPDFReader.pages[0]

    pdfWriter = PyPDF2.PdfWriter() if outputPDF else None

    for page_num in range(len(basePDFReader.pages)):
        page = basePDFReader.pages[page_num]
        page.merge_page(overPDFPage)
        if pdfWriter:
            pdfWriter.add_page(page)
        else:
            basePDFReader.pages[page_num] = page
    
    if pdfWriter:
        with open(outputPDF,'wb') as outputFile:
            pdfWriter.write(outputFile)
    else:
        with open(basePDF,'wb') as outputFile:
            basePDFReader.write(outputFile)

