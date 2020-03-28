from custom_modules import mono_caesar as mc 
from custom_modules import poly_caesar as pc 
from custom_modules import vigenere as vig 

from tkinter import filedialog
from tkinter import *

def create_gui():
    encoded = mc.mono_Caesar_Encode('Hallo Welt', 2)
    print(encoded)

    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Caeser-Verschlüsselung nach Monoalphabetischer Substitution", command=load_Mono_Caeser)
    filemenu.add_command(label="Caeser-Verschlüsselung nach Polyalphabetischer Substitution", command=load_Poly_Caeser)
    filemenu.add_command(label="Vigenére-Verschlüsselung ", command=load_vigenere)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)

    root.mainloop()

def get_state():
    return root.state

def create_Mono_Caesar():
    mono_Caesar_Entry_1.grid(row=1, column=1)

def destroy_Mono_Caesar():
    mono_Caesar_Entry_1.grid_remove()


def load_Mono_Caeser():
    create_Mono_Caesar()
    root.state = 0

    print(root.state)
    print("mono_caesar")

def load_Poly_Caeser():
    destroy_Mono_Caesar()
    root.state = 1

    print(root.state)
    print("poly_caesar")

def load_vigenere():
    print("vigenere")

def OpenFile():
    root.filename =  filedialog.askopenfilename(initialdir = "/",
                                            title = "Select file",
                                            filetypes = (("txt files","*.txt")
                                                        ,("all files","*.*")))

    print(root.filename)

def About():
    print("This is a simple example of a menu")


if __name__ == '__main__':
    root = Tk()

    root.state = 0

    mono_Caesar_Entry_1 = Entry(root)

    create_gui()