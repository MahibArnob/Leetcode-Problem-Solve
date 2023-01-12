### Approach Two - Using hashmap ###

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
            
        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans

### Approach Two - Using sort & two pointers ###

class Solution:
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()

    ans = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            ans.append(nums1[i])
            i += 1
            j += 1
    return ans
