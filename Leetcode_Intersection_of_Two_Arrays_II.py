class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [val for val in nums1 if val in nums2]
