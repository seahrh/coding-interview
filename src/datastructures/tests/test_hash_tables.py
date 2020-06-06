from datastructures.hash_tables import *


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
