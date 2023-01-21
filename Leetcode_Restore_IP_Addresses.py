class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        if len(s) < 4 or len(s) > 12:
            return result

        def backTrack(i, dots, currIP):
            if dots == 4 and i == len(s):
                result.append(currIP[:-1])
                return
            if dots > 4:
                return

            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    backTrack(j + 1, dots + 1, currIP + s[i:j+1] + ".")
        
        backTrack(0, 0, "")
        return result
