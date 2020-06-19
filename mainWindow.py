from tkinter import *
from tkinter.ttk import Combobox

import os

import calculator

def main():
    window = Tk()
    window.title("Calculadora Grafos")
    window.geometry('870x500')

    arrayFiles = []
    path = "./graphs"
    for files in os.listdir(path):
        if files.endswith(".txt"):
            arrayFiles.append(files)

    combobox = Combobox(window)
    combobox['values'] = arrayFiles
    combobox.current(0)
    combobox.place(x = 380, y = 60)

    label = Label(window, text="Selecione o arquivo da matriz...", font=("Arial", 12))
    label.place(x = 370, y = 20)

    def show():
        label['text'] = calculator.resultValues(combobox.get())

    btn = Button(window, text = "Calcular informações...", command = show)
    btn.place(x = 380, y = 100)

    label = Label(window)
    label.place(x = 50, y = 170)

    window.mainloop()

if __name__ == "__main__":
    main()