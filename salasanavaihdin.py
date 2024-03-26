import random
import string
import unittest

runtest = 1

def generate_password():
    nominit = ['pöytä', 'tuoli', 'omena,', 'päärynä', 'pyörä', 'ruuvi', 
               'ruusu', 'neilikka', 'leppäkerttu', 'perhonen', 'kala', 'mökki',
               'kenkä', 'sukka', 'puhelin', 'kello', 'radio', 'telkkari', 'jauho', 
               'jyvä', 'kynsi', 'tukka', 'vesi', 'öljy', 'kivi', 'puurunko']

    adjektiivit = ['nopea', 'hitas', 'kiltti', 'tuhma', 'iso', 'pieni', 'pimeä',
                   'vaalea', 'tahmea', 'liukas', 'punainen', 'sininen',
                   'hiljas', 'äänekäs', 'jännittävä', 'tylsä', 'kylmä', 'lämmin', 'tuulinen', 
                   'tyyni', 'komea', 'ruma', 'kevyt', 'painava', 'kiero', 'suora']
    
    while True:
        adjektiivi = random.choice(adjektiivit)
        nomini = random.choice(nominit)
        numero = str(random.randrange(10, 100))
        erikoismerkki = random.choice(string.punctuation)
        
        salasana = adjektiivi + nomini + numero + erikoismerkki
        '''print(min(nominit, key=len))'''
        if runtest == 0:
            print('salasanasi on: ' + salasana)
            vastaus = input('Haluatko toisen salasanan? Vastaa k tai e: ')
            if vastaus == 'e':
                break
            else:
                return generate_password()
        else:
            return salasana


if runtest == 0:
    generate_password()

# Testit
# Class nimi pitää olla sama kuin tiedoston nimi
class salasanavaihdin(unittest.TestCase):
    def test_generate_password_success(self):
        actual = len(generate_password())
        expected = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        print('actual= ', actual)
        self.assertIn(actual, expected)