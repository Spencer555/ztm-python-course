# testing - a method where individual units are tested to see if they work properly

# a test is another python file accompanying one of your files you want to test and this file never runs in production its only for development


import unittest
from main import do_stuff


class TestMain(unittest.TestCase):

    def setUp(self):
        # this runs before the test of a function
        print('this runs before each test runs')

    def test_do_stuff(self):
        test_param = 10
        result = do_stuff(test_param)

        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'string'
        result = do_stuff(test_param)

        # since we are returning value error the result is an instance of the value error
        self.assertTrue(isinstance(result, ValueError))


# even though we are repeating ourselves its fine test dont go into production so you want to have a readable and descriptive test

    def test_do_stuff3(self):
        test_param = None
        result = do_stuff(test_param)

        self.assertEqual(result, 'pls enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = do_stuff(test_param)

        self.assertEqual(result, 'pls enter number')

    def test_do_stuff5(self):
        test_param = 0
        result = do_stuff(test_param)

        self.assertEqual(result, 'pls enter number')

    def tearDown(self):
        # to clean up some vars and mostly used for testing dbase or complex stuff but not used often
        print('cleaning up')


# run the test
# so it dont run when we import  it only run this code when its the file being run
if __name__ == '__main__':
    unittest.main()


# this -v means verbose and gives us more info on the test
# python -m nameoftestfile -v
