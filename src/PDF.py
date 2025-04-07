from fpdf import FPDF

pdf = FPDF('P', 'mm', 'Letter')

def SetFont(font: str, size: int, style: str = ''):
    pdf.set_font(font, style, size)

def AddPage():
    pdf.add_page()

def AddText(text: str, width: int, centered: bool = False):
    if centered:
        pdf.cell(width, 12, text, center=True)
    else:
        pdf.cell(width, 12, text)

def AddBox(text: str, width: int, centered: bool = False):
    if centered:
        pdf.cell(width, 12, text, border=True, center=True)
    else:
        pdf.cell(width, 12, text, border=True)

def AddImage(filePath: str, properties: tuple[int, int, int, int]):
    pdf.image(filePath, *properties)

def AddLine(font_size: int):
    pdf.ln(font_size * 1/2)

def AddDivider():
    SetFont('helvetica', 16, 'B')
    AddText('_______________________________________________________', 175, centered=True)

def Create(title: str):
    pdf.output(title)