class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        beingTrusted = defaultdict(int)
        trusting = defaultdict(int)

        for a, b in trust:
            trusting[a] += 1
            beingTrusted[b] += 1
        
        for i in range(1, n+1):
            if beingTrusted[i] == n - 1 and trusting[i] == 0:
                return i
        
        return -1
