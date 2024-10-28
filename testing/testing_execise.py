import pdb
import unittest
import random


def guess_game(answer=0):
    random_answer = random.randint(1, 10)

    if type(answer) == bool or type(answer) != int:
        return 'Error input a number'

    if answer < 1 or answer > 10:
        return 'Ans must be between 0 and 11'

    answer = int(answer)
    if random_answer == answer:
        return f'you got the answer right {random_answer}'
    return f'{answer} is wrong kindly try again  right ans: {random_answer}'



class GuessTest(unittest.TestCase):

    def test_with_string(self):
        self.assertEqual(guess_game('pineapple'), 'Error input a number')

    def test_with_greater_than(self):
        self.assertEqual(guess_game(100), 'Ans must be between 0 and 11')

    def test_with_bool(self):
        self.assertEqual(guess_game(True), 'Error input a number')
        
    def test_with_none(self):
        self.assertEqual(guess_game(None), 'Error input a number')


if __name__ == '__main__':
    unittest.main()
    # guess_game(9)
    # guess_game(True)
