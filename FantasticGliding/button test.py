from tkinter import *
from pygame import *

def thanks():
    print('Thanks for clicking me!!')
    
btn = Button(Tk(), text="click me!!" , bg = "black" , fg = "white" , pady = 30, padx = 50 , command=thanks)
btn.pack()
