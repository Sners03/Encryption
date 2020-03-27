from custom_modules import mono_caesar as mc 
from custom_modules import poly_caesar as pc 
from custom_modules import vigenere as vig 

from tkinter import filedialog
from tkinter import *


def NewFile():
    print("New File!")
def OpenFile():
    root.filename =  filedialog.askopenfilename(initialdir = "/",
                                            title = "Select file",
                                            filetypes = (("txt files","*.txt")
                                                        ,("all files","*.*")))

    print(root.filename)
def About():
    print("This is a simple example of a menu")

if __name__ == '__main__':
    encoded = mc.mono_Caesar_Encode('Hallo Welt', 2)
    print(encoded)

    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Caeser-Verschlüsselung nach Monoalphabetischer Substitution", command=NewFile)
    filemenu.add_command(label="Caeser-Verschlüsselung nach Polyalphabetischer Substitution", command=NewFile)
    filemenu.add_command(label="Vigenére-Verschlüsselung ", command=OpenFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)

    mainloop()