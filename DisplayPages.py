import tkinter
from tkinter import ttk
from tkinter.ttk import Entry


class Display(tkinter.Tk):
    def __init__(self):
        super().__init__()

    def  makeLabel(self, labelText, x ,y):
       label= ttk.Label(self, text =" testing tkinter")
       ttk.Label.grid(column=x, row=y)
       return label




