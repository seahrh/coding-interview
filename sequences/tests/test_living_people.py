import unittest
from sequences.living_people import *


class TestLivingPeople(unittest.TestCase):
    def test_when_array_is_empty_then_return_none(self):
        self.assertEqual(year_with_most_people_alive([]), None)

    def test_given_one_person_only_when_yob_equals_yod_then_return_same_year(self):
        self.assertEqual(
            year_with_most_people_alive([
                Person(1900, 1900)
            ]), 1900)

    def test_given_two_persons_only(self):
        self.assertEqual(
            year_with_most_people_alive([
                Person(1900, 1910),
                Person(1910, 1911)
            ]), 1910)


if __name__ == '__main__':
    unittest.main()
