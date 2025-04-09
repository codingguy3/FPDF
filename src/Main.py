import pdf
import tkinter
from utils import gui, file
import items

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