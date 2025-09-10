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

t = Text(root, width = 40, height = 5, wrap = "none")
ys = ttk.Scrollbar(root, orient = 'vertical', command = t.yview)
xs = ttk.Scrollbar(root, orient = 'horizontal', command = t.xview)
t['yscrollcommand'] = ys.set
t['xscrollcommand'] = xs.set
t.insert('end', "Lorem ipsum...\n...\n...")
t.grid(column = 0, row = 0, sticky = 'nwes')
xs.grid(column = 0, row = 1, sticky = 'we')
ys.grid(column = 1, row = 0, sticky = 'ns')
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)

root.bind(<Ctrl><O>, newFile)

text = StringVar()
#text_entry = ttk.Entry(mainframe, width=32, textvariable=text)
#text_entry.grid(column=32, row=1, sticky=(W, E))
#text_entry = ttk.

root.mainloop()

# начальный экран
# на потом