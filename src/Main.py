import PDF
import tkinter

HEADER_SIZE = 16
PARAGRAPH_SIZE = 15

IPHONE_PRICE = 999.99
AIRPODS_PRICE = 499.99
CHARGER_PRICE = 99.99

# Dictionaries in python:
# { Key: Value }

quantities = {'iPhone': 0, 'Airpods': 0, 'Charger': 0}

checkboxes_ticked = None

class Product:
    def __init__(self, item: str, qty: int, unit_price: float, total: float):
        self.item = item 
        self.qty = qty
        self.unit_price = unit_price
        self.total = total
        self.checkbox_ticked = False

iPhone = Product('iPhone', 0, IPHONE_PRICE, 0.00)


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

def AddData(item: str, qty: int, unit_price: float, total: float): # Numerical data
    if qty > 0:
        AddRow(item, str(qty), f'${unit_price}', f'${total}')



def GUI():
    # ------- NESTED FUNCTIONS ------
    def Update():
        for i in range(len(checkboxes_states)):
            if checkboxes_states[i].get() == 1:
                checkboxes_ticked[i] = True
            else:
                checkboxes_ticked[i] = False            

    # ------ SETUP ------
    global iphones, airpods, chargers, checkboxes_ticked
    gui = tkinter.Tk()
    gui.title('GUI')
    gui.iconbitmap('res/pdf_edit.ico')
    gui.geometry('250x350')
    checkboxes_states = [ tkinter.IntVar(), tkinter.IntVar(), tkinter.IntVar() ]
    checkboxes_ticked = [False, False, False]

    # ------ CHECKBOX ------
    checkboxes = [
        tkinter.Checkbutton(gui, text='iPhone', variable=checkboxes_states[0], command=Update),
        tkinter.Checkbutton(gui, text='Airpods', variable=checkboxes_states[1], command=Update),
        tkinter.Checkbutton(gui, text='Charger', variable=checkboxes_states[2], command=Update)
        ]
    for checkbox in checkboxes:
        checkbox.pack()

    # ------ LOOP ------
    gui.mainloop()


def UpdatePDF():
    # ------ GET QUANTITIES FROM GUI ------
    global checkboxes_ticked, quantities
    keys = list(quantities.keys())
    for i in range(len(checkboxes_ticked)):
        if checkboxes_ticked[i] == True:
            quantities[keys[i]] = 1 
        else:
            quantities[keys[i]] = 0
        print(quantities[keys[i]])

    # ------ CALCULATE ------
    iphones_total = round (quantities['iPhone'] * IPHONE_PRICE, 2)
    airpods_total = round (quantities['Airpods'] * AIRPODS_PRICE, 2)
    charger_total = round (quantities['Charger'] * CHARGER_PRICE, 2)

    data_arguments = [
        ('iPhone', quantities['iPhone'], IPHONE_PRICE, iphones_total),
        ('Airpods', quantities['Airpods'], AIRPODS_PRICE, airpods_total),
        ('Charger', quantities['Charger'], CHARGER_PRICE, charger_total)
    ]

    # ------ MAKE A PAGE ------
    CreatePage()

    # ------ CREATE A TABLE ------
    PDF.SetFont('helvetica', PARAGRAPH_SIZE, 'B')
    AddRow('ITEM', 'QTY', 'UNIT PRICE', 'TOTAL')

    PDF.SetFont('helvetica', PARAGRAPH_SIZE)
    for i in range(len(checkboxes_ticked)):
        AddData(*data_arguments[i])


    # ------ OUTPUT PDF ------
    PDF.Create('PDF.pdf')

def Main():
    GUI()
    UpdatePDF()

if __name__ == '__main__':
    Main()