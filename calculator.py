from tkinter import *
from tkinter import ttk

class Controlator(ttk.Frame):
    def __init__(self, parent): #kwargs = clave/valor
        ttk.Frame.__init__(self, parent, width=272, height=300)


class Display(ttk.Frame):
    def __init__(self,parent):
        ttk.Frame.__init__(self, parent, widht=272, height=50)

        lbl = ttk.Label(self, text="0", anchor=E)
        lbl.pack(side=TOP, fill=BOTH, expand=True)



class Selector(ttk.Radiobutton):
    pass

class CalcButton(ttk.Button):
    pass

