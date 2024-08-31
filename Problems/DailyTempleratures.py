"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] 
is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this 
is possible, keep answer[i] == 0 instead.


Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100"""


from typing import List

# brute force (O(n^2))
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    result = []
    for i in range(len(temperatures)):
        if(i == len(temperatures)-1):
            result.append(0)
            break
        current_temp = temperatures[i]
        for j in range(i+1, len(temperatures)):
            if temperatures[j] > current_temp:
                result.append(j-i)
                break
        if i != len(result)-1:
            result.append(0)

    return result



print(dailyTemperatures([30,60,90]))
print(dailyTemperatures([73,74,75,71,69,72,76,73]))

# O(n) space and time complexity
def dailyTemperatures2(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    stack = []

    for index, temperature in enumerate(temperatures):
        while stack and temperature > temperatures[stack[-1]]:
            stackIndex = stack.pop()
            result[stackIndex] = (index - stackIndex)
        stack.append(index)
    return result

print(dailyTemperatures2([30,60,90]))
print(dailyTemperatures2([73,74,75,71,69,72,76,73]))
