from fpdf import FPDF

def Main():
    # PDF object
    pdf = FPDF('P', 'mm', 'Letter')

    # Add a page
    pdf.add_page()

    # Specify font
    pdf.set_font('helvetica', '', 16)

    # Add text
    pdf.cell(40, 10, 'Hello, world!')

    # Create PDF file
    pdf.output('PDF.pdf')

if __name__ == '__main__':
    Main()