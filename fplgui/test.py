from tkinter import *

def create_cbuts():
    for i in cbuts_text:
        cbuts[i]=Checkbutton(root, text = i)
        cbuts[i].pack()

def select_all():
    global cbuts
    global cbuts_text
    for j in cbuts_text:
        cbuts[j].select()

def deselect_all():
    global cbuts
    global cbuts_text
    for j in cbuts_text:
        cbuts[j].deselect()

root = Tk()
cbuts_text = ['a','b','c','d']
cbuts = {}
create_cbuts()
Button(root, text = 'all', command = select_all).pack()
Button(root, text = 'None', command = deselect_all).pack()
print(cbuts)

root.mainloop()

