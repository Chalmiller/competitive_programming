# 1134: Armstrong Number

class Solution:
    def isArmstrong(self, N: int) -> bool:
        # Brute force
        str_num = str(N)
        len_num = len(str_num)
        num_sum = 0
        for i in range(len_num):
            num_sum += int(str_num[i]) ** len_num
        return num_sum == N