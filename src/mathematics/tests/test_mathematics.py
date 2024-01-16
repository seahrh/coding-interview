from mathematics import ndiegame


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
