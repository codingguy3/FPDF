import PDF

FONT_SIZE = 11

def Main():
    # ------ PAGE DETAILS ------
    PDF.AddPage()

    PDF.SetFont('helvetica', FONT_SIZE, 'B')
    PDF.AddText('Apple Inc.', 20, centered=True)

    PDF.AddLine(16)

    PDF.AddText('CONDENSED CONSOLIDATED STATEMENTS OF OPERATIONS (Unaudited)', 143, centered=True)
    PDF.AddLine(FONT_SIZE)

    PDF.SetFont('helvetica', FONT_SIZE)
    PDF.AddText('(In millions, except number of shares, which are reflected in thousands, and per-share amounts)', 167, centered=True)

    # ------ CREATE PDF ------
    PDF.Create('PDF.pdf')

if __name__ == '__main__':
    Main()