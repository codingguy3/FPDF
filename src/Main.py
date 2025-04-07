import PDF

FONT_SIZE = 11

def Main():
    # ------ GET INPUT ------
    income = int (input('Enter income: $'))
    expenses = int (input('Enter expenses: $'))
    profit = income - expenses

    # ------ PAGE DETAILS ------
    PDF.AddPage()

    PDF.SetFont('helvetica', FONT_SIZE, 'B')
    PDF.AddText('Apple Inc.', 20, centered=True)

    PDF.AddLine(16)

    PDF.AddText('CONDENSED CONSOLIDATED STATEMENTS OF OPERATIONS (Unaudited)', 143, centered=True)
    PDF.AddLine(FONT_SIZE)

    PDF.SetFont('helvetica', FONT_SIZE)
    PDF.AddText('(In millions, except number of shares, which are reflected in thousands, and per-share amounts)', 167, centered=True)

    PDF.AddLine(FONT_SIZE)
    PDF.AddLine(FONT_SIZE)
    PDF.AddLine(FONT_SIZE)

    PDF.AddText(f'Income: ${income}', 32)
    PDF.AddLine(FONT_SIZE)

    PDF.AddText(f'Expenses: ${expenses}', 32)
    PDF.AddLine(FONT_SIZE)

    PDF.AddText(f'Profit: ${profit}', 32)
    PDF.AddLine(FONT_SIZE)


    # ------ CREATE PDF ------
    PDF.Create('PDF.pdf')

if __name__ == '__main__':
    Main()