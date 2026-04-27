class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            d1[s[i]] = d1.get(s[i], 0) + 1
            d2[t[i]] = d2.get(t[i], 0) + 1
        if len(d1) != len(d2):
            return False
        for key in d1.keys():
            if key not in d2:
                return False
            elif d1[key] != d2[key]:
                return False
        return True
        