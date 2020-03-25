input_text = input('Geben sie einen Text ein: ').lower()

code = int(input('Geben sie nun ein um wie viele Zeichen der Text verschoben werden soll: '))

alphabet = 'abcdefghijklmnopqrstuvwxyz'



def caeser_Encode(input_text,code):

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

def caeser_Decode(encoded_text,code):
    pass

print(caeser_Encode(input_text,code))