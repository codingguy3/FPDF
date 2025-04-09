import PDF
import tkinter

HEADER_SIZE = 16
PARAGRAPH_SIZE = 15

ITEMS = ['iPhone', 'Airpods', 'Charger']

IPHONE_PRICE = 999.99
AIRPODS_PRICE = 499.99
CHARGER_PRICE = 99.99

iphones = None
airpods = None 
chargers = None


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

def AddData(item: str, qty: int, unit_price: int, total: int): # Numerical data
    if qty > 0:
        AddRow(item, str(qty), f'${unit_price}', f'${total}')



def GUI():
    # ------- NESTED FUNCTIONS ------
    def Print():
        for i, state in enumerate(checkboxes_states):
            if state.get() == 1:
                print(f'Item {i} ticked')

    # ------ SETUP ------
    global iphones, airpods, chargers
    gui = tkinter.Tk()
    gui.title('GUI')
    gui.iconbitmap('res/pdf_edit.ico')
    gui.geometry('250x350')
    checkboxes_states = [ tkinter.IntVar(), tkinter.IntVar(), tkinter.IntVar() ]

    # ------ CHECKBOX ------
    checkboxes = [
        tkinter.Checkbutton(gui, text='iPhone', variable=checkboxes_states[0], command=Print),
        tkinter.Checkbutton(gui, text='Airpods', variable=checkboxes_states[1], command=Print),
        tkinter.Checkbutton(gui, text='Charger', variable=checkboxes_states[2], command=Print)
        ]
    for checkbox in checkboxes:
        checkbox.pack()

    # ------ LOOP ------
    gui.mainloop()


def UpdatePDF():
    # ------ CALCULATE ------
    iphones_total = round (iphones * IPHONE_PRICE, 2)
    airpods_total = round (airpods * AIRPODS_PRICE, 2)
    charger_total = round (chargers * CHARGER_PRICE, 2)

    # ------ MAKE A PAGE ------
    CreatePage()

    # ------ CREATE A TABLE ------
    PDF.SetFont('helvetica', PARAGRAPH_SIZE, 'B')
    AddRow('ITEM', 'QTY', 'UNIT PRICE', 'TOTAL')

    PDF.SetFont('helvetica', PARAGRAPH_SIZE)
    AddData('iPhone', iphones, IPHONE_PRICE, iphones_total)
    AddData('Airpods', airpods, AIRPODS_PRICE, airpods_total)
    AddData('Charger', chargers, CHARGER_PRICE, charger_total)


    # ------ OUTPUT PDF ------
    PDF.Create('PDF.pdf')

def Main():
    GUI()
    # UpdatePDF()

if __name__ == '__main__':
    Main()