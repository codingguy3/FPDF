import PDF

def Main():
    # ------ PAGE DETAILS ------
    PDF.AddPage()

    PDF.SetFont('helvetica', 16)
    PDF.AddBox('Hey!', 15)
    PDF.AddLine()

    PDF.SetFont('helvetica', 16, 'B')
    PDF.AddBox('Hey!', 15)
    PDF.AddLine()

    # ------ CREATE PDF ------
    PDF.Create('PDF.pdf')

if __name__ == '__main__':
    Main()