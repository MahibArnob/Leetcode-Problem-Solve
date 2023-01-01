class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countS[t[i]] = 1 + countS.get(t[i], 0)
        
        for j in countS:
            if countS[j] != countT.get(c, 0):
                return False
        
        return True
    
### Second Way ###

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # This code does the exact same thing as the above code. Counter is a build-in python Hashmap 
        # that count things automatically.
        return Counter(s) == Counter(t)
    
### Third Way ###

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # This program first sort the two given string, if they are anagram then they would be exactly
        # same string after sorting, and return True, otherwise it will return False
        return sorted(s) == sorted(t)
