from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
      count = 0
      result_list = []
      num_dict = defaultdict(list)
      for i in range(1, n+1):
        if len(str(i)) > 1:
          curr_sum = sum([int(num) for num in str(i)])
          num_dict[curr_sum].append(i)
        else:
          num_dict[i].append(i)
      print(num_dict)
      
      for key, val in num_dict.items():
        result_list.append(len(val))
      print(result_list)
      list_max = max(result_list)
      for el in result_list:
        if el == list_max:
          count += 1
      return count

obj = Solution()
print(obj.countLargestGroup(13))

