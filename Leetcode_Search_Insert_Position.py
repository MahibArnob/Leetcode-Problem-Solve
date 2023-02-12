class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        left, right = 0, len(nums) - 1

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        if nums[left] > target:
            return left
        else:
            return left + 1
