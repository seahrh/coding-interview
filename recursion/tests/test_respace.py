import unittest
from recursion.respace import *


class TestRespace(unittest.TestCase):
    def test_given_empty_text_then_return_empty_string(self):
        self.assertEqual(split(dictionary={'i'}, text=''), '')

    def test_given_empty_dictionary_then_return_space_after_every_character(self):
        self.assertEqual(split(dictionary=set(), text='helloworld'), 'h e l l o w o r l d')

    def test_given_text_of_three_words(self):
        self.assertEqual(split(
            dictionary={'i', 'am', 'legend'}, text='iamlegend'), 'i am legend')

    def test_given_text_of_repeating_words(self):
        self.assertEqual(split(
            dictionary={'i', 'am', 'legend'}, text='iamlegendlegendami'), 'i am legend legend am i')

    def test_given_example_1(self):
        self.assertEqual(split(
            dictionary={'this', 'is', 'mikes', 'favorite', 'food'},
            text='thisismikesfavoritefood'), 'this is mikes favorite food')

    def test_given_example_2(self):
        self.assertEqual(split(
            dictionary={'looked', 'just', 'like', 'her', 'brother'},
            text='jesslookedjustliketimherbrother'), 'j e s s looked just like t i m her brother')

    def test_given_example_3(self):
        self.assertEqual(split(
            dictionary={'i', 'reset', 'the', 'computer', 'it', 'still', 'did', 'not', 'boot'},
            text='iresetthecomputeritstilldidnotboot'), 'i reset the computer it still did not boot')


if __name__ == '__main__':
    unittest.main()
