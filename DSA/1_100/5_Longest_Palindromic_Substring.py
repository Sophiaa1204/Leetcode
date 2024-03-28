# Two pointers: outward
class Solution:
    def isPalindrome(self,s,i,j):
        left = i
        right = j

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return s[left+1:right]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            r1 = self.isPalindrome(s,i,i)
            r2 = self.isPalindrome(s,i,i+1)

            if len(r1) > len(res):
                res = r1
            if len(r2) > len(res):
                res = r2
        
        return res