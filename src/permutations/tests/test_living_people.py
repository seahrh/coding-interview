from sequences.living_people import *


class TestLivingPeople:
    def test_when_array_is_empty_then_return_none(self):
        assert year_with_most_people_alive([]) is None

    def test_given_one_person_only_when_yob_equals_yod_then_return_same_year(self):
        assert year_with_most_people_alive([Person(1900, 1900)]) == 1900

    def test_given_two_persons_only(self):
        assert (
            year_with_most_people_alive([Person(1900, 1910), Person(1910, 1911)])
            == 1910
        )
