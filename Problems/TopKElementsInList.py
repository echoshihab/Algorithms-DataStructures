from collections import defaultdict
from typing import List

"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size."""

#brute force 
def topKFrequent(nums: List[int], k: int) -> List[int]:    
    test = defaultdict(int)

    for i in range(0, len(nums)):
        if test.get(nums[i]) is None:
            test[nums[i]] = 1
        else:
            test[nums[i]] += 1
        
    sorted_dict = sorted(test.items(), key=lambda x: x[1], reverse=True)
    
    solution_arr = []
    for i in range(0,k):
        solution_arr.append(sorted_dict[i][0])

    return solution_arr



print(topKFrequent([1], 1))


