import random
import tkinter
import threading
import time
Amount = 0
def upDown(AddorRemoveNumber = 0):
    global StringNumber
    global Amount
    Amount += AddorRemoveNumber
    StringNumber.set(Amount)
    KeepTrackOfAmount(0)

def Disco():
    global Amount
    if Amount >69:
        Amount = 69
    for i in range(10):
        window.config(bg="red")
        time.sleep(0.5)
        window.config(bg="green")
        time.sleep(0.5)
        window.config(bg="yellow")
        time.sleep(0.5)
        window.config(bg="blue")
        time.sleep(0.5)

def ChangeColorOnHover(event):
    window.config(bg="yellow")


def KeepTrackOfAmount(event):
    global Amount

    if Amount >= 1:
        window.config(bg="green")
    elif Amount <= -1:
        window.config(bg="red")
    elif Amount == 0:
        window.config(bg="grey")
    elif Amount == 69: 
        downButton.config(state=tkinter.DISABLED)
        UpButton.config(state=tkinter.DISABLED)
        Disco()
                
window = tkinter.Tk()
window.geometry("500x300")
UpButton = tkinter.Button(text="+1",padx=100,pady=20,command=lambda: upDown(1))
UpButton.pack()
StringNumber = tkinter.StringVar(window,value=Amount)
score = tkinter.Label(textvariable=StringNumber,pady=20,padx=100)
score.bind("<Enter>", ChangeColorOnHover)
score.bind("<Leave>", KeepTrackOfAmount)
score.pack()
downButton = tkinter.Button(text="-1",padx=100,pady=20,command=lambda: upDown(-1))
downButton.pack()
window.mainloop()