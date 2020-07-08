from greedy.job_sequencing import *


class TestJobSequencing:
    def test_2_jobs_or_less(self):
        assert job_sequence(job_ids=["a"], profits=[1], deadlines=[1]) == ["a"]
        assert job_sequence(job_ids=["a"], profits=[1], deadlines=[2]) == ["a"]
        assert job_sequence(job_ids=["a", "b"], profits=[2, 1], deadlines=[1, 1]) == [
            "a"
        ]
        assert job_sequence(job_ids=["a", "b"], profits=[2, 1], deadlines=[1, 2]) == [
            "a",
            "b",
        ]
        assert job_sequence(job_ids=["a", "b"], profits=[2, 1], deadlines=[2, 1]) == [
            "b",
            "a",
        ]
        assert job_sequence(job_ids=["a", "b"], profits=[2, 1], deadlines=[2, 3]) == [
            "a",
            "b",
        ]

    def test_case_1(self):
        assert job_sequence(
            job_ids=["2", "1", "4", "3", "5"],
            profits=[100, 60, 40, 20, 20],
            deadlines=[1, 2, 2, 3, 1],
        ) == ["2", "1", "3"]

    def test_case_2(self):
        assert job_sequence(
            job_ids=["1", "2", "3", "4", "5"],
            profits=[20, 15, 10, 5, 1],
            deadlines=[2, 2, 1, 3, 3],
        ) == ["2", "1", "4"]

    def test_case_3(self):
        assert job_sequence(
            job_ids=["1", "2", "3", "4", "5", "6", "7"],
            profits=[35, 30, 25, 20, 15, 12, 5],
            deadlines=[3, 4, 4, 2, 3, 1, 2],
        ) == ["4", "3", "1", "2"]

    def test_case_4(self):
        assert job_sequence(
            job_ids=["a", "b", "c", "d"],
            profits=[20, 10, 40, 30],
            deadlines=[2, 1, 1, 1],
        ) == ["c", "a"]

    def test_case_5(self):
        assert job_sequence(
            job_ids=["a", "b", "c", "d", "e"],
            profits=[100, 19, 27, 25, 15],
            deadlines=[2, 1, 2, 1, 3],
        ) == ["c", "a", "e"]
