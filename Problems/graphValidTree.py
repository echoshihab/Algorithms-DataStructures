"""
Graph Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adjacency_dict = {i: [] for i in range(n)}

        for n1,n2 in edges:
            adjacency_dict[n1].append(n2)
            adjacency_dict[n2].append(n1)
        
        visited = set()

        def dfs(prev, node):
            # loop detected
            if node in visited:
                return False

            visited.add(node)
            
            for adj in adjacency_dict[node]:
                if adj == prev:
                    continue
                if not dfs(node, adj):
                    return False
            return True

        return dfs(-1, 0) and len(visited) == n


            
        