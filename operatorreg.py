from tkinter import *
from tkinter import messagebox
import sqlite3

global addOperatorScreen
addOperatorScreen = Tk()
addOperatorScreen.geometry("400x500")
addOperatorScreen.title("ENTER OPERATOR DETAILS")


def addOperator():
    conn = sqlite3.connect("db/userAuthentication.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO Users VALUES (:firstName,:lastName,:password)",{
            'firstName': operatorNameEntry.get(),
            'lastName': operatorLastNameEntry.get(),
            'password': operatorPasswordEntry.get()
        })
        errorLabel = Label(addOperatorScreen, text="Addition Successful",fg="green")
        errorLabel.grid(row=6,column=0,columnspan=2)
    except:
        errorLabel = Label(addOperatorScreen, text="Could not add operator",fg="red")
        errorLabel.grid(row=6,column=0,columnspan=2)
    conn.commit()
    conn.close()
    
    operatorNameEntry.delete(0,END)
    operatorLastNameEntry.delete(0,END)
    operatorPasswordEntry.delete(0,END)

# ADD OPERATOR SCREEN LABELS
operatorNameLabel = Label(addOperatorScreen,text="First Name:",font=("Roboto",10))
operatorLastNameLabel = Label(addOperatorScreen,text="Last Name:",font=("Roboto",10))
operatorPasswordLabel = Label(addOperatorScreen,text="Password:",font=("Roboto",10))

# ADD OPERATOR SCREEN ENTRY BOXES
global operatorNameEntry
global operatorLastNameEntry
global operatorPasswordEntry

operatorNameEntry = Entry(addOperatorScreen,width=35)
operatorLastNameEntry = Entry(addOperatorScreen,width=35)
operatorPasswordEntry = Entry(addOperatorScreen,width=35,show="-")

# ADD OPERATOR SCREEN BUTTONS
addOperatorBtn = Button(addOperatorScreen,text="Add Operator",font=("Roboto",10),command=addOperator)
# ADD OPERATOR SCREEN DISPLAY
operatorNameLabel.grid(row=0,column=0,padx=(30,0),pady=(50,10)) 
operatorLastNameLabel.grid(row=1,column=0,padx=(30,0),pady=(10,10)) 
operatorPasswordLabel.grid(row=2,column=0,padx=(30,0),pady=(10,10))


operatorNameEntry.grid(row=0,column=1,padx=(30,0),pady=(50,10),ipady=5)
operatorLastNameEntry.grid(row=1,column=1,padx=(30,0),pady=(10,10),ipady=5)
operatorPasswordEntry.grid(row=2,column=1,padx=(30,0),pady=(10,10),ipady=5)


addOperatorBtn.grid(row=5,column=0,columnspan=2,ipadx=50,padx=(20,0),ipady=7)



