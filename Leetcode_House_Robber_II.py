# Solution1
'
class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1, rob2 = 0, 0
        def helper(rob1, rob2, x, y):
            for n in range(x, len(nums) - y):
                temp = max(nums[n] + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(nums[0], helper(0, 0, 0, 1), helper(0, 0, 1, 0))
        
 # Solution2
 
 class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
