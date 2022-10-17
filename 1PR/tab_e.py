from cmath import pi
from pickletools import read_uint1
import tkinter as tk
from tkinter import *
import math as M
from unittest import result
import numpy as np
from numpy import double
class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.label =Label( self,text='Введиет  x')
        # вторая метка в строке 1
        self.label2 = Label( self,text='Введиет y')
        
        

        # создаем виджеты текстовых полей
        self.EntryA = Entry( self, width=10, font='Arial 16')
        self.EntryB = Entry( self,  width=10, font='Arial 16')
        

        self.EntryE = Entry( self , width=20, font='Arial 16')

        
       


        self.button = tk.Button(self, text='Расчитать', command=self.on_click)
        
        self.label.pack()
        self.EntryA.pack(fill=BOTH)

        self.label2.pack()
        self.EntryB.pack(fill=BOTH)

        

        self.button.pack()
        self.EntryE.pack(fill=BOTH)
        
        
        self.pack()

    def on_click(self):
        a = self.EntryA.get() # берем текст из первого поля
        a = float(a) # преобразуем в число целого типа

        b = self.EntryB.get() 
        b = float(b)
        
        arcsin= np.arcsin(a+b)
        result='arcsin(x+y)='+str(arcsin)
        

         # результат переведем в строку для дальнейшего вывода
        self.EntryE.delete(0, END) # очищаем текстовое поле полностью
        self.EntryE.insert(0, result) # вставляем результат в начало 