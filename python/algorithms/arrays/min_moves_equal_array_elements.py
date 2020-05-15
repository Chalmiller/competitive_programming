from typing import *

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # move = len(nums) - 1
        # are_equal = all([elem == nums[0] for elem in nums])
        # count = 0
        
        # while not are_equal:
        #   sorted_nums = sorted(nums)
        #   min_els = [sorted_nums[i] for i in range(move)]
        #   for el in min_els:
        #     el_index = nums.index(el)
        #     nums[el_index] += 1
        #   count += 1
        #   are_equal = all([elem == nums[0] for elem in nums])
        # return count

        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
          diff = (moves + nums[i]) - nums[i - 1]
          print(diff)
          nums[i] += moves
          moves += diff
        return moves

obj = Solution()
print(obj.minMoves([1,2,3]))