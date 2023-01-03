class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))
        # nums ... [1,2,3,4]
        prefix = 1
        postfix = 1
        # inserting the prefix value to result and multiplying it with current number for next iteration. ...[1,1,2,6]
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        # In reverse order multiplying the postfix value to result and storing it in place of result, for next iteration multiplying it with current number ..[24,12,8,6]
        for j in range(len(nums) -1, -1, -1):
            result[j] *= postfix
            postfix *= nums[j]
        
        return result
