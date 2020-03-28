from custom_modules import mono_caesar as mc 
from custom_modules import poly_caesar as pc 
from custom_modules import vigenere as vig 

from tkinter import filedialog
from tkinter import *

def create_gui():

    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(
        label="Caeser-Verschlüsselung nach Monoalphabetischer Substitution",
        command=load_Mono_Caeser)
    filemenu.add_command(
        label="Caeser-Verschlüsselung nach Polyalphabetischer Substitution",
        command=load_Poly_Caeser)
    filemenu.add_command(label="Vigenére-Verschlüsselung ", command=load_vigenere)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)

    root.mainloop()

def create_Mono_Caesar():
    mono_Caesar_Label_head.grid(row=0, column=1)

    mono_Caesar_Label_1.grid(row=1, column=0)
    mono_Caesar_Label_2.grid(row=1, column=1)
    mono_Caesar_Label_3.grid(row=1, column=2)
    mono_Caesar_Label_4.grid(row=2, column=2)

    mono_Caesar_Entry_1.grid(row=2, column=0)
    mono_Caesar_Entry_2.grid(row=2, column=1)

    mono_Caesar_Button_1.grid(row=3, column=0)
    mono_Caesar_Button_2.grid(row=3, column=1)
    mono_Caesar_Button_3.grid(row=3, column=2)

def destroy_Mono_Caesar():
    mono_Caesar_Label_head.grid_remove()

    mono_Caesar_Label_1.grid_remove()
    mono_Caesar_Label_2.grid_remove()
    mono_Caesar_Label_3.grid_remove()
    mono_Caesar_Label_4.grid_remove()

    mono_Caesar_Entry_1.grid_remove()
    mono_Caesar_Entry_2.grid_remove()

    mono_Caesar_Button_1.grid_remove()
    mono_Caesar_Button_2.grid_remove()
    mono_Caesar_Button_3.grid_remove()

def create_Poly_Caesar():
    pass

def destroy_Poly_Caesar():
    pass

def create_Vigenere():
    pass

def destroy_Vigenere():
    pass


def load_Mono_Caeser():
    if root.state == 0:
        pass
    if root.state == 1:
        destroy_Poly_Caesar()
        create_Mono_Caesar()
    if root.state == 2:
        destroy_Vigenere()
        create_Mono_Caesar()

    root.state = 0

def load_Poly_Caeser():
    if root.state == 0:
        destroy_Mono_Caesar()
        create_Poly_Caesar()
    if root.state == 1:
        pass
    if root.state == 2:
        destroy_Vigenere()
        create_Poly_Caesar()

    root.state = 1

def load_vigenere():
    if root.state == 0:
        destroy_Mono_Caesar()
        create_Vigenere()
    if root.state == 1:
        destroy_Poly_Caesar()
        create_Vigenere()
    if root.state == 2:
        pass

    root.state = 2

def use_mono_Caesar_Encode():
    text = mono_Caesar_Entry_1.get()
    key = int(mono_Caesar_Entry_2.get())

    encoded_text = mc.mono_Caesar_Encode(text,key)

    mono_Caesar_Label_4.config(text=encoded_text)

def use_mono_Caesar_Decode():
    pass

def clear_Entry_1():
    mono_Caesar_Entry_1.delete(0,'end')

def clear_Entry_2():
    mono_Caesar_Entry_2.delete(0,'end')

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

    mono_Caesar_Label_head = Label(root, 
        text='Caeser-Verschlüsselung nach Monoalphabetischer Substitution')
    mono_Caesar_Label_1 = Label(root, text='lesbarer Text')
    mono_Caesar_Label_2 = Label(root, text='Schlüsselzahl')
    mono_Caesar_Label_3 = Label(root, text='verschlüsselter Text')
    mono_Caesar_Label_4 = Label(root, text='ijcnnq ygnv!')

    mono_Caesar_Entry_1 = Entry(root)
    mono_Caesar_Entry_2 = Entry(root)

    mono_Caesar_Button_1 = Button(root, text="Eingabefeld leeren",
                                        command=clear_Entry_1)
    mono_Caesar_Button_2 = Button(root, text="Eingabefeld leeren",
                                        command=clear_Entry_2)
    mono_Caesar_Button_3 = Button(root, text="anwenden", 
                                        command=use_mono_Caesar_Encode)


    #Mono Caeser is loaded first
    create_Mono_Caesar()

    create_gui()