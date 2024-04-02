# Enumeration
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0

        for a in range(1,n+1):
            for b in range(1,n+1):
                c = int(sqrt(a*a + b*b + 1))
                if c <= n and (a * a + b * b) == c * c:
                    count += 1
        
        return count