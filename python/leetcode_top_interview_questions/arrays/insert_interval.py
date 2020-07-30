from typing import *
import unittest

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Task: Given an existing list of intervals, insert the new interval where appropriate
                and merge if needed.
        Intuition: I think if I modularize the merge intervals problem I can use it functionally

        Algorithm:
            - modularize merge_interval as a function
            - iterate through the intervals
                - if the new interval start time is less than the curr_start time from the iteration, we
                    have found our insertion point
                - insert and run merge_interval
            return merged_intrervals
        """
        def merge_intervals(intervals):
            res = []
            start, end = intervals[0]

            for i in range(1, len(intervals)):
                new_start, new_end = intervals[i]

                if end < new_start:
                    res.append([start, end])
                    start, end = new_start, new_end
                else:
                    if end < new_end:
                        end = new_end
                    else:
                        continue

            res.append([start,end])
            return res

        if not intervals: return [newInterval]
        start = newInterval[0]

        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i]
            if curr_start > start:
                intervals.insert(i, newInterval)
            elif i == len(intervals) - 1:
                intervals.append(newInterval)

        merged_intervals = merge_intervals(intervals)
        return merged_intervals
            

class TestInsertInterval(unittest.TestCase):

    def test_insert_interval(self):
        intervals = [[1,3],[6,9]]
        new_interval = [2,5]
        response = [[1,5],[6,9]]
        self.assertEqual(response, Solution().insert(intervals, new_interval))

unittest.main(verbosity=2)