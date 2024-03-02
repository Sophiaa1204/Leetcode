# Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for i in s:
            if i != '#':
                s_stack.append(i)
            else:
                if len(s_stack):
                    s_stack.pop()
        
        for i in t:
            if i != '#':
                t_stack.append(i)
            else:
                if len(t_stack):
                    t_stack.pop()
        
        return "".join(s_stack) == "".join(t_stack)