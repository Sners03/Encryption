# mono_caesar.py 
# Caeser-Verschlüsselung nach Monoalphabetischer Substitution

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def adjust_Data(text, code):
    '''
    Hilfsfunktion zum anpassen der Daten

    input:

    text, code
    text    (str)-->    Der Eingegebene Text
    code    (int)-->    Code zur Verschiebung des Alphabets

    output:

    text, code
    text    (str)-->   Text nur mit lowercase Buchstaben
    code    (int)-->   Der, auf die größe des Alphabets, zugeschnittene Code
    '''
    text = text.lower()

    if code > 26 or code < 0:
        code %= 26

    return text, code


def mono_Caesar_Encode(input_text, code):
    '''
    Funktion, welche die monoalphabetische Caesar-Verschlüsselung anwendet um 
    einen Text zu verschlüsseln.

    input:

    input_text, code
    input_text  (str)-->    Der Eingegebene Text
    code        (int)-->    Code zur Verschiebung des Alphabets

    output:

    encoded_text
    encoded_text (str)-->   Der Verschlüsselte Text nach der 
                            Caeser-Verschlüsselung
    '''

    input_text, code = adjust_Data(input_text, code)

    replace_alphabet = alphabet[code:] + alphabet[:code]
    encoded_text=''

    for i in input_text:
        '''
        In dieser Schleife werden die Buchstaben in einem neuen Text durch die 
        verschobenen Buchstaben ausgetauscht.

        Das Exception-Handling wird so genutzt, dass wenn ein Zeichen, welches 
        nicht Teil des Alphabets ist, auftritt, dieses Zeichen einfach in den 
        Verschlüsselten Text weitergegeben wird. So bleibt ein Leerzeichen ein
        Leerzeichen und ein '!' bleibt ein '!'
        '''
        try:
            key_index = alphabet.index(i)
            new_key = replace_alphabet[key_index]
            encoded_text += new_key
        except Exception:
            encoded_text += i

    return encoded_text

def mono_Caesar_Decode(encoded_text, code):
    '''
    Funktion um einen mit der monoalphabetische Caesar-Verschlüsselung 
    verschlüsselten Text wieder zu entschlüsseln. Der Code wird dafür benötigt.

    input:

    encoded_text, code
    encoded_text    (str)-->    Ein verschlüsselter Text
    code            (int)-->    Code zur Verschiebung des Alphabets welcher zu 
                                der Verschlüsselung gehört.

    output:

    decoded_text
    decoded_text (str)-->   Der Entschlüsselte Text 
    '''
    encoded_text, code = adjust_Data(encoded_text, code)

    replace_alphabet = alphabet[code:] + alphabet[:code]
    decoded_text = ''

    for i in encoded_text:
        '''
        In dieser Schleife werden die verschobenen Buchstaben zurückgeschoben.

        Das Exception-Handling wird so genutzt, dass wenn ein Zeichen, welches 
        nicht Teil des Alphabets ist, auftritt, dieses Zeichen einfach in den 
        Verschlüsselten Text weitergegeben wird. So bleibt ein Leerzeichen ein
        Leerzeichen und ein '!' bleibt ein '!'
        '''
        try:
            key_index = replace_alphabet.index(i)
            new_key = alphabet[key_index]
            decoded_text += new_key
        except Exception:
            decoded_text += i

    return decoded_text




if __name__=='__main__':

    input_text = input('Geben sie einen Text ein: ')
    code = int(input('Geben sie nun ein um wie viele Zeichen der Text verschoben werden soll: '))

    encoded_text = mono_Caesar_Encode(input_text,code)
    decoded_text = mono_Caesar_Decode(encoded_text, code)
 
    print(input_text,'\n',code)
    print(encoded_text)
    print(decoded_text)