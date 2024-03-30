# DFS
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.path.append(0)
        self.traverse(graph,0)
        return self.res
        
    def traverse(self, graph, node):
        if node == len(graph) - 1:
            self.res.append(self.path[:])
            return
        
        for child in graph[node]:
            self.path.append(child)
            self.traverse(graph,child)
            self.path.pop()