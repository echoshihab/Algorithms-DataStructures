"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
 #O(log(m * n)) time complexity.
from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    targetRow = []

    high = len(matrix) - 1
    low = 0

    while low <= high:
        middle = (low + high) // 2
        if matrix[middle][0] <= target and matrix[middle][-1] >= target:
            targetRow = matrix[middle]
            break
        elif matrix[middle][0] > target:
            high = middle - 1
        elif matrix[middle][-1] < target:
            low = middle + 1 

    if targetRow:
        l = 0
        r = len(targetRow) - 1
        while l <= r:
            mid = (l + r) // 2
            if  targetRow[mid] == target:
                return True
            elif targetRow[mid] > target:
                r = mid -1
            else:
                l = mid + 1

        return False
            
    else:
        return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
