"""Median of Two Sorted Arrays
You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order.
 Return the median value among all elements of the two arrays.

Your solution must run in 
O(log(m+n)) time.

Example 1:

Input: nums1 = [1,2], nums2 = [3]

Output: 2.0
Explanation: Among [1, 2, 3] the median is 2.

Example 2:

Input: nums1 = [1,3], nums2 = [2,4]

Output: 2.5
Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
-10^6 <= nums1[i], nums2[i] <= 10^6"""

from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    shortList, largeList = nums1, nums2

    # swap if initial assignment is not correct
    if len(largeList) <  len(shortList):
        shortList, largeList = largeList, shortList


    totalElements = len(shortList) + len(largeList)
    half = totalElements // 2

    left, right = 0, len(shortList) - 1

    while True:
        i = (left + right) // 2 # shortlist index
        j = half - i - 2 # largelist index

        shortListLeft = shortList[i] if i >= 0 else float("-infinity")
        shortListRight = shortList[i + 1] if (i + 1) < len(shortList) else float("infinity")

        largeListLeft = largeList[j] if j >= 0 else float("-infinity")
        largeListRight = largeList[j+1] if (j + 1) < len(largeList) else float("infinity")

        if shortListLeft <= largeListRight and largeListLeft <= shortListRight:
            if totalElements % 2:
                return min(shortListRight, largeListRight)
            return (max(shortListLeft, largeListLeft) + min(shortListRight, largeListRight)) / 2
        elif shortListLeft > largeListRight:
            right = i - 1
        else:
            left = i + 1




print(findMedianSortedArrays([1,2], [3,4]))