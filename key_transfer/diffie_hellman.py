from math import pow
from random import choice, randrange

class person:
    def __init__(self, num, prime = None, num_g = None):
    # Eine Liste mit Primzahlen zwischen 54950 und 55000 um eine große Primzahl 
    # auszuwählen. Die Primzahl wird dabei immer zufällig gewählt. Es sind 
    # insgesamt 9 Primzahlen vorhanden.
        primes = [54907, 54917, 54919, 54941, 54949, 54959, 54973, 54979, 54983]
        self.num = num

        if prime == None:
            self.prime = choice(primes)
        else:
            self.prime = prime
        
        if num_g == None:
            self.num_g = randrange(2, self.prime - 2)
        else:
            self.num_g = num_g

    def get_values(self):
        return self.prime, self.num_g



if __name__ == '__main__':
    a= int(input('Gib die nummer für person a an: '))
    b= int(input('Gib die nummer für person b an: ')) 

    person_a = person(a)
    person_b = person(b, person_a.get_values()[0], person_a.get_values()[1])

    print(person_a.get_values())
    print(person_b.get_values())

