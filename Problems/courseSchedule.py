"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites 
where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prerequisite_map = {i : [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            prerequisite_map[course].append(prerequisite)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if prerequisite_map[course] == []:
                return True
            
            visited.add(course)

            for prerequisite in prerequisite_map[course]:
                if not dfs(prerequisite):
                    return False
            
            visited.remove(course)
            prerequisite_map[course] = []

            return True
        
    
        for course in range(numCourses):
            if not dfs(course): return False
        return True    
        

            





        
