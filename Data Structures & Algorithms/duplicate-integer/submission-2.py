class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for x in nums:
            if d.get(x) is not None:
                return True
            d[x] = d.get(x, 0) + 1
        return False
         
        