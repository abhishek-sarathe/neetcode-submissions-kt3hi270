class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        archive = {}

        for num in nums:
            if num not in archive:
                archive[num] = 0
            else:
                return True

        return False