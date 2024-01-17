from codi.datastructures.non_repeating_character import *


class TestNonRepeatingCharacter:
    def test_first_non_repeating_character(self):
        assert first_non_repeating_character("") == -1
        assert first_non_repeating_character("a") == 0
        assert first_non_repeating_character("abccb") == 0
        assert first_non_repeating_character("bccba") == 4
        assert first_non_repeating_character("geeksforgeeks") == 5
        assert first_non_repeating_character("abccba") == -1
