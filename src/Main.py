import PDF

def Main():
    # ------ PAGE DETAILS ------
    PDF.AddPage()

    PDF.SetFont('helvetica', 16)
    PDF.AddText('Hey!', 15)
    PDF.AddLine()

    PDF.SetFont('helvetica', 16, 'B')
    PDF.AddText('Hey!', 15)
    PDF.AddLine()

    PDF.AddText('_______________________________________________________', 175, centered=True)

    # ------ CREATE PDF ------
    PDF.Create('PDF.pdf')

if __name__ == '__main__':
    Main()