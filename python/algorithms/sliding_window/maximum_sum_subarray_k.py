def max_sub_array_of_size_k(k, arr):
  # Brute Force
  # max_sum = 0
  # window_sum = 0

  # for i in range(len(arr) - k + 1):
  #   window_sum = 0
  #   for j in range(i, i+k):
  #     window_sum += arr[j]
  #   max_sum = max(max_sum, window_sum)
  # return max_sum
  
  # Sliding Window Technique
  result = []
  window_start = 0
  window_sum = 0
  window_max = 0

  for window_end in range(len(arr)):
    window_sum += arr[window_end]
    if window_end >= k - 1:
      if window_sum > window_max:
        window_max = window_sum
        result = sum(list(arr[window_start: k + window_start]))
      window_sum -= arr[window_start]
      window_start += 1
  return result

num = max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])
print(num)