from typing import *

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
      intervals.sort(key=lambda x: x[0])
      print(intervals)
      for index in range(len(intervals) - 1):
        if intervals[index][1] > intervals[index+1][0]:
          return False
      return True

obj = Solution()
print(obj.canAttendMeetings([[0,30],[5,10],[15,20]]))
