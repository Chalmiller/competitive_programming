from itertools import dropwhile
class Solution:
    def reverse(self, x: int) -> int:
        if x==0: #dropwhile can't take anything if the condition is True for all elements
            return 0
        x=list(dropwhile(lambda i:i=="0",str(x)[::-1]))
        neg=""
        if "-" in x: #if the number is negative, we remove the "-" sign for now
            x.remove("-")
            neg="-"
        temp=''.join(x) #convert the list back to string
        if int(temp)>pow(2,31): #account for overflow
            return 0
        return neg+temp #if the number was negative, we return the "-" here

obj = Solution()
print(obj.reverse(1534236469))




