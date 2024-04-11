class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 0:
            return False
        
        visited = set()
        visited.add(n)

        while True:
            total = 0
            n = str(n)

            for i in range(len(n)):
                total += int(n[i])**2
            
            if total == 1:
                return True
            
            if total in visited:
                return False
            else:
                visited.add(total)
            
            n = total