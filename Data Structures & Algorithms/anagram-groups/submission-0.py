class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        freq_list = []
        for s in strs:
            isAnagram = False
            
            for i in range(len(ans)):
                x = freq_list[i].copy()
                if len(s) != x[-1]:
                    continue
                for ch in s:
                    x[ord(ch) - ord("a")] -= 1
                isPresent = True
                for j in range(26):
                    if x[j] != 0:
                        isPresent = False
                        break
                if isPresent == False:
                    continue
                isAnagram = True
                ans[i].append(s)
                break
            if isAnagram == False:
                ans.append([s])
                y = [0]*27
                for ch in s:
                    y[ord(ch)-ord('a')] +=1
                y[-1] = len(s)
                freq_list.append(y)
        return ans


        