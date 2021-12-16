import os
import PyPDF2

def pdf_merger():
    # create a name that will store all the merged files
    NEW_FILE_NAME = "Merged_Files.pdf"

    pdf_writer = PyPDF2.PdfFileWriter()

    # get the path for the pdfs; change per class folder
    path = os.path.join(os.getcwd(), "pdfs\\")

    # read all the files in the same directory
    for filename in os.listdir(path):

        name, extension = os.path.splitext(filename)
        # if the page is a pdf type file then access
        if (extension == ".pdf"):
            filePath = os.path.join(path, filename)
            pdf_reader = PyPDF2.PdfFileReader(filePath)
            # access every file, and access it page by page
            for page in range(pdf_reader.getNumPages()):
                # append this page to the documented the will be merged
                pdf_writer.addPage(pdf_reader.getPage(page))

    # write the merged pdf to a file
    with open(NEW_FILE_NAME, "wb") as out:
        pdf_writer.write(out)


if __name__ == "__main__":
    pdf_merger()