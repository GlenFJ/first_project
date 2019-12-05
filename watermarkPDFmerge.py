import PyPDF2

template=PyPDF2.PdfFileReader(open('208 super.pdf','rb'))
output=PyPDF2.PdfFileWriter()
watermark=PyPDF2.PdfFileReader(open('208 wtr.pdf','rb'))

for i in range(template.getNumPages()):
    page=template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf','wb') as file:
        output.write(file)




