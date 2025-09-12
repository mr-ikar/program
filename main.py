from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import gc
root = Tk()
root.title("Текстовый редактор 'Анаконда'")
root.geometry("512x512")
mainframe = ttk.Frame(root, padding="3 3 12 12")

def newFile(event):
    t.delete(1.0, 'end')
    root.title("Новый файл - Текстовый редактор 'Анаконда'")
    gc.collect()
def openFile(event):
    file_path = filedialog.askopenfilename(
        title="Открыть текстовый файл",
        filetypes=[("Все файлы", "*.*")]
    )
    if not file_path:  # Отмена открытия
        return

    # Прочитать файл
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Вставить текст файла в текстовое окно
    t.delete(1.0, 'end')  # Очистить текстовое окно
    t.insert('end', content)
    root.title(file_path+" - Текстовый редактор 'Анаконда'")
    gc.collect() # Очищение мусора из оперативной памяти (ОЗУ)
def saveFile(event):
    file_path = filedialog.asksaveasfilename(
        title="Сохранить файл",
        defaultextension=".txt",
        filetypes=[("Текстовый файл", "*.txt"), ("Все файлы", "*.*")]
    )
    if not file_path:
        return

    # Get content from the Text widget
    content = t.get(1.0, 'end')

    # Save to file with UTF-8 encoding
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

t = Text(root, width = 40, height = 5, wrap = "none")
ys = ttk.Scrollbar(root, orient = 'vertical', command = t.yview)
xs = ttk.Scrollbar(root, orient = 'horizontal', command = t.xview)
t['yscrollcommand'] = ys.set
t['xscrollcommand'] = xs.set
t.insert('end', "Добро пожаловать в упрощенный текстовый редактор 'Анаконда'\nНажмите Ctrl+O для открытия файла\nНажмите Ctrl+N для нового файла\nНажмите Ctrl+S для сохранения файла")
t.grid(column = 0, row = 0, sticky = 'nwes')
xs.grid(column = 0, row = 1, sticky = 'we')
ys.grid(column = 1, row = 0, sticky = 'ns')
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)

root.bind("<Control-o>", openFile)
root.bind("<Control-n>", newFile)
root.bind("<Control-s>", saveFile)
root.mainloop()

