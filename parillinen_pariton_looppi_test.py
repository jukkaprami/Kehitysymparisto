import unittest
runtest = 1

def parillisuus(luku):
    for counter in range(1, luku + 1):
        if (counter % 2) == 0:
            print(counter)
            palautusarvo = "on parillinen"
            print(palautusarvo)
        else:
            print(counter)
            palautusarvo = "on pariton"
            print(palautusarvo)
    if runtest == 1:
        return palautusarvo

if runtest == 0:
    parillisuus(2)

# python -m unittest parillinen_pariton_looppi.py
class parillinen_pariton_looppi(unittest.TestCase):
  def test_parillinen_pariton_looppi_success_parillinen(self):
        testiarvo = 4
        actual = str(parillisuus(testiarvo))
        expected = 'on parillinen'
        try: 
            assert actual == expected
        except:  
            print('Virhe parittomuuden tarkistamisessa' + ' Numero = ' + str(testiarvo) + ' ' + actual + ' != ' + expected)

  def test_parillinen_pariton_looppi_success_pariton(self):
        testiarvo = 3
        actual = str(parillisuus(testiarvo))
        expected = 'on pariton'
        try: 
            assert actual == expected
        except:  
            print('Virhe parittomuuden tarkistamisessa' + ' Numero = ' + str(testiarvo) + ' ' + actual + ' != ' + expected)