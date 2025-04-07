import PDF

def Main():
    # ------ INITIALIZE ------
    PDF.SetFont('helvetica', 16)

    # ------ PAGE 1 ------
    PDF.AddPage()
    PDF.AddText('This is page 1!', (0, 50))

    # ------ PAGE 2 ------
    PDF.AddPage()
    PDF.AddText('This is page 2!', (0, 50))

    # ------ CREATE PDF ------
    PDF.Create('PDF.pdf')

if __name__ == '__main__':
    Main()