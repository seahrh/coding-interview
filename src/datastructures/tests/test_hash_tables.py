from datastructures.hash_tables import *


class TestStringHash:
    def test_hash(self):
        capacity = 10
        assert string_hash("a", capacity) == 7
        assert string_hash("b", capacity) == 8
        assert string_hash("c", capacity) == 9
        assert string_hash("d", capacity) == 0
        assert string_hash("e", capacity) == 1

    def test_hash_value_should_be_unique_for_anagrams(self):
        capacity = 10
        assert string_hash("ab", capacity) != string_hash("ba", capacity)
        assert string_hash("aabbcc", capacity) != string_hash("cbaacb", capacity)

    def test_hash_value_is_consistent_when_capacity_is_fixed(self):
        capacity = 10
        assert string_hash("a", capacity) == string_hash("a", capacity)


class TestMyHashTable:
    def test_overwrite_key(self):
        table = MyHashTable[str, str](capacity=10)
        table.put("a", "a1")
        table.put("b", "b1")
        table.put("c", "c1")
        assert table.get("a") == "a1"
        assert table.get("b") == "b1"
        assert table.get("c") == "c1"
        table.put("a", "a2")
        assert table.get("a") == "a2"
        assert table.get("b") == "b1"
        assert table.get("c") == "c1"

    def test_collision(self):
        table = MyHashTable[str, str](capacity=1)
        table.put("a", "a1")
        table.put("b", "b1")
        table.put("c", "c1")
        assert table.get("a") == "a1"
        assert table.get("b") == "b1"
        assert table.get("c") == "c1"
