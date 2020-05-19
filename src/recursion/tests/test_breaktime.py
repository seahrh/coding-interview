from recursion.breaktime import *


class TestBreaktimeRecursive:
    def test_given_empty_bookings_then_return_zero(self):
        assert max_minutes_rec([]) == 0

    def test_given_one_booking_then_return_its_duration(self):
        assert max_minutes_rec([15]) == 15

    def test_given_two_bookings_then_return_the_booking_with_longer_duration(self):
        assert max_minutes_rec([30, 15]) == 30

    def test_given_example_1(self):
        assert max_minutes_rec([30, 15, 60, 75, 45, 15, 15, 45]) == 180

    def test_example_that_breaks_greedy_strategy(self):
        assert max_minutes_rec([45, 60, 45, 15]) == 90


class TestBreaktime:
    def test_given_empty_bookings_then_return_zero(self):
        assert max_minutes([]) == 0

    def test_given_one_booking_then_return_its_duration(self):
        assert max_minutes([15]) == 15

    def test_given_two_bookings_then_return_the_booking_with_longer_duration(self):
        assert max_minutes([30, 15]) == 30

    def test_given_example_1(self):
        assert max_minutes([30, 15, 60, 75, 45, 15, 15, 45]) == 180

    def test_example_that_breaks_greedy_strategy(self):
        assert max_minutes([45, 60, 45, 15]) == 90
