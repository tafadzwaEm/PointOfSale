from tkinter import *
from tkinter import messagebox
import sqlite3


POSScreen = Tk()
POSScreen.title("Point Of Sale")
POSScreen.attributes("-fullscreen",True)
conn = sqlite3.connect('db/stock.db')
c = conn.cursor()
c.execute("SELECT * FROM products")
productList = []
records = c.fetchall()
for record in records:
    productList.append(record[0])
conn.close()


# Creating a frame for displaying items bought
itemsFrame = Frame(POSScreen,relief=SUNKEN,bd=3,bg="white",width=700,height=500)
totalCostFrame = Frame(POSScreen,width=300,height=100)

items = []
priceList = []
# global itemsCounter
# itemsCounter = 1
# totalCostVar = Label(totalCostFrame,text=int(sum(priceList)),font=('Roboto',30,'bold'))
def addSelected():
    item =  str(clicked.get())
    items.append(item)
    itemsCounter = 1
    for i in items:
        conn = sqlite3.connect("db/stock.db")
        c = conn.cursor()
        c.execute("SELECT * FROM products")
        productPrice = " "
        records = c.fetchall()
        for record in records:
            if record[0] == i:
                productPrice = str(record[2])
        itemsCounter += 1
    priceList.append(int(productPrice))
    print(priceList)

    itemName = Label(itemsFrame,text=i,font=("Roboto",14,"bold"),bg="white")
    itemPrice = Label(itemsFrame,text="$ "+str(productPrice),font=("Roboto",14,"bold"),bg="white")
    totalCostVar = Label(totalCostFrame,text=int(sum(priceList)),font=('Roboto',30,'bold'))
    totalCostVar.grid(row=0,column=2,pady=(10,40))
    itemName.grid(row=itemsCounter,column=0,pady=10,padx=(10,0),sticky=W)
    itemPrice.grid(row=itemsCounter,column=2,pady=10,padx=(10,0))
    itemsCounter += 1
    
clicked = StringVar()
listOfProducts = OptionMenu(POSScreen,clicked,*productList)
addSelectedBtn = Button(POSScreen,text="Add Selected",command=addSelected)
#
topLabelText = "Item \t\t\t Quantity \t Amount($)"
topLabel = Label(itemsFrame,text=topLabelText,font=("Roboto",17,"bold"))
# middleFrame = Frame(POSScreen,width=300,relief=SUNKEN,bd=3)

# Creating a frame for displaying total cost amount

totalCostLabel = Label(totalCostFrame,text="TOTAL COST:",font=('Roboto',30,'bold'))


button1 = Button(totalCostFrame,text="1",font=('Roboto',20,'bold'),padx=40,pady=20)
button2 = Button(totalCostFrame,text="2",font=('Roboto',20,'bold'),padx=40,pady=20)
button3 = Button(totalCostFrame,text="3",font=('Roboto',20,'bold'),padx=40,pady=20)
button4 = Button(totalCostFrame,text="4",font=('Roboto',20,'bold'),padx=40,pady=20)
button5 = Button(totalCostFrame,text="5",font=('Roboto',20,'bold'),padx=40,pady=20)
button6 = Button(totalCostFrame,text="6",font=('Roboto',20,'bold'),padx=40,pady=20)
button7 = Button(totalCostFrame,text="7",font=('Roboto',20,'bold'),padx=40,pady=20)
button8 = Button(totalCostFrame,text="8",font=('Roboto',20,'bold'),padx=40,pady=20)
button9 = Button(totalCostFrame,text="9",font=('Roboto',20,'bold'),padx=40,pady=20)
button0 = Button(totalCostFrame,text="0",font=('Roboto',20,'bold'),padx=40,pady=20)
button_add = Button(totalCostFrame,text="+",font=('Roboto',20,'bold'),padx=39,pady=20)
button_equal = Button(totalCostFrame,text="=",font=('Roboto',20,'bold'),padx=91,pady=20)
button_clear = Button(totalCostFrame,text="Clear",font=('Roboto',20,'bold'),padx=79,pady=20)




# displaying widgets on the screen
# FRAME ONE
itemsFrame.grid_propagate(0)
itemsFrame.grid(row=0,column=0,ipadx=20,ipady=20,padx=(30,10),pady=50)
listOfProducts.grid(row=0,column=3,sticky=N,pady=120,padx=(20,0),ipadx=10)
addSelectedBtn.grid(row=1,column=3,padx=(20,0),ipadx=15,ipady=10)
topLabel.grid(row=0,column=0,padx=20,columnspan=3)


# FRAME THREE
totalCostFrame.grid_propagate(1)
totalCostFrame.grid(row=0,column=2,ipadx=10,ipady=10,padx=(50,30),pady=(50,30),sticky=N)
totalCostLabel.grid(row=0,column=0,columnspan=2,pady=(10,40))



button1.grid(row=3,column=0,padx=10,pady=10)
button2.grid(row=3,column=1,padx=10,pady=10)
button3.grid(row=3,column=2,padx=10,pady=10)

button4.grid(row=2,column=0,padx=10,pady=10)
button5.grid(row=2,column=1,padx=10,pady=10)
button6.grid(row=2,column=2,padx=10,pady=10)

button7.grid(row=1,column=0,padx=10,pady=10)
button8.grid(row=1,column=1,padx=10,pady=10)
button9.grid(row=1,column=2,padx=10,pady=10)

button0.grid(row=4,column=0,padx=10,pady=10)
button_clear.grid(row=4,column=1,columnspan=2,padx=10,pady=10)
button_add.grid(row=5,column=0,padx=10,pady=10)
button_equal.grid(row=5,column=1,columnspan=2,padx=10,pady=10)


POSScreen.mainloop()