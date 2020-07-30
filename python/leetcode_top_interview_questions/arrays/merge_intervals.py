from typing import *
import unittest

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Task: Merge a list of intervals
        Intuition: We can do this in one pass using a for_loop

        Algorithm:
            - Take the first value and decompose into a (start,end)
            - for each interval in list compare end with new_start
                - if end < new_start
                    - append (start, end) to response list
                - if end > new_start
                    if end < new_end
                        - end = new_end
                        - append (start, end) to response list
                    else
                        the current interval is consumed
        """
        if not intervals: return []
        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0]
        res = []

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



class TestMergeIntervals(unittest.TestCase):

    def test_interval_merge(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        response = [[1,6],[8,10],[15,18]]
        self.assertCountEqual(response, Solution().merge(intervals))

    def test_unsorted_interval_merge(self):
        intervals = [[1,4],[0,4]]
        response = [[0,4]]
        self.assertCountEqual(response, Solution().merge(intervals))
    
    def null_check(self):
        intervals = []
        response = []
        self.assertEqual(response, Solution().merge(intervals))
        

unittest.main(verbosity=2)