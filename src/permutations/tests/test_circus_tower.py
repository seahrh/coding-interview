from permutations.circus_tower import *


class TestCircusTower:
    def test_empty_array(self):
        assert tower_length([]) == 0

    def test_array_of_length_one(self):
        assert tower_length([Person(65, 193)]) == 1

    def test_array_of_length_two(self):
        assert tower_length([Person(65, 100), Person(70, 150)]) == 2

    def test_example_case_1(self):
        assert (
            tower_length(
                [
                    Person(65, 100),
                    Person(70, 150),
                    Person(56, 90),
                    Person(75, 190),
                    Person(60, 95),
                    Person(68, 110),
                ]
            )
            == 6
        )

    def test_example_case_2(self):
        assert (
            tower_length(
                [
                    Person(65, 100),
                    Person(70, 200),
                    Person(56, 90),
                    Person(75, 190),
                    Person(60, 95),
                    Person(68, 110),
                ]
            )
            == 5
        )

    def test_when_person_gets_lighter_and_taller_then_return_one(self):
        assert (
            tower_length(
                [
                    Person(65, 193),
                    Person(70, 191),
                    Person(56, 195),
                    Person(75, 190),
                    Person(60, 194),
                    Person(68, 192),
                ]
            )
            == 1
        )
