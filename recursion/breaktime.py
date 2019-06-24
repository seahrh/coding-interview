"""
The Masseuse: A popular masseuse receives a sequence of back-to-back appointment requests
and is debating which ones to accept. She needs a 15-minute break between appointments and
therefore she cannot accept any adjacent requests. Given a sequence of back-to-back appointment
requests (all multiples of 15 minutes, none overlap, and none can be moved), find the optimal
(highest total booked minutes) set the masseuse can honor. Return the number of minutes.
EXAMPLE
Input: {30, 15, 60, 75, 45, 15, 15, 45}
Output: 180 minutes ({30, 60, 45, 45}).

(17.16, p585)
SOLUTION
The greedy strategy (i.e. picking longest appointment first) may not be optimal.
e.g. given [45, 60, 45, 15], optimal set does not include 60.

1. Recursion with memoization
Problem as a sequence of choices as we walk down the list of appointments:
Do we use this appointment or do we not?
If we use appointment i, we must skip appointment i + 1 as we can't take back-to-back appointments.
Appointment i + 2 is a possibility (but not necessarily the best choice).
Memo table is an array that maps index of bookings to max-minutes.
O(N) time: call stack is a lopsided tree, branching all the way down to the left. Hence linear.
O(N) space: memo table, depth of call stack
"""


def _max_minutes_rec(bookings, index, memo):
    if index >= len(bookings):  # base case
        return 0
    if memo[index] == 0:
        best_with = bookings[index] + _max_minutes_rec(bookings, index + 2, memo)
        best_without = _max_minutes_rec(bookings, index + 1, memo)
        memo[index] = max(best_with, best_without)
    return memo[index]


def max_minutes_rec(bookings):
    memo = [0] * len(bookings)
    return _max_minutes_rec(bookings, 0, memo)
