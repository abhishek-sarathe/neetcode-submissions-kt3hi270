class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            if d.get(nums[i]) is not None:
                return True
            d[nums[i]] = d.get(nums[i], 0) + 1
        return False
         
        