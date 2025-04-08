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

    PDF.SetFont('helvetica', PARAGRAPH_SIZE, 'BU')
    PDF.AddText('Items:', 16)
    PDF.AddLine(PARAGRAPH_SIZE)

    PDF.SetFont('helvetica', PARAGRAPH_SIZE)
    PDF.AddText('iPhone 16 (x5)', 22)


    # ------ CREATE PDF ------
    PDF.Create('PDF.pdf')

if __name__ == '__main__':
    Main()