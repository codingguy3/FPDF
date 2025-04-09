import PDF
import tkinter

HEADER_SIZE = 16
PARAGRAPH_SIZE = 15

PRICES = {'iPhone': 999.99, 'Airpods': 499.99, 'Charger': 99.99}

quantities = {'iPhone': 0, 'Airpods': 0, 'Charger': 0}

checkboxes_ticked = None

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

def AddData(item: str, qty: int, unit_price: int, total: int):
    if qty > 0:
        AddRow(item, str(qty), f'${unit_price}', f'${total}')

def GUI():
    def Update():
        for item in checkboxes_states:
            checkboxes_ticked[item] = checkboxes_states[item].get() == 1

    global checkboxes_ticked
    gui = tkinter.Tk()
    gui.title('GUI')
    gui.iconbitmap('res/pdf_edit.ico')
    gui.geometry('250x350')

    checkboxes_states = {item: tkinter.IntVar() for item in PRICES.keys()}
    checkboxes_ticked = {item: False for item in PRICES.keys()}

    checkboxes = [tkinter.Checkbutton(gui, text=item, variable=checkboxes_states[item], command=Update) for item in PRICES.keys()]
    
    for checkbox in checkboxes:
        checkbox.pack()

    gui.mainloop()

def UpdatePDF():
    global checkboxes_ticked, quantities

    for item in quantities.keys():
        quantities[item] = 1 if checkboxes_ticked[item] else 0
        print(f"{item}: {quantities[item]}")

    CreatePage()

    PDF.SetFont('helvetica', PARAGRAPH_SIZE, 'B')
    AddRow('ITEM', 'QTY', 'UNIT PRICE', 'TOTAL')

    PDF.SetFont('helvetica', PARAGRAPH_SIZE)
    for item in quantities.keys():
        total_price = round(quantities[item] * PRICES[item], 2)
        AddData(item, quantities[item], PRICES[item], total_price)

    PDF.Create('PDF.pdf')

def Main():
    GUI()
    UpdatePDF()

if __name__ == '__main__':
    Main()
