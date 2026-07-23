class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_index:
                return [nums_index[complement], i]

            nums_index[nums[i]] = i