import random
import unittest



lives = 9
words = ['pizza', 'keiju', 'sorsa', 'kieli', 'paita', 'kirje']

secret_word = random.choice(words)

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
    updated_clue = clue
    return updated_clue
    
# Prevent this module to be run by other modules
if __name__ == "__main__":
    
    while lives > 0:
        print(clue)
        print('Henkia jaljella: ' + heart_symbol * lives)
        
        guess = input(' Arvaa kirjain tai koko sana: ')
        
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
                print(secret_word)