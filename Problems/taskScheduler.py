"""
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100

"""
from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ##A. need total count of each letter
        ##B. need to ensure we tackle letters with highest frequency first
        ##C. need to keep track of number of cpu intervals
        ##D. need to prevent reuse of tasks while in gap

        
        ## A
        letterCount = Counter(tasks)
        ##B
        max_heap = [-cnt for cnt in letterCount.values()]
        heapq.heapify(max_heap)

        doubleQueue = deque() # for preventing reuse of letters while in gap


        ## C
        cpu_intervals = 0

        while max_heap or doubleQueue:
            cpu_intervals += 1

            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    doubleQueue.append([count, cpu_intervals + n])

            if doubleQueue and doubleQueue[0][1] == cpu_intervals:
                heapq.heappush(max_heap, doubleQueue.popleft()[0])

            
        
        return cpu_intervals

                

        
                