# vigenere.py
# Vigenére-Verschlüsselung 

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# c = Zeichen ((zahl(K)+zahl(e)) Modulo 26)

def vignere_Encode(input_text, key):

    key_length = len(key)
    key_pos = 0
    encoded_text = ''

    for i in input_text:
        try:

            key_char = key[key_pos]
            encoded_char_pos = (alphabet.index(i) + alphabet.index(key_char)) % 26

            encoded_text += alphabet[encoded_char_pos]

        except Exception:
            encoded_text += i

        if key_pos != key_length-1:
            key_pos += 1
        else:
            key_pos = 0

    return encoded_text

if __name__ == '__main__':

    input_text = input('Geben sie einen Text ein: ').lower()
    key = input('Geben sie ihr schlüsselwort ein: ').lower()

    encoded_text = vignere_Encode(input_text, key)

    print(encoded_text)