import PDF

def Main():
    # ------ INITIALIZE ------
    PDF.SetFont('helvetica', 16)

    # ------ PAGE 1 ------
    PDF.AddPage()
    PDF.AddBox('Welcome to my PDF', 54, centered=True)
    PDF.AddLine()
    PDF.AddText('This is page 1!', 80)
    PDF.AddText('Same line!', 90)
    PDF.AddText('Final words', 0)
    PDF.AddLine()
    PDF.AddText('Description', 0) 
    PDF.AddLine()
    PDF.AddBox('Sample box', 32)

    # ------ PAGE 2 ------
    PDF.AddPage()
    PDF.AddText('This is page 2!', 0)

    # ------ CREATE PDF ------
    PDF.Create('PDF.pdf')

if __name__ == '__main__':
    Main()