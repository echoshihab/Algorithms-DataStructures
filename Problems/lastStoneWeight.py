"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
 
"""

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for item in stones:
            heapq.heappush(max_heap, -item)

        while len(max_heap) > 1:
            x = -(heapq.heappop(max_heap))
            y = -(heapq.heappop(max_heap))

            if x == y:
                continue
        
            heapq.heappush(max_heap, -(x-y))

        return -max_heap[0] if len(max_heap) else 0

