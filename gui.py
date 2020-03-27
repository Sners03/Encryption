from custom_modules import mono_caesar as mc 
from custom_modules import poly_caesar as pc 
from custom_modules import vigenere as vig 
import tkinter as tk

if __name__ == '__main__':
    encoded = mc.mono_Caesar_Encode('Hallo Welt', 2)
    print(encoded)