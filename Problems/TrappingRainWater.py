"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

"""
from typing import List


def trap(height: List[int]) -> int:
    water_collected = 0
    water_collected_confirmed = 0
    left_index = 0 
    peak = 0
    peak_set = False


    while left_index < len(height):
        print(height[left_index])
        if height[left_index] > peak and peak_set == False:
            peak = height[left_index]
            print("setting peak with ", height[left_index])
            peak_set = True
        elif height[left_index] >= peak and peak_set == True:
            print("reached second peak with ")
            water_collected_confirmed += water_collected
            water_collected = 0
            peak = height[left_index]
        elif height[left_index] < peak:
            water_collected += (peak - height[left_index])
        
        left_index += 1

    return water_collected_confirmed



print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))