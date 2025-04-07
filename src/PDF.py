from fpdf import FPDF

pdf = FPDF('P', 'mm', 'Letter')

def SetFont(font: str, size: int):
    pdf.set_font(font, '', size)

def AddPage():
    pdf.add_page()

def AddText(text: str, position: tuple[int, int]):
    pdf.set_xy(*position) 
    pdf.cell(0, 0, text)

def Create(title: str):
    pdf.output(title)