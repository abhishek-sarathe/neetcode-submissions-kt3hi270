class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            d = {}
            for i in range(len(nums)):
                
                complement = target - nums[i]
                complement_key = d.get(complement)
                if complement_key is not None:
                    return [complement_key, i]
                d[nums[i]] = i
        
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return 0
        