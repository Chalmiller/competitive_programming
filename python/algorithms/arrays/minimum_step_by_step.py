class Solution:
     def minStartValue(self, nums: List[int]) -> int:
        return 1 - min(0, min(itertools.accumulate(nums)))