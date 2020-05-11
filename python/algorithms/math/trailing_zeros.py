from typing import *

def zeros(n):
    def return_num(num):
      # if num == 1:
      #   return num
      # return num * return_num(num - 1)
      factorial = 1
      for num in range(num, 0, -1):
        factorial *= num
      return factorial

    num_factorial = str(return_num(n))
    count = 0
    while num_factorial[-1] == '0':
      num_factorial = num_factorial[:-1]
      count += 1

    return count

print(zeros(1000))