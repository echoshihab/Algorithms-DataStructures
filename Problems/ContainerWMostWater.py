"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

from typing import List

#brute force (O(n^2))
def maxArea(height: List[int]) -> int:
    max_area = 0
    left_index = 0
    right_index = len(height) - 1

    for i in range(len(height)):
        left_index = i
        right_index = len(height) - 1
        while left_index < right_index:
            contender_max = (right_index - left_index) * min(height[left_index], height[right_index])
            if contender_max > max_area:
                max_area = contender_max
            right_index -= 1

    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))

    
