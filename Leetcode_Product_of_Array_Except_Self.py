class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums)) # [1, 1, 1, 1]
        # nums ... [1,2,3,4]
        prefix = 1
        postfix = 1
        # Inserting the prefix value to the result and multiplying it with the current number for the next iteration. ...[1,1,2,6]
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        # In reverse order multiply the postfix value to the result and store it in place of result, for next iteration multiplying it with current number ..[24,12,8,6]
        for j in range(len(nums) -1, -1, -1):
            result[j] *= postfix
            postfix *= nums[j]
        
        return result
