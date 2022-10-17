from cmath import pi
import tkinter as tk
from tkinter import *
import math as M


class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.label =Label( self,text='Площадь круга')
        # вторая метка в строке 1
        self.label2 = Label( self,text='Площадь квадрата')

        # создаем виджеты текстовых полей
        self.EntryA = Entry( self, width=10, font='Arial 16')
        self.EntryB = Entry( self,  width=10, font='Arial 16')
        self.EntryC = Entry( self , width=20, font='Arial 16')# для вывода ответа

        
       


        self.button = tk.Button(self, text='Расчитать', command=self.on_click)
        # пакуем все наши блоки через pack() , так же есть еще два метода упаковки блоков
        self.label.pack()
        self.EntryA.pack(fill=BOTH)
        self.label2.pack()
        self.EntryB.pack(fill=BOTH)
        self.button.pack()
        self.EntryC.pack(fill=BOTH)
        
        
        self.pack()

    def on_click(self):
        a = self.EntryA.get() # берем текст из первого поля
        a = int(a) # преобразуем в число целого типа

        Pcircl= M.sqrt(a/pi)

        b = self.EntryB.get() 
        b = int(b)

        Psquare= M.sqrt(b)

        d= 2* M.sqrt(Pcircl/pi)
        e= M.sqrt(Psquare)
        diag=M.sqrt(2*e*e)

        if Pcircl<=Psquare:
            result="Круг поместиться в квадрат"
        

        if diag<=d:
            result="квадрат поместиться в круг"  
        else:
            result='Нет'

            
         # результат переведем в строку для дальнейшего вывода
        self.EntryC.delete(0, END) # очищаем текстовое поле полностью
        self.EntryC.insert(0, result) # вставляем результат в начало 