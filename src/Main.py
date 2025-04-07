import PDF

def Main():
    # ------ INITIALIZE ------
    PDF.SetFont('helvetica', 16)

    # ------ PAGE 1 ------
    PDF.AddPage()
    PDF.AddText('This is page 1!', (80,12))
    PDF.AddText('Same line!', (0,12))
    PDF.AddLine()
    PDF.AddText('Description', (0,12)) # 0 just means it'll extend to the rest of the page

    # ------ PAGE 2 ------
    PDF.AddPage()
    PDF.AddText('This is page 2!', (0, 12))

    # ------ CREATE PDF ------
    PDF.Create('PDF.pdf')

if __name__ == '__main__':
    Main()