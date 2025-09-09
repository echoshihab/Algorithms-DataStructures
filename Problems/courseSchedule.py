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

import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prerequisite_map = {i : [] for i in range(numCourses)}

        # what are the prerequisites for each course
        # course: [prerequisite1, prerequisite2 ...]
        for course, prerequisite in prerequisites:
            prerequisite_map[course].append(prerequisite)

        visited = set()

        def dfs(course):
            # one of the prereqs have a circular dependency with a course earlier in the chain
            if course in visited:
                return False
            # if this course has no preqrequisite then this current course path can be finished
            if prerequisite_map[course] == []:
                return True
            
            visited.add(course)

            for prerequisite in prerequisite_map[course]:
                if not dfs(prerequisite):
                    return False
            
            visited.remove(course)
            
            # we know that this path can be completed so remove list of prereqs since we already traversed them
            prerequisite_map[course] = []

            return True
        
    
        for course in range(numCourses):
            if not dfs(course): return False
        return True    
        

            

class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prerequisite_map = {i : [] for i in range(numCourses)}


        crs_prereq_count = [0] * numCourses

        # { prerequisite: [course1, course2....]}
        for course, prerequisite in prerequisites:
            prerequisite_map[prerequisite].append(course)
            crs_prereq_count[course] += 1

        # add all courses with 0 prerequisites to queue
        queue = collections.deque([i for i in range(numCourses) if crs_prereq_count[i] == 0])

        can_finish = 0

        while queue:
            course = queue.popleft()
            can_finish +=1

            # loop through courses that have this course as preqrequisite and reduce the prereq count for those
            for crs in prerequisite_map[course]:
                crs_prereq_count[crs] -= 1
                if crs_prereq_count[crs] == 0:
                    queue.append(crs)

        if can_finish == numCourses:
            return True
        return False
            

        





        
