from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Task: find the least amount of meeting times between all pairs

        1. make the first meeting time the start and end
        2. iterate through the rest of the meetings and try to merge
        3. if the times merge, compare the end times and take the max
        4. else if the times don't merge, append the current pair to the response
        5. append the last meeting to the response

        Edge Case:
          - the list is empty
          - the list only has one meeting
          - the meetings all overlap into one
          - no meetings overlap

        Time Complexity:
          - O(n) - time complexity
          - O(1) - space complexity
        """
        # [[1,3],[2,6],[8,10],[15,18]]
        start, end = intervals[0][0], intervals[0][1]
        response = []

        for i in range(1, len(intervals)):
          curr_start, curr_end = intervals[i][0], intervals[i][1]
          if end >= curr_start:
            end = max(end, curr_end)
          else:
            response.append([start, end])
            start = curr_start
            end = curr_end
        response.append([start, end])


