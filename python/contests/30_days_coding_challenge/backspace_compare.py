class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_array = []
        t_array = []

        for index in range(len(S)):
          if S[index] == "#" and s_array:
            s_array.pop()
            continue
          elif S[index] == "#" and not s_array:
            continue
          else:
            s_array.append(S[index])  
        
        for index in range(len(T)):
          if T[index] == "#" and t_array:
            t_array.pop()
            continue
          elif T[index] == "#" and not t_array:
            continue
          else:
            t_array.append(T[index]) 
        print(s_array, t_array)
        return s_array == t_array

obj = Solution()
truthy = obj.backspaceCompare("a##c", "#a#c")
print(truthy)
          