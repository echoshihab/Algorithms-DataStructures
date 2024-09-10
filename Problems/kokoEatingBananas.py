"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 

If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109

"""


from typing import List

# O(log(max(n)) * n)
def minEatingSpeed(piles: List[int], h: int) -> int:
    piles_sum = sum(piles)

    l = (piles_sum // h) + (piles_sum %  h > 0)
    r = max(piles)
    result = r
    

    while l <= r:
        hour_taken = 0
        mid = (l+r) // 2 
        for item in piles:
            hour_taken += ((item // mid) + (item % mid > 0))
        if hour_taken <= h:
            result = mid
            r = mid - 1
        else:
            l = mid + 1
    
    return result

print(minEatingSpeed([3,6,7,11], 8))
print(minEatingSpeed([30,11,23,4,20], 5))

print(minEatingSpeed([312884470], 312884469))

