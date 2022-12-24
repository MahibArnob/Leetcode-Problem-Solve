class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        output = 0
        num = len(s)
        i = num - 1

        while i >= 0:
            if i < num -1 and romanDict[s[i]] < romanDict[s[i+1]]:
                output = output - romanDict[s[i]]
            else:
                output = output + romanDict[s[i]]
            i -= 1

        return output
