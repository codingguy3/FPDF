from fpdf import FPDF

pdf = FPDF('P', 'mm', 'Letter')

def SetFont(font: str, size: int):
    pdf.set_font(font, '', size)

def AddPage():
    pdf.add_page()

def AddText(text: str, position: tuple[int, int]):
    pdf.cell(*position, text, border=True)

def AddLine():
    pdf.ln(12)

def Create(title: str):
    pdf.output(title)