import PyPDF2
import sys

inputs=sys.argv[1:]

#with open ('208 dummy.pdf','rb') as file:
    #print(file)
   # reader=PyPDF2.PdfFileReader(file)
    #print(reader.numPages)

#Combine pdfs:

def pdf_combiner(pdf_list):
    merger=PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)