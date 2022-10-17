# import imp
# from tkinter import *


# def proizv():
#     a = EntryA.get() # берем текст из первого поля
#     a = int(a) # преобразуем в число целого типа

#     b = EntryB.get() 
#     b = int(b)

#     result = str(a * b) # результат переведем в строку для дальнейшего вывода
#     EntryC.delete(0, END) # очищаем текстовое поле полностью
#     EntryC.insert(0, result) # вставляем результат в начало 


from tkinter import Tk, ttk
import tkinter as tk

from tab_a import Example as TabA
from tab_b import Example as TabB
from tab_c import Example as TabC
from tab_d import Example as TabD
from tab_e import Example as TabE


class MainWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.parent.title('Шляпа')

        self.init_ui()

    def init_ui(self):
        self.parent['padx'] = 10
        self.parent['pady'] = 10

        self.notebook = ttk.Notebook(self, width=1000, height=700)

        a_tab = TabA(self.notebook)
        b_tab = TabB(self.notebook)
        c_tab = TabC(self.notebook)
        d_tab = TabD(self.notebook)
        e_tab = TabE(self.notebook)

        self.notebook.add(a_tab, text="Задание 16")
        self.notebook.add(b_tab, text="Задание 19")
        self.notebook.add(c_tab, text="Задание 22")
        self.notebook.add(d_tab, text="Задание 25")
        self.notebook.add(e_tab, text="Задание 28")

        self.notebook.pack()

        self.pack()


if __name__ == '__main__':
    root = Tk()
    root.title('version')
    ex = MainWindow(root)
    root.geometry("700x350")
    root.mainloop()






#16. Даны площадь квадрата S1 и круга S2. Определить поместится ли круг в квадрат и наоборот.























































# root = Tk()
# root.title('Произведение двух чисел')
# root.geometry('1200x400+200+100')

# # первая метка в строке 0, столбце 0 (0 по умолчанию)
# # парамет sticky  означает выравнивание. W, E,N,S — запад, восток, север, юг
# Label(root, text='Первое число').grid(row=0, sticky=W)

# # вторая метка в строке 1
# Label(root, text='Второе число').grid(row=1, sticky=W)

# # создаем виджеты текстовых полей
# EntryA = Entry(root, width=10, font='Arial 16')
# EntryB = Entry(root, width=10, font='Arial 16')
# EntryC = Entry(root, width=20, font='Arial 16')

# # размещаем первые два поля справа от меток, второй столбец (отсчет от нуля)
# EntryA.grid(row=0, column=1, sticky=E)
# EntryB.grid(row=1, column=1, sticky=E)

# # третье текстовое поле ввода занимает всю ширину строки 2
# # columnspan — объединение ячеек по столбцам; rowspan — по строкам
# EntryC.grid(row=2, columnspan=2)

# #####################
# Label(root, text='Первое число').grid(row=6, sticky=W)

# # вторая метка в строке 1
# Label(root, text='Второе число').grid(row=7, sticky=W)

# EntryA2 = Entry(root, width=10, font='Arial 16')
# EntryB2 = Entry(root, width=10, font='Arial 16')
# EntryC2 = Entry(root, width=20, font='Arial 16')


# EntryA2.grid(row=6, column=3, sticky=E)
# EntryB2.grid(row=7, column=3, sticky=E)
# EntryC2.grid(row=8, columnspan=2)
# ######################















# # размещаем кнопку в строке 3 во втором столбце 
# but = Button(root, text='Произведение', command=proizv)
# but.grid(row=3, column=1, sticky=E)

# root.mainloop()