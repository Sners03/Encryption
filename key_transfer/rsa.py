from random import choice

def ggt(a, b):
    while b!=0:
        c=a%b
        a, b= b, c
    return a

def rsa_encode(message, e):
    # Eine Liste mit Primzahlen zwischen 10800 und 11000 um eine große Primzahl 
    # auszuwählen. Die Primzahl wird dabei immer zufällig gewählt. Es sind 
    # insgesamt 20 Primzahlen vorhanden.
    primes = [
        10831, 10837, 10847, 10853, 10859, 10861, 10867, 10883, 10889, 10891,
        10903, 10909, 10937, 10939, 10949, 10957, 10973, 10979, 10987, 10993
    ]
    #p = choice(primes)
    #primes.remove(p)
    #q = choice(primes)

    p = 5
    q = 11

    n = p * q

    phi = (p-1) * (q-1)

    while ggt(phi, e) != 1:
        print('Bitte geben sie einen anderen Schlüssel an')
        print(f'e muss teilerfremd zu {phi} sein')
        print('Größere Primzahlen als öffentlicher schlüssel bieten sich an!')
        e = int(input())
        print('')
    
    encoded = (message ** e) % n
    return encoded, n, e

def rsa_decode(encoded, n, e):
    pass

if __name__ == '__main__':
    try:
        print(f'Für die Verschlüsselung darf der Schlüssel nicht mehr als {10831* 10837} betragen.')
        print('Dies ist das Produkt der beiden kleinsten Primzahlen, die verwendet werden.')
        message = int(input('Gib eine zu verschlüselnde Nachricht (Zahl) ein:'))
        
        encoded, n, e = rsa_encode(message,7)
        print(encoded)

    except Exception:
        print(Exception)