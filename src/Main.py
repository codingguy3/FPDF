import PDF

def Main():
    # ------ INITIALIZE ------
    PDF.SetFont('helvetica', 16)

    # ------ PAGE 1 ------
    PDF.AddPage()
    for i in range(1, 16):
        PDF.AddText(f'Line {i}', 22)
        PDF.AddLine()

    # ------ PAGE 2 ------
    PDF.AddPage()
    for i in range(1, 16):
        PDF.AddBox(f'Line {i}', 22)
        PDF.AddLine()

    # ------ PAGE 3 ------
    PDF.AddPage()
    for i in range(1, 16):
        PDF.AddText(f'Line {i}', 22, centered=True)
        PDF.AddLine()

    # ------ PAGE 4 ------
    PDF.AddPage()
    for i in range(1, 16):
        PDF.AddBox(f'Line {i}', 22, centered=True)
        PDF.AddLine()

    # ------ CREATE PDF ------
    PDF.Create('PDF.pdf')

if __name__ == '__main__':
    Main()