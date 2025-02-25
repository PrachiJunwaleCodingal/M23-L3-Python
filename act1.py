#event handler

from tkinter import *
window = Tk()
window.title("Act1- Event Handler")
window.geometry("200x200")

def key_event(event):
    print("Key pressed:")
    print(event.char)

window.bind("<Key>", key_event)  #any key

def btn_click(event):
    print("\n button clicked!")
    
button = Button(text="Click here!")
button.pack()
button.bind("<Button-1>", btn_click)

window.mainloop()