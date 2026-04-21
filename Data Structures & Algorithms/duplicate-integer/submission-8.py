class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_elements = set(nums)
        return len(unique_elements) < len(nums)