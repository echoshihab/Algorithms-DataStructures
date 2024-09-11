"""Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.


Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.

"""

#O(logn)

from typing import List


def findMin(nums: List[int]) -> int:
    length = len(nums)
    l, r  = 0, length - 1
    mid = length // 2
    min_value = 5001

    while l <= r:
        if nums[l] < nums[r]:
            min_value = min(min_value, nums[l])
            break

        mid = (l+r) // 2
        min_value = min(min_value, nums[mid])
        
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1

    return min_value

    
    
print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))


