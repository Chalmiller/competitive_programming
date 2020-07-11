import typing

class Solution:
  def reverse(self, x: int) -> int:
      if x > 0:
        str_x = str(x)
        reversed_string = list(reversed(str_x))
        new_string = "".join(reversed_string)
        return reversed_string
      else:
        new_string = ""
        str_x = str(abs(x))
        reverse_string = list(reversed(str_x))
        new_string = "-" + "".join(reverse_string)
        return int(new_string)
