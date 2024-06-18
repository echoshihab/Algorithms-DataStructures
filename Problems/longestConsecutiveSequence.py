from collections import defaultdict
from typing import List



"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109"""




def longestConsecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    longest = 0

    for item in nums_set:
        if(item - 1  in nums_set):
            continue
        else:
            current_longest = 1
            val = item
            while val + 1 in nums_set:
                current_longest += 1
                val += 1
            if current_longest > longest:
                longest = current_longest
    return longest

longestConsecutive([0,3,7,2,5,8,4,6,0,1])
longestConsecutive([100,4,200,1,3,2])