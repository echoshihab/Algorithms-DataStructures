"""Given an array of integers nums which is sorted in ascending order, \
    and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""

#O(log n)
from typing import List


def search(nums: List[int], target: int) -> int:
    high =  len(nums) - 1
    low = 0

    while high >= low:
        mid = (low+high) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


print(search([-1,0,3,5,9,12], 9))
print(search([-1,0,3,5,9,12], 2))