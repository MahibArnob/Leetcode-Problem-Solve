class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1
        index = -1
        while begin <= end:
            mid = (begin + end) / 2
            if target == nums[mid]:
                index = mid
                break
            elif target > nums[mid]: begin = mid + 1
            elif target < nums[mid]: end = mid - 1
        return index
