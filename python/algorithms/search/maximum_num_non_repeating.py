from collections import Counter

class Solution:
  def largestUniqueNumber(self, A: List[int]) -> int:
    count = Counter(A)
    max_non_repeat = 0

    for num in A:
      if count[num] == 1:
        max_non_repeat = max(max_non_repeat, num)
      else:
        continue
    return max_non_repeat
    

