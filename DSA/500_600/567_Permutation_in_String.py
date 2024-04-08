# Sliding Window

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        need = {}

        for c in s1:
            if c in need.keys():
                need[c] += 1
            else:
                need[c] = 1
        
        # [left, right)
        left = 0
        right = 0
        matc = 0

        while right < len(s2):
            if s2[right] not in window.keys():
                window[s2[right]] = 1
            else:
                window[s2[right]] += 1
            
            if s2[right] in need.keys() and window[s2[right]] == need[s2[right]]:
                matc += 1
            
            right += 1
            
            while right - left >= len(s1):
                if matc == len(need):
                    # print(window)
                    # print(need)
                    return True
                if s2[left] in need.keys() and window[s2[left]] == need[s2[left]]:
                    matc -= 1
                if window[s2[left]] == 1:
                    del window[s2[left]]
                else:
                    window[s2[left]] -= 1
                left += 1
            
        return False