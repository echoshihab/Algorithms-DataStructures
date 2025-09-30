"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, 
with one additional edge added. The added edge has two different vertices chosen from 1 to n, 
and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] 
indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
If there are multiple answers, return the answer that occurs last in the input.

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = list(range(len(edges) + 1))
        print(root)

        def find_root(node):
            if root[node] != node:
                root[node] = find_root(root[node]) 
            return root[node] 
        for node1, node2 in edges: 
            root1, root2 = find_root(node1), find_root(node2)

            if root1 == root2:
                return [node1, node2] 
 
            root[root2] = root1 
    

    

test = Solution()
test.findRedundantConnection([[1,2],[1,3],[2,3]])


class Solution2:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjacency_map = {i:[] for i in range(len(edges) + 1)}

        def cycle_exists(edge1,edge2):
            if edge1 == edge2:
                return True

            visited.add(edge1)

            for n in adjacency_map[edge1]:
                if n not in visited:
                    if cycle_exists(n, edge2):
                        return True
        
            return False
        

        for e1,e2 in edges:
            visited = set()
            
            if cycle_exists(e1,e2):
                return [e1,e2]
            else:
                adjacency_map[e1].append(e2)
                adjacency_map[e2].append(e1)


