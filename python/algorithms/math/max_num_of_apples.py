# 1196: How many apples can you put into the basket
from typing import *

class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        bag_sum = 0
        arr.sort()
        for index, apple in enumerate(arr):
            if bag_sum + apple > 5000:
                return index
            else:
                bag_sum += apple
        return len(arr)

obj = Solution()
num = obj.maxNumberOfApples([4999,1, 350,820,420,750,900, 560, 20])
print(num)
