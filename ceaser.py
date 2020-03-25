alphabet = 'abcdefghijklmnopqrstuvwxyz'

def adjust_Data(text, code):
    '''Hilfsfunktion zum anpassen der Daten'''
    text = text.lower()

    while code > 26 or code < 0:
        '''
        Schleife um sicherzustellen,  dass der Angegebene Code-Schlüssel sich 
        im Bereich zwischen 0 und 26 befindet.
        '''
        if code > 26:
            code -= 26
        if code < 0:
            code += 26

def caeser_Encode(input_text, code):

    replace_alphabet = alphabet[code:] + alphabet[:code]
    encoded_text=''

    for i in input_text:
        try:
            key_index = alphabet.index(i)
            new_key = replace_alphabet[key_index]
            encoded_text += new_key
        except Exception:
            encoded_text += i
    return encoded_text

def caeser_Decode(encoded_text, code):
    pass

if __name__=='__main__':
    input_text = input('Geben sie einen Text ein: ').lower()
    code = int(input('''Geben sie nun ein um wie viele Zeichen der Text verschoben werden soll: '''))

    print(caeser_Encode(input_text,code))