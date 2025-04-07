from fpdf import FPDF

def Main():
    # PDF object
    pdf = FPDF('P', 'mm', 'Letter')

    # Add a page
    pdf.add_page()

    # Specify font
    pdf.set_font('helvetica', '', 16)

    # Add text
    pdf.set_xy(0, 5)
    pdf.cell(0, 0, '1')

    pdf.set_xy(0, 15)
    pdf.cell(0, 0, '2')

    pdf.set_xy(0, 25)
    pdf.cell(0, 0, '3')

    # Create PDF file
    pdf.output('PDF.pdf')

if __name__ == '__main__':
    Main()