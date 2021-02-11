from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("db/stock.db")
c = conn.cursor()

global reorderView
reorderView = Tk()
reorderView.title("Products to reorder")

# FUNCTIONS IN THE STOCKREORDER MODULE
# Function for closing the reorder window
def destroyReorder():
    reorderView.destroy()

c.execute("SELECT * FROM products Where totalproducts <= 10")
records = c.fetchall()
prd_reorder = " "
for record in records:
    prd_reorder += str(record[0]) + " total left: " + str(record[4]) + "\n"

if len(prd_reorder) < 1:
    reorderLabel = Label(reorderView,text = "No Items to Display...",font=("Roboto",10,"bold")).pack(ipady=50,ipadx=50)
else:
    reorderLabel = Label(reorderView,text = prd_reorder,font=("Roboto",10),relief=RIDGE).pack(ipady=50,ipadx=50)
closeBtn = Button(reorderView,text="Close",font=("Roboto",10,"bold"),command=destroyReorder).pack(ipadx=30,ipady=10)

conn.commit()
conn.close()