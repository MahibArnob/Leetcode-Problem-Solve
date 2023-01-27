class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        start = {}
        end = {}
        result = []

        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
                start[nums[i]] = i
                end[nums[i]] = i
            else:
                count[nums[i]] += 1
                end[nums[i]] = i

        maxValue = max(count.values())

        for key, val in count.items():
            if val == maxValue:
                result.append(end[key] - start[key] + 1)
        
        return min(result)
            
