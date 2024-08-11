"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

"""
from collections import defaultdict
from typing import List


def trap(height: List[int]) -> int:
    
    total_water_collected = 0

    if not height:
        return 0
    
    max_left, max_right = 0, 0
    max_left_arr = [max_left]
    max_right_arr = [max_right]

    for h in range(1, len(height)):
        if height[h - 1] >= max_left:
           max_left = height[h -1]
        max_left_arr.append(max_left)

    for h in range(len(height) -2, -1, -1):
        if height[h + 1] >= max_right:
            max_right = height[h + 1]
        max_right_arr.insert(0, max_right)


    
    for i in range(len(height)):
        water_collected = min(max_left_arr[i], max_right_arr[i]) - height[i]
        if water_collected < 0:
            water_collected = 0
        total_water_collected += water_collected

    return total_water_collected     




#o(n) runtime o(1) space 
def trap2(height: List[int]) -> int:
    if not height:
        return 0
    
    left_pointer, right_pointer = 0, len(height)-1
    left_max, right_max = height[left_pointer], height[right_pointer]
    water_collected = 0

    while left_pointer < right_pointer:
        if left_max < right_max:
            left_pointer += 1
            left_max = max(left_max, height[left_pointer])
            water_collected += left_max - height[left_pointer]
        else:
            right_pointer -=1 
            right_max = max(right_max, height[right_pointer])
            water_collected += right_max - height[right_pointer]

    return water_collected


print(trap2([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap2([4,2,0,3,2,5]))
print(trap2([4,2,3]))


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))
print(trap([4,2,3]))