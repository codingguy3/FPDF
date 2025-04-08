import PDF

HEADER_SIZE = 16
PARAGRAPH_SIZE = 15

def Header():
    PDF.SetFont('helvetica', HEADER_SIZE, 'B')
    PDF.SetX(15)
    PDF.AddText('Apple Inc.', 0, centered=True)
    PDF.AddImage('res/apple.png', (82, 9, 12, 12))
    PDF.AddLine(25)

def CreatePage():
    PDF.AddPage()
    Header()

def AddRow(str1: str, str2: str, str3: str, str4: str):
    PDF.SetX(23)
    PDF.AddBox(str1, 60, centered=True)
    PDF.AddBox(str2, 25, centered=True)
    PDF.AddBox(str3, 40, centered=True)
    PDF.AddBox(str4, 40, centered=True)
    PDF.AddLine(12)

def Main():
    # ------ MAKE A PAGE ------
    CreatePage()

    # ------ CREATE A TABLE ------
    PDF.SetFont('helvetica', PARAGRAPH_SIZE, 'B')
    AddRow('ITEM', 'QTY', 'UNIT PRICE', 'TOTAL')

    PDF.SetFont('helvetica', PARAGRAPH_SIZE)
    AddRow('iPhone 16', '3', '$12.50', '$37.50')
    AddRow('iPhone 16', '3', '$12.50', '$37.50')
    AddRow('iPhone 16', '3', '$12.50', '$37.50')
    AddRow('iPhone 16', '3', '$12.50', '$37.50')
    AddRow('iPhone 16', '3', '$12.50', '$37.50')
    AddRow('iPhone 16', '3', '$12.50', '$37.50')


    # ------ OUTPUT PDF ------
    PDF.Create('PDF.pdf')

if __name__ == '__main__':
    Main()