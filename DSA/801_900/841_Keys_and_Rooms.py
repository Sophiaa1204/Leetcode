# DFS
# Time Complexity: O(n+m) - n: rooms m:keys
# Space Complexity: O(n)

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(num):
            visited.add(num)
            for key in rooms[num]:
                if key not in visited:
                    dfs(key)

        visited = set()
        dfs(0)
        return len(visited) == len(rooms)