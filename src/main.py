import pdf
import tkinter
import items
from utils import gui, file

def OpenGUI():
    pass

def UpdatePDF():
    pdf.AddPage()
    pdf.Output('PDF.pdf')

def Main():
    OpenGUI()
    UpdatePDF()

if __name__ == '__main__':
    Main()