from mathematics import two_missing_numbers, ndiegame


class TestTwoMissingNumbers:
    def test_missing_numbers_at_the_ends(self):
        assert two_missing_numbers.solve(10, [9, 8, 7, 6, 4, 5, 3, 2]) == (1, 10)
        assert two_missing_numbers.solve(10, [8, 7, 6, 4, 5, 3, 2, 1]) == (9, 10)
        assert two_missing_numbers.solve(10, [8, 7, 6, 4, 5, 3, 9, 10]) == (1, 2)

    def test_missing_numbers_in_the_middle(self):
        assert two_missing_numbers.solve(4, [4, 1]) == (2, 3)
        assert two_missing_numbers.solve(10, [10, 9, 8, 7, 6, 5, 3, 1]) == (2, 4)
        assert two_missing_numbers.solve(10, [10, 7, 6, 4, 5, 3, 2, 1]) == (8, 9)


class TestNDieGame:
    def test_one_die(self):
        assert ndiegame.price(1) == 3.5

    def test_two_die(self):
        assert ndiegame.price(2) == 4.25

    def test_three_die(self):
        assert ndiegame.price(3) == 5.083333333333333

    def test_four_die(self):
        assert ndiegame.price(4) == 5.847222222222222

    def test_five_die(self):
        assert ndiegame.price(5) == 5.974537037037037

    def test_six_die(self):
        assert ndiegame.price(6) == 5.995756172839506

    def test_seven_die(self):
        assert ndiegame.price(7) == 5.999292695473251
