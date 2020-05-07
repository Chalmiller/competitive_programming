class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      result = []

      for el in nums1:
        el_index = nums2.index(el)
        if el_index == len(nums2) - 1:
          result.append(-1)
        else:
          for next_el in range(el_index+1, len(nums2)):
            if nums2[next_el] > el:
              result.append(nums2[next_el])
              break
            elif next_el == len(nums2) - 1:
              result.append(-1)
      return result
