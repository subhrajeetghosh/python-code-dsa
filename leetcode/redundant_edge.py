from collections import defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        def has_node(graph, src, dest, seen):
            if src == dest:
                return True
            seen.add(src)
            for next in graph[src]:
                if next not in seen and has_node(graph, next, dest, seen):
                    return True
            return False
        
        for edge in edges:
            if has_node(graph, edge[0], edge[1], set()):
                return edge
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return []