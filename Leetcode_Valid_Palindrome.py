class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        s = s.lower()
        s = ''.join(filter(str.isalnum, s))
        str_rev = s[::-1]
        if s == str_rev:
            return True
        else:
            return False


### 2nd Approach: 2 Pointers ###

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        s = ''.join(e.lower() for e in s if e.isalnum())

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
