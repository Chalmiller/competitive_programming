from typing import *
import functools
import operator

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    """
      1. create an empty response array
      2. iertate through nums 
      3. if first element, insert the product of the rest of the list
      4. if last element, insert the product of the beginning part of the list
      5. else, we will take the product of the list up until the curr num and after the curr num
          multiplying them together
      6. return the response list

      Note: this will be n^2 because of the continual multiplication operations on the split arrays
      space complexity will be n because of the creation of split arrays and the response array
    """
    response = []
    cache = {}
    # [1,2,3,4]
    # i = 3
    # curr_el = 3
    # curr_prod = 12
    for i in range(len(nums)):
      if i == 0:
        if nums[i] not in cache:
          cache[nums[i]] = functools.reduce(operator.mul, nums[i+1:])
        response.insert(i, cache[nums[i]]) 
      elif i == len(nums) - 1:
        if nums[i] not in cache:
          cache[nums[i]] = functools.reduce(operator.mul, nums[:i])
        response.insert(i, cache[nums[i]]) 
      else:
        if nums[i] not in cache:
          first_prod = functools.reduce(operator.mul, nums[:i])
          second_prod = functools.reduce(operator.mul, nums[i+1:])
          curr_prod = first_prod * second_prod
          cache[nums[i]] = curr_prod
        response.insert(i, cache[nums[i]]) 
    return response
