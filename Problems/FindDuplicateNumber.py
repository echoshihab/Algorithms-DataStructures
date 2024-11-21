"""Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

Constraints:

1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

"""

from typing import List

# O(n) time and space complexity
def findDuplicate(self, nums: List[int]) -> int:
    hash_map = {}

    for item in nums:
        val = hash_map.get(item, 0)
        if val > 0:
            return item
        else:
            hash_map[item] = val + 1

#O(n) time and O(1) space complexity
def findDuplicate2(self, nums: List[int]) -> int:
    slow, fast = 0, 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow2 = 0

    while True:
        slow = nums[slow]
        slow2 = nums[slow2]

        if slow == slow2:
            return slow