from codi.graphs.synonyms import *


class TestSynonyms:
    def test_given_empty_names_and_synonyms_then_return_empty_list(self):
        names = []
        synonyms = []
        assert merge(names, synonyms) == set()

    def test_given_empty_synonyms(self):
        names = [("John", 15)]
        synonyms = []
        assert merge(names, synonyms) == {Node("John", 15)}

    def test_given_all_names_belong_to_same_synonym_group(self):
        names = [("John", 15), ("Jon", 1)]
        synonyms = [("Jon", "John")]
        res = merge(names, synonyms)
        assert len(res) == 1
        assert Node("John", 16) in res or Node("Jon", 16) in res

    def test_given_example(self):
        names = [
            ("John", 15),
            ("Jon", 12),
            ("Chris", 13),
            ("Kris", 4),
            ("Christopher", 19),
        ]
        synonyms = [
            ("Jon", "John"),
            ("John", "Johnny"),
            ("Chris", "Kris"),
            ("Chris", "Christopher"),
        ]
        res = merge(names, synonyms)
        assert len(res) == 2
        assert Node("Jon", 27) in res or Node("John", 27) in res
        assert (
            Node("Christopher", 36) in res
            or Node("Chris", 36) in res
            or Node("Kris", 36) in res
        )

    def test_given_synonym_group_of_size_4(self):
        names = [
            ("John", 10),
            ("Jon", 3),
            ("Davis", 2),
            ("Kari", 3),
            ("Johnny", 11),
            ("Carlton", 8),
            ("Carleton", 2),
            ("Jonathan", 9),
            ("Carrie", 5),
        ]
        synonyms = [
            ("Jonathan", "John"),
            ("Jon", "Johnny"),
            ("Johnny", "John"),
            ("Kari", "Carrie"),
            ("Carleton", "Carlton"),
        ]
        res = merge(names, synonyms)
        assert len(res) == 4
        assert (
            Node("Jonathan", 33) in res
            or Node("John", 33) in res
            or Node("Jon", 33) in res
            or Node("Johnny", 33) in res
        )
        assert Node("Davis", 2) in res
        assert Node("Kari", 8) in res or Node("Carrie", 8) in res
        assert Node("Carlton", 10) in res or Node("Carleton", 10) in res
