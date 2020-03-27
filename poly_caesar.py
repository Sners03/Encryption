# poly_caesar.py
# Caeser-Verschlüsselung nach Polyalphabetischer Substitution

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def get_replace_alphabet(code):
    '''
    Hilfsfunktion um das Alphabet zu verschieben.

    input:

    code
    code            (int)-->    Code zur Verschiebung des Alphabets

    output:
    replace_alphabet(str)-->    Das für die Verschiebung benötigte Alphabet

    '''
    if code > 26:
        code %= 26
    replace_alphabet = alphabet[code:] + alphabet[:code]

    return replace_alphabet

def poly_Caesar_Encode(input_text):
    '''
    Funktion, welche die polyalphabetische Caesar-Verschlüsselung anwendet um 
    einen Text zu verschlüsseln.

    input:

    input_text
    input_text  (str)-->    Der Eingegebene Text

    output:

    encoded_text
    encoded_text (str)-->   Der Verschlüsselte Text nach der 
                            Caeser-Verschlüsselung
    '''
    encoded_text = ''
    input_text = input_text.lower()

    for i in range(len(input_text)):
        replace_alphabet = get_replace_alphabet(i)
        try:
            key_index = alphabet.index(input_text[i])
            new_key = replace_alphabet[key_index]
            encoded_text += new_key
        except Exception:
            encoded_text += input_text[i]
    
    return encoded_text


def poly_Caesar_Decode(encoded_text):
    '''
    Funktion um einen mit der polyalphabetischen Caesar-Verschlüsselung 
    verschlüsselten Text wieder zu entschlüsseln. Der Code wird dafür benötigt.

    input:

    encoded_text
    encoded_text    (str)-->    Ein verschlüsselter Text

    output:

    decoded_text
    decoded_text (str)-->   Der Entschlüsselte Text 
    '''
    decoded_text = ''
    encoded_text = encoded_text.lower()

    for i in range(len(encoded_text)):
        '''
        In dieser Schleife werden die verschobenen Buchstaben zurückgeschoben.

        Das Exception-Handling wird so genutzt, dass wenn ein Zeichen, welches 
        nicht Teil des Alphabets ist, auftritt, dieses Zeichen einfach in den 
        Verschlüsselten Text weitergegeben wird. So bleibt ein Leerzeichen ein
        Leerzeichen und ein '!' bleibt ein '!'
        '''
        replace_alphabet = get_replace_alphabet(i)

        try:
            key_index = replace_alphabet.index(encoded_text[i])
            new_key = alphabet[key_index]
            decoded_text += new_key
        except Exception:
            decoded_text += i
    
    return decoded_text

if __name__=='__main__':

    input_text = input('Geben sie einen Text ein: ').lower()

    encoded_text = poly_Caesar_Encode(input_text)   
    decoded_text = poly_Caesar_Decode(encoded_text)

    print(input_text)
    print(encoded_text)
    print(decoded_text)