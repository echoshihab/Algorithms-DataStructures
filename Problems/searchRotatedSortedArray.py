"""There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

"""
from typing import List

# O(log n) + O(log (subset of n))  equivalent to O(logn)
def search(nums: List[int], target: int) -> int:
    r = len(nums) - 1
    l = 0
    min_number = nums[0]
    min_number_index = 0

    # find the pivot point first (binary search)
    while l <= r:
        if nums[l] < nums[r]:
            if nums[l] < min_number:
                min_number = nums[l]
                min_number_index = l
            break
        
        mid = (l + r) // 2
        if nums[mid] < min_number:
            min_number = nums[mid]
            min_number_index = mid

        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1
            
    # check which side of pivot the target is on
    if target > nums[min_number_index]:
        if target > nums[len(nums) -1]:
            l = 0
            r = min_number_index - 1
        else:
            l = min_number_index
            r = len(nums) - 1
    elif target == nums[min_number_index]:
        return min_number_index
    else: 
        return -1
    
    # binary search again to find target
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    
    return -1




    
print(search([5,1,3], 3))


