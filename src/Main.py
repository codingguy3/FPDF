import PDF

HEADER_SIZE = 16
PARAGRAPH_SIZE = 11

page_number = 0

def Header():
    PDF.SetFont('helvetica', HEADER_SIZE, 'B')
    PDF.SetX(15)
    PDF.AddText('Apple Inc.', 0, centered=True)
    PDF.AddImage('res/apple.png', (82, 9, 12, 12))

def Footer():
    global page_number
    page_number += 1

    PDF.SetFont('helvetica', PARAGRAPH_SIZE)
    PDF.SetY(-32)
    PDF.AddText(str(page_number), 0, centered=True)

def CreatePage():
    PDF.AddPage()
    Header()
    Footer()

def Main():
    # ------ PAGE 1 ------
    CreatePage()

    # ------ PAGE 2 ------
    CreatePage()

    # ------ PAGE 3 ------
    CreatePage()

    # ------ CREATE PDF ------
    PDF.Create('PDF.pdf')

if __name__ == '__main__':
    Main()