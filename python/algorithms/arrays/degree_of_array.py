from typing import *
from collections import Counter
import math

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        num_count = dict()
        max_degree = -math.inf
        index_list = []

        min_length = math.inf

        for num in nums:
          num_count[num] = num_count.get(num, 0) + 1
        
        sorted_dict = sorted(num_count.items(), key=lambda x: x[1], reverse= True)
        max_degree = sorted_dict[0][1]
        max_els = [num for num, count in sorted_dict if count == max_degree]
        
        for el in max_els:
          el_list = []
          for i in range(len(nums)):
            if nums[i] == el:
              el_list.append(i)
          index_list.append(el_list)
        print(index_list)
        for indeces in index_list:
          min_length = min(min_length, len(nums[indeces[0]:indeces[-1]+1]))
        return min_length


obj = Solution()
print(obj.findShortestSubArray([1,2,2,3,1,4,2]))