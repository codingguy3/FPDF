import PDF

FONT_SIZE = 12

def Main():
    # ------ PAGE DETAILS ------
    PDF.AddPage()

    PDF.SetFont('helvetica', FONT_SIZE)
    PDF.AddText('Hey!', 15)
    PDF.AddLine(FONT_SIZE)

    PDF.SetFont('helvetica', FONT_SIZE, 'B')
    PDF.AddText('Hey!', 15)
    PDF.AddLine(FONT_SIZE)

    PDF.AddDivider()

    # ------ CREATE PDF ------
    PDF.Create('PDF.pdf')

if __name__ == '__main__':
    Main()