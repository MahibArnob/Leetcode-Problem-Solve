class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """        
        if len(s) != len(t):
            return False
        sTot = {}
        tTos = {}
        
        for c , w in zip(s, t):
            if c in sTot and sTot[c] != w:
                return False
            if w in tTos and tTos[w] != c:
                return False
            sTot[c] = w
            tTos[w] = c
        return True