from fpdf import FPDF


def Main():
    # PDF object
    pdf = FPDF('P', 'mm', 'Letter')

    # Add a page
    pdf.add_page()

    # Specify font
    pdf.set_font('helvetica', '', 16)

    # Add text
    pdf.cell(0, 20, '1')
    pdf.ln(5)
    pdf.cell(0, 40, '2')

    # Create PDF file
    pdf.output('PDF.pdf')

if __name__ == '__main__':
    Main()