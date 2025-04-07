from fpdf import FPDF

# test

# Global PDF object
pdf = FPDF('P', 'mm', 'Letter')

def AddText(text: str, position: tuple[int, int]):
    pdf.set_xy(*position) # This just does pdf.set_xy(position[0], position[1])
    pdf.cell(0, 0, text)

def Main():
    # Add a page
    pdf.add_page()

    # Specify font
    pdf.set_font('helvetica', '', 16)

    # Add text
    AddText('Line 1', (0, 5))
    AddText('Line 2', (0, 15))
    AddText('Line 3', (0, 25))

    # Create PDF file
    pdf.output('PDF.pdf')

if __name__ == '__main__':
    Main()