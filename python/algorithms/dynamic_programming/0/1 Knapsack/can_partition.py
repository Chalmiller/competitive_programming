def can_partition(num):
  s = sum(num)

  if s%2 != 0:
    return False
  
  return can_partition_recursive(num, s/2, 0)

def can_partition_recursive(num, sum, current_index):
  if sum == 0:
    return True

  n = len(num)
  if n == 0 or current_index >= n:
    return False

  if num[current_index] <= sum:
    if(can_partition_recursive(num, sum - num[current_index], current_index + 1)):
      return True

  return can_partition_recursive(num, sum, current_index + 1)