import PyPDF2
import PyPDF2 


def learn_py_pdf():
    with open('files/dummy.pdf', 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(len(reader.pages))
        page = reader.pages[0]
        page.rotate(180)
        # writing rotated file
        writer = PyPDF2.PdfWriter()
        # adding the rotated page
        writer.add_page(page)
        with open('tilt.pdf', 'wb') as new_file:
            writer.write(new_file)
            
    return


learn_py_pdf()


# exercise combine pdfs we want to combine two pdfs to form one 

'''
so we pass in the terminal 
pdf.py dummy.pdf twopage.pdf tilt.pdf 
as many as we like 

'''

import sys 
import os 
# this grabs all arguments except the file name
inputs = sys.argv[1:]

# so we create a function pdf combine which takes pdf list 'a list of our pdf inputs'
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        file = os.path.join(os.getcwd(), 'files', pdf)
        merger.append(file)
    
    merger.write('super_merged.pdf')
        
        
        
# pdf_combiner(inputs)

# exercise watermark
# a tool that watermark my super_merged pdf use the wtr.pdf to watermark all the pages of the super merged pdf


# open the pdf and watermark file 
def watermark_super():
    watermark_path  = os.path.join(os.getcwd(), 'files', 'wtr.pdf')
    file_to_watermark_path = le = os.path.join(os.getcwd(), 'files', 'super_merged.pdf')
    
    with open(file_to_watermark_path, 'rb') as main_file:
        main_file_read = PyPDF2.PdfReader(main_file)
        with open(watermark_path, 'rb') as watermark:
            watermark_file = PyPDF2.PdfReader(watermark)
            # get watemark page
            watermark_page = watermark_file.pages[0]
            
            # create a new pdf writer object
            pdf_writer = PyPDF2.PdfWriter()
            
            # Iterate through each page in the PDF file
            for page_num in range(len(main_file_read.pages)):
                page = main_file_read.pages[page_num]
                # Merge the watermark with the current page
                page.merge_page(watermark_page)
                # Add the merged page to the PdfFileWriter object
                pdf_writer.add_page(page)
            # Write the watermarked PDF to a new file
            with open('output_watermarked.pdf', 'wb') as output_file:
                pdf_writer.write(output_file)
                
                
        return 
    
    
watermark_super()


# his way

# template = PyPDF2.PdfFileReader(open('superduper.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('water.pdf', 'rb'))
# output = PyPDF2.PdfFileWriter()
# This is the new way to do this:
template = PyPDF2.PdfReader(open('superduper.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('water.pdf', 'rb'))
output = PyPDF2.PdfWriter()


# for i in range(template.getNumPages()):
# New way to do this:
for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

with open('watermaked_output.pdf', 'wb') as outputFile:
    output.write(outputFile)

