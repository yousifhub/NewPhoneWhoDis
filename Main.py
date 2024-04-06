import json
import random
from tkinter import *

def stanger():
    with open('FilePath//NewPhoneWhoDis//stranger.json', 'r') as file:
        data = json.load(file)
    list = data["stranger"]
    response = random.choice(list)
    return response

def you():
    with open('FilePath//NewPhoneWhoDis//you.json', 'r') as file:
        data = json.load(file)
    list = data["you"]
    response = random.choice(list)
    return response

def close_and_reopen():
    root.destroy()
    app()
   
def app():
    global root
    
    root = Tk()
    root.title("NewPhoneWhoDis!")
    icon_path = "FilePath\\NewPhoneWhoDis\\icon.png"
    icon = PhotoImage(file=icon_path)
    root.iconphoto(False, icon)
    
    lbl = Label(root, text="Stranger: ")
    lbl.grid()
    
    lbl = Label(root, text=stanger(), wraplength=300)
    lbl.grid()
    
    lbl = Label(root, text="\n", wraplength=300)
    lbl.grid()
    
    lbl = Label(root, text="You: ")
    lbl.grid()
    
    lbl = Label(root, text=you(), wraplength=300)
    lbl.grid()
    
    btn = Button(root, text="Reroll", fg="red", command=close_and_reopen)
    btn.grid(column=2, row=0)
    
    root.mainloop()
    
app()
