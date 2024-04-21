class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for i in nums:
            if i in hashmap:
                return True
            hashmap.add(i)
        return False


### 2nd Approach ###
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(nums) != len(set(nums)) else False
