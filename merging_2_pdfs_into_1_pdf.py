from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF4 import PdfFileWriter, PdfFileReader, PdfFileMerger
import io
import pikepdf
from fpdf import FPDF

class MergeTwoPDFs:
    def __init__(self, input_path, output_path, image):
        self.input_path=input_path
        self.output_path=output_path
        self.image=image
        with open(self.input_path,'rb') as file:
            pdfReader = PdfFileReader(file)
            self.totalPages = pdfReader.numPages

    def Approach1(self):
        mergedObject = PdfFileMerger()

        for i in range(self.totalPages):
            # print(i)
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            can.setFontSize(10) 
            can.drawString(240,647,"Souvik")
            can.drawImage(self.image, 350, 395,width=55,height=30)
            can.save()
            packet.seek(0)
            new_pdf = PdfFileReader(packet)
            existing_pdf = PdfFileReader(open(self.input_path, "rb"))
            output = PdfFileWriter()
            page = existing_pdf.getPage(i)
            page.mergePage(new_pdf.getPage(0))
            output.addPage(page)
            outputStream = open("dump/destination"+str(i)+".pdf", "wb")
            output.write(outputStream)
            outputStream.close()
            mergedObject.append(PdfFileReader("dump/destination"+str(i)+".pdf", "rb"), import_bookmarks=False)

        mergedObject.write(self.output_path)

    def _mergeApproach1(self):
        pdf_reader = PdfFileReader(self.input_path) 
        pdf_reader_created = PdfFileReader("dump/destination.pdf") 
        pdf_writer = PdfFileWriter() 

        for page_no in range(self.totalPages): 
            page_obj = pdf_reader.getPage(page_no)
            page_obj_created = pdf_reader_created.getPage(page_no)
            page_obj.mergePage(page_obj_created)
            pdf_writer.addPage(page_obj)

        with open(self.output_path,'wb') as out:
            pdf_writer.write(out) 
        return True

    def _mergeApproach2(self):
        pdf1 = pikepdf.Pdf.open(self.input_path)
        pdf2 = pikepdf.Pdf.open("dump/destination.pdf")
        for page_no in range(self.totalPages):
            pikepdf.Page(pdf1.pages[page_no]).add_overlay(pikepdf.Page(pdf2.pages[page_no]))

        pdf1.save(self.output_path)
        return True

    def Approach2(self, merge_approach=None):
        can = canvas.Canvas('dump/destination.pdf', pagesize=letter)
        for i in range(self.totalPages):
            # print(i)
            can.setFontSize(10) 
            can.drawString(100,20,"Souvik")
            can.drawImage(self.image, 350, 395,width=55,height=30)
            can.showPage()
        can.save()

        if merge_approach == 1:
            return self._mergeApproach1()
        else:
            return self._mergeApproach2()

    def Approach3(self, merge_approach=None):
        pdf = FPDF()
        for page_no in range(self.totalPages):
            pdf.add_page()
            pdf.image(self.image, x=10, y=10, w=55, h=30)
            pdf.set_font('Arial', 'B', 8)
            pdf.y = 260
            pdf.x = 10
            pdf.cell(10, 10,"Souvik")

        pdf.output("dump/destination.pdf")

        if merge_approach == 1:
            return self._mergeApproach1()
        else:
            return self._mergeApproach2()

def main():
    obj = MergeTwoPDFs('input/sample.pdf', "output/output.pdf", "images/image.jpeg")
    # obj.Approach1()

    # obj.Approach2()
    # obj.Approach2(merge_approach = 1)
    
    obj.Approach3()
    # obj.Approach3(merge_approach = 1)

if __name__ == '__main__':
    main()