from fpdf import FPDF

def GetTitle() -> str:
    pdf_title = input("Enter title for PDF: ")
    return pdf_title

def CreatePDF(title: str):
    # PDF object
    pdf = FPDF('P', 'mm', 'Letter')

    # Add a page
    pdf.add_page()

    # Specify font
    pdf.set_font('helvetica', '', 16)

    # Add text
    pdf.cell(40, 10, 'Helslo, world!')

    # Create PDF file
    fileName = title + '.pdf'
    pdf.output(fileName)

def Main():
    title = GetTitle()
    CreatePDF(title)

if __name__ == '__main__':
    Main()