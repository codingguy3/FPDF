from fpdf import FPDF

PDF = FPDF('P', 'mm', 'Letter')

def SetFont(font: str, size: int, style: str = ''):
    PDF.set_font(font, style, size)

def AddPage():
    PDF.add_page()

def SetX(x: int):
    PDF.set_x(x)

def SetY(y: int):
    PDF.set_y(y)

def SetXY(xy: int):
    PDF.set_xy(xy)

def AddText(text: str, width: int, centered: bool = False):
    if centered:
        PDF.cell(width, 12, text, align='C')
    else:
        PDF.cell(width, 12, text)

def AddBox(text: str, width: int, centered: bool = False):
    if centered:
        PDF.cell(width, 12, text, border=True, align='C')
    else:
        PDF.cell(width, 12, text, border=True)

def AddImage(filePath: str, properties: tuple[int, int, int, int]):
    PDF.image(filePath, *properties)

def AddLine(font_size: int):
    PDF.ln(font_size)

def AddDivider():
    SetFont('helvetica', 16, 'B')
    AddText('_______________________________________________________', 175, centered=True)

def Output(title: str):
    PDF.output(title)