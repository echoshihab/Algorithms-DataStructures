"""You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.


Constraints:

1 <= heights.length <= 1000.
0 <= heights[i] <= 1000

"""

# O(n) space and time

from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    maxArea = 0
    stack = [] # to hold index and height of the bar

    for i in range(len(heights)):
        start = i
        while stack and stack[-1][1] > heights[i]:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, heights[i]))

    
    for index, height in stack:
        maxArea = max(maxArea, height * (len(heights) - index))
    
    return maxArea



        




print(largestRectangleArea([1,3,7]))
print(largestRectangleArea([7,1,7,2,2,4]))


        