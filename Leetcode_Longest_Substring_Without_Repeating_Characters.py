class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in hashmap:
                hashmap.remove(s[left])
                left += 1
            hashmap.add(s[right])
            result = max(result, (right - left + 1))
        return result
