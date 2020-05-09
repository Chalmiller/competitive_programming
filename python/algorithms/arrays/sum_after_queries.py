class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
      result = []
      even_nums = sum(list(filter(lambda x: x %2 == 0, A)))
      for num, index in queries:
        A[index] += num
        if A[index] % 2 == 0:
          even_nums += A[index]
        result.append(even_nums)
      return result
