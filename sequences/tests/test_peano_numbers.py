import unittest
from sequences.peano_numbers import *


class TestPeanoNumbers(unittest.TestCase):
    def test_to_int(self):
        self.assertEqual(to_int(None), 0)
        self.assertEqual(to_int(Num(None)), 1)
        self.assertEqual(to_int(Num(Num(None))), 2)
        self.assertEqual(to_int(Num(Num(Num(None)))), 3)

    def test_from_int(self):
        self.assertEqual(from_int(0), None)
        self.assertEqual(from_int(1), Num(None))
        self.assertEqual(from_int(2), Num(Num(None)))
        self.assertEqual(from_int(3), Num(Num(Num(None))))

    def test_add(self):
        # 0 + 0 = 0
        self.assertEqual(add(a=None, b=None), None)
        # 0 + 1 = 1
        self.assertEqual(add(a=Num(None), b=None), Num(None))
        self.assertEqual(add(a=None, b=Num(None)), Num(None))
        # 1 + 2 = 3
        self.assertEqual(add(a=Num(None), b=Num(Num(None))), Num(Num(Num(None))))
        # 2 + 2 = 4
        self.assertEqual(add(a=Num(Num(None)), b=Num(Num(None))), Num(Num(Num(Num(None)))))

    def test_subtract(self):
        # smallest peano number is zero
        self.assertEqual(subtract(a=None, b=None), None)
        self.assertEqual(subtract(a=None, b=Num(None)), None)
        self.assertEqual(subtract(a=Num(None), b=Num(Num(None))), None)
        # 1 - 0 = 1
        self.assertEqual(subtract(a=Num(None), b=None), Num(None))
        # 2 - 1 = 1
        self.assertEqual(subtract(a=Num(Num(None)), b=Num(None)), Num(None))
        # 4 - 2 = 2
        self.assertEqual(subtract(
            a=Num(Num(Num(Num(None)))), b=Num(Num(None))), Num(Num(None)))

    def test_multiply(self):
        # smallest peano number is zero
        self.assertEqual(multiply(a=None, b=None), None)
        self.assertEqual(multiply(a=None, b=Num(None)), None)
        self.assertEqual(multiply(a=Num(None), b=None), None)
        self.assertEqual(multiply(a=Num(None), b=Num(None)), Num(None))
        self.assertEqual(multiply(
            a=Num(Num(None)), b=Num(Num(None))), Num(Num(Num(Num(None)))))
        # 2 * 3 = 6
        self.assertEqual(multiply(
            a=Num(Num(None)), b=Num(Num(Num(None)))), Num(Num(Num(Num(Num(Num(None)))))))


if __name__ == '__main__':
    unittest.main()
