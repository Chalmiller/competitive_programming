from typing import *
import collections

class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        n=len(S)
        b=[False]*n
        for w in words:
            t=S.find(w)
            l=len(w)
            while t>-1:
                for i in range(t,t+l):
                    b[i]=True
                t=S.find(w,t+1)
        ans=''
        i=0
        while i<n:
            if b[i]:
                ans+=r'<b>'
                while i<n and b[i]:
                    ans+=S[i]
                    i+=1
                ans+=r'</b>'
            else:
                ans+=S[i]
                i+=1
        return ans
        
obj = Solution()
print(obj.boldWords(["ab", "bc"], "aabcd"))
