class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            currSum = numbers[left] + numbers[right]
            
            if currSum > target:
                right -= 1
            elif currSum < target:
                left += 1
            else:
                return [left + 1, right + 1]


### 2nd Approach: Using Dict ###
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(numbers):
            complement = target - num
            
            if complement in seen:
                # If complement exists, return their indices incremented by one
                return [seen[complement] + 1, i + 1]
            
            # Add current index to the dictionary
            seen[num] = i
        
        # If no solution is found, return an empty list
        return []
