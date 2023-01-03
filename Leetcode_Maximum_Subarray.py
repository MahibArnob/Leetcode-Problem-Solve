class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArr = nums[0]
        currSum = 0

        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i
            maxSubArr = max(maxSubArr, currSum)
            
        return maxSubArr
