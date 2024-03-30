# Two Pointers
class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        vowel = ['a','e','i','o','u','A','O','E','I','U']
        temp_s = list(s)

        while (left < right):
            if s[left] not in vowel:
                left += 1
                continue
            if s[right] not in vowel:
                right -= 1
                continue
            temp_s[left],temp_s[right] = temp_s[right],temp_s[left]
            left += 1
            right -= 1
        
        return "".join(temp_s)