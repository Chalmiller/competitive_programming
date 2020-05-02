import math

def find_first_missing_positive(nums):
  i = 0

  while i < len(nums):
    j = nums[i] - 1
    if nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[j]:
      print(nums)
      print(nums[i], nums[j])
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  print(nums)
  
  for i in range(len(nums)):
    if nums[i] != i + 1:
      return i + 1


print(find_first_missing_positive([-3, 1, 5, 4, 2]))
