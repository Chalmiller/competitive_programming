# 1165: Single RowKeyboard
from typing import *

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        move_sum = 0
        for index, let in enumerate(word):
            if move_sum == 0:
                move_sum += keyboard.index(let)
            else:
                move_sum += abs(keyboard.index(let) - keyboard.index(word[index - 1]))
        return move_sum

obj = Solution()
num = obj.calculateTime("pqrstuvwxyzabcdefghijklmno", "leetcode")
print(num)