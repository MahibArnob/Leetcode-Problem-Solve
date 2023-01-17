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
