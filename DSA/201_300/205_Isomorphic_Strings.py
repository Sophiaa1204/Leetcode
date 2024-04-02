# Two Directional Mapping

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1 = dict()
        s2 = dict()

        for i in range(len(s)):
            if s[i] in s1.keys() and s1[s[i]] != t[i]:
                return False
            if t[i] in s2.keys() and s2[t[i]] != s[i]:
                return False
            
            s1[s[i]] = t[i]
            s2[t[i]] = s[i]
        
        return True