# Fixed Length - Sliding Window

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = 0
        curr_cnt = 0
        res = 0
        # [left, right)
        left = 0
        right = 0

        while right < len(arr):
            curr_sum += arr[right]
            curr_cnt += 1
            right += 1
            if curr_cnt == k and curr_sum / k >= threshold:
                res += 1
            
            while curr_cnt >= k and left < right:
                curr_sum -= arr[left]
                curr_cnt -= 1
                left += 1
        
        return res