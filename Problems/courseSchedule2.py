"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""

import collections
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prerequisites_map = {i: [] for i in range(numCourses)}
        prerequisites_count = [0] * numCourses

        for course, prerequisite in prerequisites:
            prerequisites_map[prerequisite].append(course)
            prerequisites_count[course] += 1

        can_finish = []

        queue = collections.deque([i for i in range(numCourses) if prerequisites_count[i] == 0])        
        
        while queue:
            course = queue.popleft()
            can_finish.append(course)

            for crs in prerequisites_map[course]:
                prerequisites_count[crs] -= 1

                if prerequisites_count[crs] == 0:
                    queue.append(crs)
        

        if len(can_finish) == numCourses:
            return can_finish
        return []
