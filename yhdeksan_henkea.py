# yhdeksan_henkea
# Jukka Prami

import random
import unittest

runtest = 0
def yhdeksan_henkea(guess_word, guess_char):
    lives = 9
    words = ['pizza', 'keiju', 'sorsa', 'kieli', 'paita', 'kirje', 
            'jalka', 'pyora', 'ankka', 'koivu', 'ahven', 'purje',
            'varsi', 'ruuvi', 'ruoka', 'ruusu', 'maito', 'lahde']
    if runtest == 0:
        secret_word = random.choice(words)
    if runtest == 1:
                secret_word = guess_word
                print(secret_word)
    clue = list('?????') 
    clue_str = ''.join(clue)
    heart_symbol = u'\u2764'
    guessed_word_correctly = False

    def update_clue(guessed_letter, secret_word, clue):
        index = 0
        while index < len(secret_word):
            if guessed_letter == secret_word[index]:
                clue[index] = guessed_letter
            index = index + 1

    while lives > 0:
        print(clue)
        print('Henkia jaljella: ' + heart_symbol * lives)
        if runtest == 0:
            guess = input(' Arvaa kirjain tai koko sana: ')
        if runtest == 1:
            if guess_char == None:
                guess = guess_word
            else:
                guess = guess_char
        

        if guess in secret_word:
            update_clue(guess, secret_word, clue)
            clue_str = ''.join(clue)
            
                        
        else:
            print('Vaarin. Menetit yhden hengen.')
            lives = lives - 1
            if lives == 0:
                print('Havisit! Salainen sana oli: ' + secret_word)
        if guess == secret_word or clue_str == secret_word:
            guessed_word_correctly = True
            if guessed_word_correctly:
                print('Voitit! Salainen sana oli: ' + secret_word)
                return secret_word

if runtest == 0:
    yhdeksan_henkea('')

class test_yhdeksan_henkea(unittest.TestCase):
    def test_yhdeksan_henkea_success(self):
        words = ['pizza', 'keiju', 'sorsa', 'kieli', 'paita', 'kirje', 
                'jalka', 'pyora', 'ankka', 'koivu', 'ahven', 'purje',
                'varsi', 'ruuvi', 'ruoka', 'ruusu', 'maito', 'lahde']
        for i in words:
            actual = yhdeksan_henkea(i, None)
            expected = i
            print('actual = ', actual)
            self.assertIn(actual, expected)

            
    def test_yhdeksan_henkea_success2(self):
        words = ['pizza', 'keiju', 'sorsa', 'kieli', 'paita', 'kirje', 
                'jalka', 'pyora', 'ankka', 'koivu', 'ahven', 'purje',
                'varsi', 'ruuvi', 'ruoka', 'ruusu', 'maito', 'lahde']
        for i in words:
            for j in (i):
                actual = yhdeksan_henkea(i, j)
                expected = j
                print('actual = ', actual)
                self.assertIn(actual, expected)


# python -m unittest yhdeksan_henkea