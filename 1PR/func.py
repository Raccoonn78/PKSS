import main as EntryA
import main as EntryB
import main as EntryC
from tkinter import *


def proizv():
    a = EntryA.get() # берем текст из первого поля
    a = int(a) # преобразуем в число целого типа

    b = EntryB.get() 
    b = int(b)

    result = str(a * b) # результат переведем в строку для дальнейшего вывода
    return EntryC.delete(0, END),  EntryC.insert(0, result) # очищаем текстовое поле полностью
    # вставляем результат в начало 
