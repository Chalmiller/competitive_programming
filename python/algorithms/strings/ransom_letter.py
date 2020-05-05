class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_inv = dict()
        
        for let in magazine:
            if let not in mag_inv:
                mag_inv[let] = 0
            mag_inv[let] += 1
        
        print(mag_inv)
        while ransomNote:
            let = ransomNote[0]
            if let in mag_inv and mag_inv[let] > 0:
                mag_inv[let] -= 1
                ransomNote = ransomNote[1:]
            else:
                return False
        return True

obj = Solution()
print(obj.canConstruct("aa", "aab"))