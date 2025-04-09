import a
import tkinter
import items
from utils import gui, file

def OpenGUI():
    pass

def UpdatePDF():
    a.AddPage()
    a.Output('PDF.pdf')

def Main():
    OpenGUI()
    UpdatePDF()

if __name__ == '__main__':
    Main()