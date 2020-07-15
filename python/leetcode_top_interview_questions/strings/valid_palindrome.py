import typing 

class Solution:
  def isPalindrome(self, s: str) -> bool:
    if not s:
      return True
    
    munge_data = list(filter(lambda x: x.isalnum(), s))

    ptr_1 = 0
    ptr_2 = len(munge_data) - 1
    # two pointer approach
    while ptr_1 < ptr_2:
      if munge_data[ptr_1].lower() != munge_data[ptr_2].lower():
        return False
      ptr_1 += 1
      ptr_2 += 1
    return True

        