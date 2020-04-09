def pair_with_targetsum(arr, target_sum):
  #  Two Pointer Approach

  # left, right = 0, len(arr) - 1
  # while(left < right):
  #   current_sum = arr[left] + arr[right]
  #   if current_sum == target_sum:
  #     return [left, right]

  #   if target_sum > current_sum:
  #     left += 1  # we need a pair with a bigger sum
  #   else:
  #     right -= 1  # we need a pair with a smaller sum
  # return [-1, -1]

  # Hash Table Approach (Dynamic Programming)
  num_hash = {}
  for num in arr:
    num_needed = target_sum - num
    if num_needed in num_hash:
      return [num, num_needed]
    else:
      num_hash.update(num)
  return [-1,-1]
