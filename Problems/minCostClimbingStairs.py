"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.


Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        zero = cost[0]
        one = cost[1]
        
        for i in range(2, len(cost)):
            temp = one
            one = min((cost[i] + zero), (cost[i] + one))
            zero = temp
        
        return min(one, zero)
