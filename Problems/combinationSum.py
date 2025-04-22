"""Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of 
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations 
are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is 
less than 150 combinations for the given input.

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""

from typing import List

## 2^t time complexity

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

    result = []
    current_arr = []

    def dfs(index : int, current = 0):
        if current > target or index >= len(candidates):
            return
        elif current == target:
            result.append(current_arr.copy())
            return
        
        current += candidates[index]
        current_arr.append(candidates[index])

        dfs(index, current)
        current -= current_arr.pop()
        dfs(index+1, current)
    
    dfs(0)
    return result
    

def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index, current, total):
            if total == target:
                result.append(current.copy())
                return
            elif total > target or index >= len(candidates):
                return

            current.append(candidates[index])
            dfs(index, current, total + candidates[index])
            current.pop()
            dfs(index + 1, current, total)
    
        dfs(0, [], 0)
        return result
