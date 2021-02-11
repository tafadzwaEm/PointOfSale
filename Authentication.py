from tkinter import *
from tkinter import messagebox
import sqlite3



authScreen = Tk()
authScreen.title("POS START")
authScreen.geometry("500x300")

spacingFrame = Frame(authScreen)
frame = Frame(bg="green",padx=10)
welcomeLabel = Label(frame,text="STOP & SHOP",font=("roboto",10,"bold"),pady=10)

# CREATING AND/OR CONNECTING TO LOGIN DATABASE
conn = sqlite3.connect("db/userAuthentication.db")
c = conn.cursor()

# c.execute("""CREATE TABLE Users(
#         firstName text,
#         lastName text,
#         password varchar
# )""")
# c.execute("INSERT INTO users (firstName,lastName,password) VALUES('Emmanuel','Mukombero','Manue4578')")
# creating all necessary functions of system modules
def back():
    oplogin.destroy()

def operatorlogin():
    conn = sqlite3.connect("db/userAuthentication.db")
    c = conn.cursor()

    c.execute("SELECT * FROM Users")
    records = c.fetchall()

    for record in records:
        if usernameEntry.get() == record[0] and passwordEntry.get() == record[2]:
            response = messagebox.showinfo("LOGIN SUCCESS","You have successfully logged in.")
            if response == "ok":
                oplogin.destroy()
                import pointOfSale
                
        elif len(usernameEntry.get()) == 0 or len(passwordEntry.get()) == 0:
            messagebox.showerror("FILL IN","Fill in all fields")
        else:
            messagebox.showerror("LOGIN FAIL","Incorrect username or password")




        
        
    conn.commit()
    conn.close()
# CREATING OPERATOR LOGIN SCREEN
def operatorLogin():
    global oplogin
    oplogin = Tk()
    oplogin.title("OPERATOR LOGIN")
    oplogin.geometry("500x300")

    # create labels for logins
    usernameLabel = Label(oplogin,text="Username",font=("roboto",10))
    passwordLabel = Label(oplogin,text="Password",font=("roboto",10))
    # create entry widgets for login
    global usernameEntry
    global passwordEntry
    usernameEntry = Entry(oplogin,width=35)
    passwordEntry = Entry(oplogin,width=35,show="-")
    # create login and back button
    loginBtn = Button(oplogin,text="Login",font=("roboto",10),command=operatorlogin)
    backBtn = Button(oplogin,text="Back",font=("roboto",10),command=back)
    # displaying widgets on screen
    usernameLabel.grid(row=0,column=0,pady=(100,20),padx=(100,10))
    passwordLabel.grid(row=1,column=0,padx=(100,10))
    usernameEntry.grid(row=0,column=1,pady=(100,20))
    passwordEntry.grid(row=1,column=1)
    loginBtn.grid(row=2,column=0,columnspan=2,pady=20,padx=(150,0),ipadx=50)
    backBtn.grid(row=3,column=0,columnspan=2,padx=(150,0),ipadx=50)

def adminlogin():
    conn = sqlite3.connect("db/userAuthentication.db")
    c = conn.cursor()

    c.execute("SELECT * FROM Users")
    records = c.fetchall()

    for record in records:
        if usernameEntry.get() == record[0] and passwordEntry.get() == record[2]:
            response = messagebox.showinfo("LOGIN SUCCESS","You have successfully logged in.")
            if response == "ok":
                adlogin.destroy()
                import adminView
                
        elif len(usernameEntry.get()) == 0 or len(passwordEntry.get()) == 0:
            messagebox.showerror("FILL IN","Fill in all fields")
        else:
            messagebox.showerror("LOGIN FAIL","Incorrect username or password")




        
        
    conn.commit()
    conn.close()

   

    # if str(usernameEntry.get()) == "Emmanuel" and str(passwordEntry.get()) == "Mukombero":
    #     response = messagebox.showinfo("LOGIN SUCCESS","You have successfully logged in.")
    #     if response == "ok":
    #         adlogin.destroy()
    # #         import adminView
            
    # else:
    #     messagebox.showerror("LOGIN FAIL","Incorrect username or password, try again.")

        
    

#  CREATING ADMIN LOGIN SCREEN
def adminLogin():
    
    global adlogin
    adlogin = Tk()
    adlogin.title("ADMIN LOGIN")
    adlogin.geometry("500x300")
    def adback():
        adlogin.destroy()
  # create labels for logins
    usernameLabel = Label(adlogin,text="Username",font=("roboto",10))
    passwordLabel = Label(adlogin,text="Password",font=("roboto",10))
    global usernameEntry
    global passwordEntry
    # create entry widgets for login
    usernameEntry = Entry(adlogin,width=35)
    passwordEntry = Entry(adlogin,width=35,show="-")
    # create login and back button
    loginBtn = Button(adlogin,text="Login",font=("roboto",10),command=adminlogin)
    backBtn = Button(adlogin,text="Back",font=("roboto",10),command=adback)
    # displaying widgets on screen
    usernameLabel.grid(row=0,column=0,pady=(100,20),padx=(100,10))
    passwordLabel.grid(row=1,column=0,padx=(100,10))
    usernameEntry.grid(row=0,column=1,pady=(100,20))
    passwordEntry.grid(row=1,column=1)
    loginBtn.grid(row=2,column=0,columnspan=2,pady=20,padx=(150,0),ipadx=50)
    backBtn.grid(row=3,column=0,columnspan=2,padx=(150,0),ipadx=50)
    
    

# Creating Login Options Buttons
AdminloginOptionBtn = Button(authScreen,text="LOGIN \n AS ADMIN",font=("roboto",10,"bold"),command=adminLogin)
OperatorloginOptionBtn = Button(authScreen,text="LOGIN \n AS OPERATOR",font=("roboto",10,"bold"),command=operatorLogin)

# Displaying Widgets to screen
spacingFrame.grid(row=0,column=0,columnspan=2,pady=10)
frame.grid(row=1,column=0,columnspan=2,ipadx=130)
welcomeLabel.grid(row=1,column=0,columnspan=2,ipadx=100)

# Displaying Buttons on the screen
AdminloginOptionBtn.grid(row=2,column=0,pady=(50,10),ipady=5,ipadx=35,padx=(0,70),columnspan=2)
OperatorloginOptionBtn.grid(row=3,column=0,pady=10,ipady=5,padx=(0,70),ipadx=20,columnspan=2)


conn.commit()
conn.close()
authScreen.mainloop()