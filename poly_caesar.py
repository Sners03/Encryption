# poly_caesar.py
# Caeser-Verschlüsselung nach Polyalphabetischer Substitution

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def get_replace_alphabet(code):
    '''

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

def 