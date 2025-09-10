from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Текстовый редактор 'Анаконда'")
mainframe = ttk.Frame(root, padding="3 3 12 12")

def newFile():
    print("new file (not)")
def openFile():
    print("open file (not)")
def closeFile():
    print("close file (not)")

ttk.Button(mainframe, text="Новый текстовый файл", command=newFile)
ttk.Button(mainframe, text="Открыть текстовый файл", command=openFile)
ttk.Button(mainframe, text="Закрыть редактируемый файл", command=closeFile)

text = StringVar()
#text_entry = ttk.Entry(mainframe, width=32, textvariable=text)
#text_entry.grid(column=32, row=1, sticky=(W, E))
#text_entry = ttk.

root.mainloop()

# начальный экран
# на потом