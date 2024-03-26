# This module contains tests for module moduleToTest_yhdeksan henkea

# libraries and modules

import unittest # module for test classes
import yhdeksan_henkea_v2_copy

# Test classes

class ClueTest(unittest.TestCase):

    def test_update_clue(self):
        """Updates the clue pattern according to the guess

        Args:
            guessed_letter (str): letter or word given
            secret_word (str): word to check against
            clue (list): letter pattern (list of characters)

        Returns:
            list: updated clue pattern
        """
        clue = list('?????')
        secret_word = 'sorsa'
        guessed_word = 's'
        result = yhdeksan_henkea_v2_copy.update_clue(guessed_word, secret_word, clue)
        expected_result = list('s??s?')
        self.assertEqual(result, expected_result)



if __name__ == "__main__":
    unittest.main()