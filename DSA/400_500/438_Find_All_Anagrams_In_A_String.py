# Fixed Length Sliding Window
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = collections.defaultdict(int)
        need = collections.defaultdict(int)
        total_need = 0
        matc = 0
        res = []

        for c in p:
            if need[c] == 0:
                total_need += 1
            need[c] += 1
        
        # [left,right)
        left = 0
        right = 0

        while right < len(s):
            window[s[right]] += 1
            if window[s[right]] == need[s[right]]:
                matc += 1
            right += 1
            while right - left == len(p):
                if matc == total_need:
                    res.append(left)
                if window[s[left]] == need[s[left]]:
                    matc -= 1
                window[s[left]] -= 1
                left += 1
        
        return res