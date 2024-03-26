import random
import unittest

runtest = 0
def yhdeksan_henkea(guess_test):
    lives = 9
    words = ['pizza', 'keiju', 'sorsa', 'kieli', 'paita', 'kirje']
    if runtest == 0:
        secret_word = random.choice(words)
    if runtest == 1:
        secret_word = guess_test
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
            guess = guess_test
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

class test_yhdeksan_henkea_v2(unittest.TestCase):
    def test_yhdeksan_henkea_success(self):
        actual = yhdeksan_henkea('pizza')
        excepted = ['pizza']
        print('actual = ', actual)
        self.assertIn(actual, excepted)

    def test_yhdeksan_henkea_success2(self):
        actual = yhdeksan_henkea('keiju')
        excepted = ['keiju']
        print('actual = ', actual)
        self.assertIn(actual, excepted)

    def test_yhdeksan_henkea_success3(self):
        actual = yhdeksan_henkea('sorsa')
        excepted = ['sorsa']
        print('actual = ', actual)
        self.assertIn(actual, excepted)
    
    def test_yhdeksan_henkea_success4(self):
        actual = yhdeksan_henkea('kieli')
        excepted = ['kieli']
        print('actual = ', actual)
        self.assertIn(actual, excepted)

    def test_yhdeksan_henkea_success5(self):
        actual = yhdeksan_henkea('paita')
        excepted = ['paita']
        print('actual = ', actual)
        self.assertIn(actual, excepted)
    
    def test_yhdeksan_henkea_success6(self):
        actual = yhdeksan_henkea('kirje')
        excepted = ['kirje']
        print('actual = ', actual)
        self.assertIn(actual, excepted)