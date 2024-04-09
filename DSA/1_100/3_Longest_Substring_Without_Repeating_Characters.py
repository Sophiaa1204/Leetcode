# Non-fixed Sliding Window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = collections.defaultdict(int)
        repeat = 0
        res = 0
        # [left, right)
        left = 0
        right = 0

        while right < len(s):
            window[s[right]] += 1
            if window[s[right]] > 1:
                repeat += 1
            right += 1
            if repeat == 0:
                res = max(res, right-left)

            while repeat >= 1 and left < right:
                if window[s[left]] == 2:
                    repeat -= 1
                window[s[left]] -= 1
                left += 1
        
        return res