class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        ans = [0]*k
        sorted_freq = sorted(freq.items(), key=lambda item: item[1])
        for i in range(k):
            ans[i] = sorted_freq[len(sorted_freq)-1-i][0]
        return ans

        