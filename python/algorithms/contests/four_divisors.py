from typing import *

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        divisors = 0

        for i in nums:
            num_divisor = []
            for j in range(i+1):
                if len(num_divisor) > 4:
                    break
                if i%(j+1) == 0:
                    num_divisor.append(j+1)

            if len(num_divisor) == 4:
                sum_divisors = sum(num_divisor)
                divisors += sum_divisors

        return divisors

nums = [21,4,7]
obj = Solution()
obj.sumFourDivisors(nums)
