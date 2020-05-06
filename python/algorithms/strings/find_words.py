class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top, middle, bottom = [q,w,e,r,t,y,u,i,o,p], [a,s,d,f,g,h,j,k,l], [z,x,c,v,b,n,m]
        result = []

        for word in words:
          high, mid, low = 0, 0, 0
          for let in word:
            let = let.tolower()
            if let in top:
              high += 1
            elif let in middle:
              mid += 1
            else:
              low += 1
          if high == len(word) or mid == len(word) or low == len(word):
            result.append(word)
        return result


