class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0]*26
        for i in range(len(s)):
            ch_s = ord(s[i]) - ord('a')
            ch_t = ord(t[i]) - ord('a')
            count[ch_s] += 1
            count[ch_t] -= 1
        for x in count:
            if x != 0:
                return False
        return True 
        