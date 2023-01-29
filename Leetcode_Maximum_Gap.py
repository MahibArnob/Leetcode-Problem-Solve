class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        result = 0

        for num in range(len(nums) - 1):
            if nums[num + 1] - nums[num] > result:
                result = nums[num + 1] - nums[num]

        return result
