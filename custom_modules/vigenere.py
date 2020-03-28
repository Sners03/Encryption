# vigenere.py
# Vigenére-Verschlüsselung 

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# c = Zeichen ((zahl(K)+zahl(e)) Modulo 26)

def vigenere_Encode(input_text, key):  
    '''
    Funktion, welche die Vigenére-Verschlüsselung anwendet um einen Text zu 
    verschlüsseln.

    input:

    input_text
    input_text  (str)-->    Der Eingegebene Text
    key         (str)-->    Der Schlüssel für den Text

    output:

    encoded_text
    encoded_text (str)-->   Der Verschlüsselte Text nach der 
                            Vigenére-Verschlüsselung
    '''
    input_text = input_text.lower()
    key_length = len(key)
    key_pos = 0
    encoded_text = ''
# für jeden Buchstaben im Text
    for i in input_text:
        try:
# c = Zeichen ((zahl(K)+zahl(e)) Modulo 26)
            key_char = key[key_pos] # K = i; e = key_char
            encoded_char_pos = (alphabet.index(i) + 
                                alphabet.index(key_char)) % 26

            encoded_text += alphabet[encoded_char_pos]

#Zeichen mtnehmen, welche nicht Teil des Alphabets sind
        except Exception:
            encoded_text += i

# rotieren durch den Schlüssel
        if key_pos != key_length-1:
            key_pos += 1
        else:
            key_pos = 0

    return encoded_text

def vigenere_Decode(encoded_text, key):
    '''
    Funktion um einen mit der Vigenére-Verschlüsselung verschlüsselten Text
    wieder zu entschlüsseln. Der Schlüssel wird dafür benötigt.

    input:

    encoded_text, key
    encoded_text    (str)-->    Ein verschlüsselter Text
    key             (str)-->    Der Schlüssel für den Text

    output:

    decoded_text
    decoded_text (str)-->   Der Entschlüsselte Text 
    '''
    key_length = len(key)
    key_pos = 0
    decoded_text = ''
# für jeden Buchstaben im Text
    for i in encoded_text:
        try:
# K = Zeichen ((26 + Zahl(c) - zahl(e)) Modulo 26)
            key_char = key[key_pos] # c = i; e = key_char 
            decoded_char_pos = (26 + alphabet.index(i) - 
                                alphabet.index(key_char)) % 26

            decoded_text += alphabet[decoded_char_pos]
#Zeichen mtnehmen, welche nicht Teil des Alphabets sind (z.B. '!','?','ü', ' ')
        except Exception:
            decoded_text += i
# rotieren durch den Schlüssel
        if key_pos != key_length-1:
            key_pos += 1
        else:
            key_pos = 0

    return decoded_text

if __name__ == '__main__':

    input_text = input('Geben sie einen Text ein: ').lower()
    key = input('Geben sie ihr schlüsselwort ein: ').lower()

    encoded_text = vigenere_Encode(input_text, key)
    decoded_text = vigenere_Decode(encoded_text, key)

    print(encoded_text)
    print(decoded_text)