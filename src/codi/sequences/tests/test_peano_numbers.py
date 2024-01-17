from codi.sequences.peano_numbers import *


class TestPeanoNumbers:
    def test_to_int(self):
        assert to_int(None) == 0
        assert to_int(Num(None)) == 1
        assert to_int(Num(Num(None))) == 2
        assert to_int(Num(Num(Num(None)))) == 3

    def test_from_int(self):
        assert from_int(0) is None
        assert from_int(1) == Num(None)
        assert from_int(2) == Num(Num(None))
        assert from_int(3) == Num(Num(Num(None)))

    def test_add(self):
        # 0 + 0 = 0
        assert add(a=None, b=None) is None
        # 0 + 1 = 1
        assert add(a=Num(None), b=None) == Num(None)
        assert add(a=None, b=Num(None)) == Num(None)
        # 1 + 2 = 3
        assert add(a=Num(None), b=Num(Num(None))) == Num(Num(Num(None)))
        # 2 + 2 = 4
        assert add(a=Num(Num(None)), b=Num(Num(None))) == Num(Num(Num(Num(None))))

    def test_subtract(self):
        # smallest peano number is zero
        assert subtract(a=None, b=None) is None
        assert subtract(a=None, b=Num(None)) is None
        assert subtract(a=Num(None), b=Num(Num(None))) is None
        # 1 - 0 = 1
        assert subtract(a=Num(None), b=None) == Num(None)
        # 2 - 1 = 1
        assert subtract(a=Num(Num(None)), b=Num(None)) == Num(None)
        # 4 - 2 = 2
        assert subtract(a=Num(Num(Num(Num(None)))), b=Num(Num(None))) == Num(Num(None))

    def test_multiply(self):
        # smallest peano number is zero
        assert multiply(a=None, b=None) is None
        assert multiply(a=None, b=Num(None)) is None
        assert multiply(a=Num(None), b=None) is None
        assert multiply(a=Num(None), b=Num(None)) == Num(None)
        assert multiply(a=Num(Num(None)), b=Num(Num(None))) == Num(Num(Num(Num(None))))
        # 2 * 3 = 6
        assert multiply(a=Num(Num(None)), b=Num(Num(Num(None)))) == Num(
            Num(Num(Num(Num(Num(None)))))
        )
