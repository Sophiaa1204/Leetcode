class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = dict()

        for i in s:
            if i in counter.keys():
                counter[i] += 1
            else:
                counter[i] = 1
        
        for i in range(len(s)):
            if s[i] in counter.keys() and counter[s[i]] == 1:
                return i
        
        return -1