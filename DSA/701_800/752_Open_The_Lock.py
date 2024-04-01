# BFS
class Solution:
    def plusOne(self,s,j):
        ch = list(s)
        if ch[j] == '9':
            ch[j] = '0'
        else:
            ch[j] = str(int(ch[j]) + 1)
        return ''.join(ch)

    def minusOne(self,s,j):
        ch = list(s)
        if ch[j] == '0':
            ch[j] = '9'
        else:
            ch[j] = str(int(ch[j]) - 1)
        return ''.join(ch)

    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        q1,q2 = set(),set()
        visited = set()

        q1.add('0000')
        q2.add(target)
        step = 0

        while q1 and q2:
            temp = set()
            for curr in q1:
                if curr in dead:
                    continue
                if curr in q2:
                    return step

                visited.add(curr)
                
                for i in range(4):
                    plusOne = self.plusOne(curr,i)
                    minusOne = self.minusOne(curr,i)

                    if plusOne not in visited: 
                        temp.add(plusOne)
                    if minusOne not in visited: 
                        temp.add(minusOne)
            
            step += 1
            q1,q2 = q2, temp
        
        return -1