"""There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination."""


from typing import List



def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    result_dict = {}
    stack = []
    for i in range(len(position)):
        result_dict[position[i]] = speed[i]
    
    position.sort(reverse=True)


    for item in position:
        step_target = target-item
        steps_required = step_target / result_dict[item] 

        if stack: 
            if steps_required > stack[-1]:
                stack.append(steps_required)
        else:
            stack.append(steps_required)


    return len(stack)



print(carFleet(10, [1,4], [3,2]))
print(carFleet(10, [4,1,0,7],  [2,2,1,1]))
print(carFleet(10, [0,4,2], [2,1,3]))



