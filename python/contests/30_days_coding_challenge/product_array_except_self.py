import functools
import operator
from typing import *

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      # With Division

      # res = []
      # total_prod = curr_prod = functools.reduce(operator.mul, nums)
      # for num in nums:
      #   res.append(total_prod//num)

      # return res

      # # Non-division solution
      # res = []
      # for index, num in enumerate(nums):
      #   if not nums[:index]:
      #     curr_prod = functools.reduce(operator.mul, nums[index + 1:])
      #     res.append(curr_prod)
      #   elif not nums[index + 1:]:
      #     curr_prod = functools.reduce(operator.mul, nums[:index])
      #     res.append(curr_prod)
      #   else:
      #     curr_prod = functools.reduce(operator.mul, nums[:index]) * functools.reduce(operator.mul, nums[index + 1:])
      #     res.append(curr_prod)
      # return res

      p = 1
      n = len(nums)
      output = []
      for i in range(0,n):
          output.append(p)
          p = p * nums[i]
      p = 1
      for i in range(n-1,-1,-1):
          output[i] = output[i] * p
          p = p * nums[i]
      return output

obj = Solution()
prod_nums = obj.productExceptSelf([1,2,3,4])
print(prod_nums)