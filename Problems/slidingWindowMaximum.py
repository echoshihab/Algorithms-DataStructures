"""Sliding Window Maximum
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.
"""

from collections import deque
from typing import List

#O(n)
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    result = []

    queue = deque()
    l = r = 0

    while r < len(nums):
        while queue and nums[queue[-1]] < nums[r]:
            queue.pop()
        queue.append(r)

        if l > queue[0]:
            queue.popleft()
        
        if (r + 1) >= k:
            result.append(nums[queue[0]])
            l +=1
        
        r += 1

    return result


        
        


