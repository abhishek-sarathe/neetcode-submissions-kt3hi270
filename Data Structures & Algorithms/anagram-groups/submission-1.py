class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        freq_list = [] # Stores character counts for each group
        
        for s in strs:
            s_freq = [0] * 26
            for char in s:
                s_freq[ord(char) - ord('a')] += 1
            
            found = False
            for i in range(len(freq_list)):
                if s_freq == freq_list[i]: # Python can compare lists directly
                    ans[i].append(s)
                    found = True
                    break
            
            if not found:
                ans.append([s])
                freq_list.append(s_freq)
        return ans


        