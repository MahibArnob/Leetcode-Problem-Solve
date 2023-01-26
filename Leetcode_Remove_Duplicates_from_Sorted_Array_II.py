class Solution(object):
    def removeDuplicates(self, nums):
        # Initialize an integer k that updates the kth index of the array...
        # only when the current element does not match either of the two previous indexes. ...
        k = 0
        for i in nums:
            if k < 2 or i != nums[k - 2]:
                nums[k] = i
                k += 1
        return k   
