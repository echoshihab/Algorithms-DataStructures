"""
Number of Connected Components in an Undirected Graph
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2

"""

import collections
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        if len(edges) == 0 or n ==1:
            return n
        
    
        adjecency_list = {i: [] for i in range(n)}

        for n1,n2 in edges:
            adjecency_list[n1].append(n2)
            adjecency_list[n2].append(n1)


        connections = [0]
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for n in adjecency_list[node]:
                dfs(n)



        for i in range(n):
            if i not in visited:
                dfs(i)
                connections[0] += 1

        
        return connections[0]



test = Solution()
print(test.countComponents(6, edges=[[0,1], [1,2], [2,3], [4,5]]))



class Solution2:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        if len(edges) == 0 or n == 1:
            return n
        
    
        adjecency_list = {i: [] for i in range(n)}

        for n1,n2 in edges:
            adjecency_list[n1].append(n2)
            adjecency_list[n2].append(n1)


        connections = [0]
        visited = set()
        queue = collections.deque()

        for i in range(n):
            if i not in visited:
                queue.append(i)
                while queue:
                    node = queue.popleft()
                    for an in adjecency_list[node]:
                        if an not in visited:
                            visited.add(an)
                            queue.append(an)
                connections[0] +=1            

        
        return connections[0]



test2 = Solution2()
print(test2.countComponents(6, edges=[[0,1], [1,2], [2,3], [4,5]]))
