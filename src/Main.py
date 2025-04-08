import PDF

HEADER_SIZE = 16
PARAGRAPH_SIZE = 13

def Header():
    PDF.SetFont('helvetica', HEADER_SIZE, 'B')
    PDF.SetX(15)
    PDF.AddText('Apple Inc.', 0, centered=True)
    PDF.AddImage('res/apple.png', (82, 9, 12, 12))
    PDF.AddLine(35)

def CreatePage():
    PDF.AddPage()
    Header()

def Main():
    # ------ PAGE CONTENT ------
    CreatePage()

    PDF.SetFont('helvetica', PARAGRAPH_SIZE, 'B')
    PDF.SetX(23)
    PDF.AddBox('ITEM', 60, centered=True)
    PDF.AddBox('QTY', 25, centered=True)
    PDF.AddBox('UNIT PRICE', 40, centered=True)
    PDF.AddBox('TOTAL', 40, centered=True)
    PDF.AddLine(PARAGRAPH_SIZE)

    PDF.SetFont('helvetica', PARAGRAPH_SIZE)


    # ------ CREATE PDF ------
    PDF.Create('PDF.pdf')

if __name__ == '__main__':
    Main()