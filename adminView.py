from tkinter import *
from tkinter import messagebox
import sqlite3


adminScreen = Tk()
adminScreen.title("LOGGED IN AS ADMIN")
# adminScreen.attributes("-fullscreen",True)

stock_conn = sqlite3.connect("db/stock.db")
c = stock_conn.cursor()

# c.execute(""" CREATE TABLE products (
#     productName text,
#     productDescription text,
#     price integer,
#     productCode text,
#     totalproducts integer
# )

# """)


# ALL NECESSARY FUNCTIONS
def exitApp():
    response = messagebox.askyesno("Exit Application","Are you sure you want to exit?")
    if response == 1:
        adminScreen.destroy()
    elif response == 2:
        return
    else:
        return
# add product into database
def appendProduct():
    stock_conn = sqlite3.connect("db/stock.db")
    c = stock_conn.cursor()
    if len(productCodeEntry.get()) == 0 or len(productDescriptionEntry.get()) == 0 or len(productPriceEntry.get()) == 0 or len(productCodeEntry.get()) == 0 or len(totalInStockEntry.get()) == 0:
        successfulLabel = Label(addProductScreen,text="Fill in all fields",font=("Roboto",12,"bold"),fg="red")
        successfulLabel.grid(row=6,column=0,columnspan=2,pady=20)
    else:
       
        try:
            c.execute("INSERT INTO products VALUES (:productName,:productDescription,:price,:productCode,:totalproducts)",{
                'productName': productNameEntry.get(),
                'productDescription':productDescriptionEntry.get(),
                'price':productPriceEntry.get(),
                'productCode':productCodeEntry.get(),
                'totalproducts':totalInStockEntry.get()
            })

            stock_conn.commit()
            stock_conn.close()

            productNameEntry.delete(0,END)
            productDescriptionEntry.delete(0,END)
            productPriceEntry.delete(0,END)
            productCodeEntry.delete(0,END)
            totalInStockEntry.delete(0,END)

            successfulLabel = Label(addProductScreen,text="Product Addition Scuccessful",font=("Roboto",12,"bold"),fg="green")
            successfulLabel.grid(row=6,column=0,columnspan=2,pady=20)
        except:
            successfulLabel = Label(addProductScreen,text="Could not establish connection\nwith database. Please\ntry again",font=("Roboto",12,"bold"),fg="red")
            successfulLabel.grid(row=6,column=0,columnspan=2,pady=20)

def addProduct():
    stock_conn = sqlite3.connect("db/stock.db")
    c = stock_conn.cursor()
    global addProductScreen
    addProductScreen = Tk()
    addProductScreen.geometry("400x500")
    addProductScreen.title("ENTER PRODUCT DETAILS")

    # ADD PRODUCT SCREEN LABELS
    productNameLabel = Label(addProductScreen,text="Product Name",font=("Roboto",10))
    productDescriptionLabel = Label(addProductScreen,text="Prd Description",font=("Roboto",10))
    productPriceLabel = Label(addProductScreen,text="Product Price",font=("Roboto",10))
    productCodeLabel = Label(addProductScreen,text="Product Code",font=("Roboto",10))
    totalInStockLabel = Label(addProductScreen,text="Total In Stock",font=("Roboto",10))
    # ADD PRODUCT SCREEN ENTRY BOXES
    global productNameEntry
    global productDescriptionEntry
    global productPriceEntry
    global productCodeEntry
    global totalInStockEntry
    productNameEntry = Entry(addProductScreen,width=35)
    productDescriptionEntry = Entry(addProductScreen,width=35)
    productPriceEntry = Entry(addProductScreen,width=35)
    productCodeEntry = Entry(addProductScreen,width=35)
    totalInStockEntry = Entry(addProductScreen,width=35)
    # ADD PRODUCT SCREEN BUTTONS
    addProductBtn = Button(addProductScreen,text="Add Product",font=("Roboto",10),command=appendProduct)
    # ADD PRODUCT SCREEN DISPLAY
    productNameLabel.grid(row=0,column=0,padx=(30,0),pady=(50,10)) 
    productDescriptionLabel.grid(row=1,column=0,padx=(30,0),pady=(10,10)) 
    productPriceLabel.grid(row=2,column=0,padx=(30,0),pady=(10,10))
    productCodeLabel.grid(row=3,column=0,padx=(30,0),pady=(10,10)) 
    totalInStockLabel.grid(row=4,column=0,padx=(30,0),pady=(10,10)) 

    productNameEntry.grid(row=0,column=1,padx=(30,0),pady=(50,10),ipady=5)
    productDescriptionEntry.grid(row=1,column=1,padx=(30,0),pady=(10,10),ipady=5)
    productPriceEntry.grid(row=2,column=1,padx=(30,0),pady=(10,10),ipady=5)
    productCodeEntry.grid(row=3,column=1,padx=(30,0),pady=(10,10),ipady=5)
    totalInStockEntry.grid(row=4,column=1,padx=(30,0),pady=(10,40),ipady=5)

    addProductBtn.grid(row=5,column=0,columnspan=2,ipadx=50,padx=(20,0),ipady=7)



    stock_conn.commit()
    stock_conn.close()

def viewStock():
    global vStock
    vStock = Tk()
    stock_conn = sqlite3.connect("db/stock.db")
    c = stock_conn.cursor()
    c.execute("SELECT *,oid FROM products")
    records = c.fetchall()
    stockRecords = ""
    for record in records:
        stockRecords += "PRODUCT NAME: "+str(record[0])+"....PRODUCT ID: "+str(record[5])+"....DESCRIPTION: "+str(record[1])+"....PRODUCT CODE: "+str(record[3])+"....PRICE: $"+str(record[2])+"....TOTAL IN STOCK: "+str(record[4])+"\n\n ---------- \n\n\n"
    stock_conn.commit()
    stock_conn.close()
    displayStock = Label(vStock,text=stockRecords,font=("Roboto",10),relief=RIDGE)
    displayStock.grid(row=0,column=0,ipadx=20,padx=30,pady=50,ipady=15)

def deleteProduct():
    stock_conn = sqlite3.connect("db/stock.db")
    c = stock_conn.cursor()
    c.execute("SELECT * FROM products WHERE oid="+removeProductEntry.get())
    records = c.fetchall()
    try:
        response = messagebox.showwarning("WARNING","This will delete "+str(records[0])+" ?")
    except:
        deleteSuccessLabel = Label(removeProductWindow,text="Could not remove product\ncheck if product exists",font=("Roboto",10,"bold"),fg="red")
        deleteSuccessLabel.grid(row=2,column=0,columnspan=2,pady=(0,20))
        removeProductEntry.delete(0,END)
    if response == "ok":
        try:
            c.execute("DELETE FROM products WHERE oid="+removeProductEntry.get())
            deleteSuccessLabel = Label(removeProductWindow,text="Product Removed Successfully",font=("Roboto",10,"bold"),fg="green")
            deleteSuccessLabel.grid(row=2,column=0,columnspan=2,pady=(0,20))
            removeProductEntry.delete(0,END)
        except:
            deleteSuccessLabel = Label(removeProductWindow,text="Could not remove product\ncheck if product exists",font=("Roboto",10,"bold"),fg="red")
            deleteSuccessLabel.grid(row=2,column=0,columnspan=2,pady=(0,20))
            removeProductEntry.delete(0,END)
            
    stock_conn.commit()
    stock_conn.close()

def removeProduct():
    global productId
    global removeProductWindow
    global removeProductEntry
    removeProductWindow = Tk()
    removeProductWindow.title("Remove Product")
    removeProductLabel = Label(removeProductWindow,text="Enter Product Id: ",font=("Roboto",10))
    removeProductEntry = Entry(removeProductWindow,width=10)
    removeProductWindowBtn = Button(removeProductWindow,text="Remove Product",command=deleteProduct)

    removeProductLabel.grid(row=0,column=0,padx=(50,10),pady=(50,20))
    removeProductEntry.grid(row=0,column=1,padx=(10,50),pady=(50,20))
    removeProductWindowBtn.grid(row=1,column=0,padx=(10,0),pady=(10,50),columnspan=2,ipadx=30)

def reorder():
    import stockreorder

def addOperatorr():
    import operatorreg
# ADMIN VIEW FRAMES

actionsFrame = Frame(adminScreen,relief=SOLID,width=300,height=700,bg="floral white")  
# ALL ADMIN VIEW LABELS
actionsLabel = Label(actionsFrame,text="ADMIN ACTIONS \n AVAILABLE",font=("Roboto",10,"bold"))

# ALL ADMIN VIEW ENTRY WIDGETS

#  ALL ADMIN VIEW BUTTONS
# buttons inside frame
addProductsBtn = Button(actionsFrame,text="Add Product",font=("Roboto",10),command=addProduct)
removeProductsBtn = Button(actionsFrame,text="Remove Product",font=("Roboto",10),command=removeProduct)
reorderLevelBtn = Button(actionsFrame,text="Stock Reorder",font=("Roboto",10),command=reorder)
viewStockBtn = Button(actionsFrame,text="View Stock",font=("Roboto",10),command=viewStock)
pointOfSaleBtn = Button(actionsFrame,text="Point Of Sale",font=("Roboto",10))
addOperatorBtn = Button(actionsFrame,text="Add Operator",font=("Roboto",10),command=addOperatorr)
# exit button
exitBtn = Button(adminScreen,text="Exit Application",command=exitApp)

# DISPLAY WIDGETS ON SCREEN
actionsFrame.grid(row=0,column=0,padx=(50,50),pady=(50,0))
# frame widgets
actionsLabel.grid(row=0,column=0,padx=5,pady=20,ipadx=150,ipady=10)

addProductsBtn.grid(row=1,column=0,padx=5,pady=10,ipadx=100,ipady=10)
removeProductsBtn.grid(row=2,column=0,padx=5,pady=10,ipadx=90,ipady=10) 
reorderLevelBtn.grid(row=3,column=0,padx=5,pady=10,ipadx=97,ipady=10)
viewStockBtn.grid(row=4,column=0,padx=5,pady=10,ipadx=105,ipady=10)
pointOfSaleBtn.grid(row=5,column=0,padx=5,pady=10,ipadx=100,ipady=10)
addOperatorBtn.grid(row=6,column=0,padx=5,pady=10,ipadx=100,ipady=10)


exitBtn.grid(row=1,column=0,ipadx=40,pady=20)


stock_conn.commit()
stock_conn.close()

adminScreen.mainloop()