from math import pow
from random import choice, randrange

class Person:
    def __init__(self):
    # Eine Liste mit Primzahlen zwischen 10900 und 11000 um eine große Primzahl 
    # auszuwählen. Die Primzahl wird dabei immer zufällig gewählt. Es sind 
    # insgesamt 10 Primzahlen vorhanden.
        primes = [10903, 10909, 10937, 10939, 10949, 10957, 10973, 10979, 10987, 10993]

        self.prime = choice(primes)
        self.num_g = randrange(2, self.prime - 2)
        self.num = randrange(2, self.prime - 2)

    def get_Values(self):
        return self.prime, self.num_g
    
    def reinit_Values(self, prime, num_g):
        self.prime = prime
        self.num_g = num_g
        self.num = randrange(2, self.prime - 2)
    
    def get_Big_Number(self):
        self.big_Number = self.num_g ** self.num % self.prime
        return self.big_Number
    
    def get_Key(self, cls):
        key = (cls.get_Big_Number()** self.num) % self.prime
        self.key = key
        return self.key



if __name__ == '__main__':

    Person_a = Person()
    Person_b = Person()

    values = Person_a.get_Values()
    Person_b.reinit_Values(values[0], values[1])

    key_1 = Person_a.get_Key(Person_b)
    key_2 = Person_b.get_Key(Person_a)

    print(f'Person 1 Nummer: {Person_a.num}')
    print(f'Person 2 Nummer: {Person_b.num}\n')

    print(f'Key 1: {key_1}')
    print(f'Key 2: {key_2}\n')

    print(f'Die Keys stimmen über ein: {key_1 == key_2}')

