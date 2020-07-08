"""
================================
Job Sequencing with Deadline
================================
Given an array of jobs where every job has a deadline and associated profit
if the job is finished before the deadline.
Given that every job takes single unit of time, so the minimum possible deadline for any job is 1.
What is the job sequence that maximises total profit if only one job can be scheduled at a time?

Examples:

Input: Four Jobs with following deadlines and profits
JobID  Deadline  Profit
  a      2        20
  b      1        10
  c      1        40
  d      1        30
Output: c, a


Input:  Five Jobs with following deadlines and profits
JobID   Deadline  Profit
  a       2        100
  b       1        19
  c       2        27
  d       1        25
  e       3        15
Output: c, a, e

SOLUTION: Greedy method
Time O(N^2)
Space O(N): store the Job objects

See
- https://www.geeksforgeeks.org/job-sequencing-problem/
- https://www.youtube.com/watch?v=zPtI8q9gvX8
"""
from typing import List, NamedTuple


class Job(NamedTuple):
    profit: int
    deadline: int
    id: str


def job_sequence(
    job_ids: List[str], profits: List[int], deadlines: List[int]
) -> List[str]:
    empty_slot = ""
    max_deadline: int = max(deadlines)
    res: List[str] = [empty_slot] * max_deadline
    free_slots: int = max_deadline
    jobs: List[Job] = []
    for i in range(len(job_ids)):
        jobs.append(Job(profit=profits[i], deadline=deadlines[i], id=job_ids[i]))
    jobs.sort(reverse=True)  # sort jobs by profit descending
    for job in jobs:
        if free_slots == 0:
            break
        for i in range(job.deadline - 1, -1, -1):
            if res[i] == empty_slot:
                res[i] = job.id
                free_slots -= 1
                break
    # remove free slots if there are any
    if free_slots != 0:
        res = [r for r in res if r != empty_slot]
    return res
