import PDF

FONT_SIZE = 11

page_number = 0

def Footer():
    global page_number
    page_number += 1

    PDF.SetFont('helvetica', FONT_SIZE)
    PDF.SetY(-32)
    PDF.AddText(str(page_number), 0, centered=True)

def CreatePage():
    PDF.AddPage()
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