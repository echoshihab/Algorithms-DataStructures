"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 Constraints:

1 <= k <= points.length <= 104
-104 <= xi, yi <= 104
"""

import heapq
from typing import List


def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        result = []

        for x,y in points:
            distance = ((0-x)**2 + (0 - y)**2)**0.5
            heapq.heappush(min_heap, (distance, [x,y]))

        while  len(result) < k:
            result.append(heapq.heappop(min_heap)[1])
            
            
        return result
