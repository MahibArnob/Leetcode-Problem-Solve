class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    output.append([a, nums[left], nums[right]])
                    # Updating left, checking if list contain 
                    # duplicate value, If so, then upadte again
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return output
