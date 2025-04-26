"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""


from typing import List


def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()

    result = []

    def dfs(index, current, total):

        if total == target:
            result.append(current.copy())
            return
        elif total > target or index == len(candidates):
            return
        


        current.append(candidates[index])
        dfs(index + 1, current, total+candidates[index])
        current.pop()

        while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
            i +=1

        dfs(index + 1, current, total)

    
    dfs(0, [], 0)
    return result

     
            

                



    
    dfs(0, 0, [])
