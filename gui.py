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

    # Encoding part
    mono_Caesar_Label_subhead_1.grid(row=1, column=0)

    mono_Caesar_Label_1.grid(row=2, column=0)
    mono_Caesar_Label_2.grid(row=2, column=1)
    mono_Caesar_Label_3.grid(row=2, column=2)
    mono_Caesar_Label_4.grid(row=3, column=2)

    mono_Caesar_Entry_1.grid(row=3, column=0)
    mono_Caesar_Entry_2.grid(row=3, column=1)

    mono_Caesar_Button_1.grid(row=4, column=0)
    mono_Caesar_Button_2.grid(row=4, column=1)
    mono_Caesar_Button_3.grid(row=4, column=2)

    placeholder_Label.grid(row=5, column=0)

    # Decoding part
    mono_Caesar_Label_subhead_2.grid(row=6, column=0)

    mono_Caesar_Label_5.grid(row=7, column=0)
    mono_Caesar_Label_6.grid(row=7, column=1)
    mono_Caesar_Label_7.grid(row=7, column=2)
    mono_Caesar_Label_8.grid(row=8, column=2)

    mono_Caesar_Entry_3.grid(row=8, column=0)
    mono_Caesar_Entry_4.grid(row=8, column=1)

    mono_Caesar_Button_4.grid(row=9, column=0)
    mono_Caesar_Button_5.grid(row=9, column=1)
    mono_Caesar_Button_6.grid(row=9, column=2)

def destroy_Mono_Caesar():
    mono_Caesar_Label_head.grid_remove()

    # Encoding part
    mono_Caesar_Label_subhead_1.grid_remove()

    mono_Caesar_Label_1.grid_remove()
    mono_Caesar_Label_2.grid_remove()
    mono_Caesar_Label_3.grid_remove()
    mono_Caesar_Label_4.grid_remove()

    mono_Caesar_Entry_1.grid_remove()
    mono_Caesar_Entry_2.grid_remove()

    mono_Caesar_Button_1.grid_remove()
    mono_Caesar_Button_2.grid_remove()
    mono_Caesar_Button_3.grid_remove()

    placeholder_Label.grid_remove()

    # Decoding part
    mono_Caesar_Label_subhead_2.grid_remove()

    mono_Caesar_Label_5.grid_remove()
    mono_Caesar_Label_6.grid_remove()
    mono_Caesar_Label_7.grid_remove()
    mono_Caesar_Label_8.grid_remove()

    mono_Caesar_Entry_3.grid_remove()
    mono_Caesar_Entry_4.grid_remove()

    mono_Caesar_Button_4.grid_remove()
    mono_Caesar_Button_5.grid_remove()
    mono_Caesar_Button_6.grid_remove()

def create_Poly_Caesar():
    poly_Caesar_Label_head.grid(row=0, column=1)

    # Encoding part
    poly_Caesar_Label_subhead_1.grid(row=1, column=0)

    poly_Caesar_Label_1.grid(row=2, column=0)
    poly_Caesar_Label_2.grid(row=2, column=1)
    poly_Caesar_Label_3.grid(row=3, column=1)

    poly_Caesar_Entry_1.grid(row=3, column=0)

    poly_Caesar_Button_1.grid(row=4, column=0)
    poly_Caesar_Button_2.grid(row=4, column=1)

    placeholder_Label.grid(row=5, column=0)

    # Decoding part
    poly_Caesar_Label_subhead_2.grid(row=6, column=0)

    poly_Caesar_Label_4.grid(row=7, column=0)
    poly_Caesar_Label_5.grid(row=7, column=1)
    poly_Caesar_Label_6.grid(row=8, column=1)

    poly_Caesar_Entry_2.grid(row=8, column=0)

    poly_Caesar_Button_3.grid(row=9, column=0)
    poly_Caesar_Button_4.grid(row=9, column=1)

def destroy_Poly_Caesar():
    poly_Caesar_Label_head.grid_remove()

    # Encoding part
    poly_Caesar_Label_subhead_1.grid_remove()

    poly_Caesar_Label_1.grid_remove()
    poly_Caesar_Label_2.grid_remove()
    poly_Caesar_Label_3.grid_remove()

    poly_Caesar_Entry_1.grid_remove()

    poly_Caesar_Button_1.grid_remove()
    poly_Caesar_Button_2.grid_remove()

    placeholder_Label.grid_remove()

    # Decoding part
    poly_Caesar_Label_subhead_2.grid_remove()

    poly_Caesar_Label_4.grid_remove()
    poly_Caesar_Label_5.grid_remove()
    poly_Caesar_Label_6.grid_remove()

    poly_Caesar_Entry_2.grid_remove()

    poly_Caesar_Button_3.grid_remove()
    poly_Caesar_Button_4.grid_remove()

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

#Mono Caesar Code use
def use_Mono_Caesar_Encode():
    text = mono_Caesar_Entry_1.get()
    key = int(mono_Caesar_Entry_2.get())

    encoded_text = mc.mono_Caesar_Encode(text,key)

    mono_Caesar_Label_4.config(text=encoded_text)
    print(encoded_text)

def use_Mono_Caesar_Decode():
    text = mono_Caesar_Entry_3.get()
    key = int(mono_Caesar_Entry_4.get())

    decoded_text = mc.mono_Caesar_Decode(text,key)

    mono_Caesar_Label_8.config(text=decoded_text)
    print(decoded_text)

#Poly Caesar Code use 
def use_Poly_Caesar_Encode():
    text = poly_Caesar_Entry_1.get()

    encoded_text = pc.poly_Caesar_Encode(text)

    poly_Caesar_Label_3.config(text=encoded_text)
    print(encoded_text)

def use_Poly_Caesar_Decode():
    text = poly_Caesar_Entry_2.get()

    decoded_text = pc.poly_Caesar_Decode(text)

    poly_Caesar_Label_6.config(text=decoded_text)
    print(decoded_text)


def mono_Clear_Entry_1():
    mono_Caesar_Entry_1.delete(0,'end')

def mono_Clear_Entry_2():
    mono_Caesar_Entry_2.delete(0,'end')

def mono_Clear_Entry_3():
    mono_Caesar_Entry_3.delete(0,'end')

def mono_Clear_Entry_4():
    mono_Caesar_Entry_4.delete(0,'end')

def poly_Clear_Entry_1():
    mono_Caesar_Entry_1.delete(0,'end')

def poly_Clear_Entry_2():
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

    placeholder_Label = Label(root,  text=' ')

    #Mono Caesar
    #Encode
    mono_Caesar_Label_head = Label(root, 
        text='''  Caeser-Verschlüsselung nach 
Monoalphabetischer Substitution''',
        font=("Courier", 11))
    mono_Caesar_Label_subhead_1 = Label(root,   text='Verschlüsselung',
                                                font=("Courier", 10))
    mono_Caesar_Label_1 = Label(root, text='lesbarer Text')
    mono_Caesar_Label_2 = Label(root, text='Schlüsselzahl')
    mono_Caesar_Label_3 = Label(root, text='verschlüsselter Text')
    mono_Caesar_Label_4 = Label(root, text='jcnnq ygnv!')

    mono_Caesar_Entry_1 = Entry(root)
    mono_Caesar_Entry_2 = Entry(root)

    mono_Caesar_Button_1 = Button(root, text="Eingabefeld leeren",
                                        command=mono_Clear_Entry_1)
    mono_Caesar_Button_2 = Button(root, text="Eingabefeld leeren",
                                        command=mono_Clear_Entry_2)
    mono_Caesar_Button_3 = Button(root, text="anwenden", 
                                        command=use_Mono_Caesar_Encode)
    #Decode
    mono_Caesar_Label_subhead_2 = Label(root,   text='Entschlüsselung',
                                                font=("Courier", 10))    
    mono_Caesar_Label_5 = Label(root, text='verschlüsselter Text')
    mono_Caesar_Label_6 = Label(root, text='Schlüsselzahl')
    mono_Caesar_Label_7 = Label(root, text='lesbarer Text')
    mono_Caesar_Label_8 = Label(root, text='hallo welt!')

    mono_Caesar_Entry_3 = Entry(root)
    mono_Caesar_Entry_4 = Entry(root)

    mono_Caesar_Button_4 = Button(root, text="Eingabefeld leeren",
                                        command=mono_Clear_Entry_3)
    mono_Caesar_Button_5 = Button(root, text="Eingabefeld leeren",
                                        command=mono_Clear_Entry_4)
    mono_Caesar_Button_6 = Button(root, text="anwenden", 
                                        command=use_Mono_Caesar_Decode)

    #Poly Caesar
    #Encode
    poly_Caesar_Label_head = Label(root, 
        text='''  Caeser-Verschlüsselung nach 
Polyalphabetischer Substitution''',
        font=("Courier", 11))
    poly_Caesar_Label_subhead_1 = Label(root,   text='Verschlüsselung',
                                                font=("Courier", 10))
    poly_Caesar_Label_1 = Label(root, text='lesbarer Text')
    poly_Caesar_Label_2 = Label(root, text='verschlüsselter Text')
    poly_Caesar_Label_3 = Label(root, text='hbnos cltc!')

    poly_Caesar_Entry_1 = Entry(root)

    poly_Caesar_Button_1 = Button(root, text="Eingabefeld leeren",
                                        command=poly_Clear_Entry_1)
    poly_Caesar_Button_2 = Button(root, text="anwenden", 
                                        command=use_Poly_Caesar_Encode)
    #Decode
    poly_Caesar_Label_subhead_2 = Label(root,   text='Entschlüsselung',
                                                font=("Courier", 10))    
    poly_Caesar_Label_4 = Label(root, text='verschlüsselter Text')
    poly_Caesar_Label_5 = Label(root, text='lesbarer Text')
    poly_Caesar_Label_6 = Label(root, text='hallo welt!')

    poly_Caesar_Entry_2 = Entry(root)

    poly_Caesar_Button_3 = Button(root, text="Eingabefeld leeren",
                                        command=poly_Clear_Entry_2)
    poly_Caesar_Button_4 = Button(root, text="anwenden", 
                                        command=use_Poly_Caesar_Decode)

    #Mono Caesar is loaded first
    create_Mono_Caesar()

    create_gui()

    
    