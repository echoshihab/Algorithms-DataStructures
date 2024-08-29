"""You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:
Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5

Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].
"""


from typing import List


# o(n) time and space
def evalRPN(tokens: List[str]) -> int:
    result_stack = []

    for character in tokens:
        if character == '+':
            result_stack.append(result_stack.pop() + result_stack.pop())
        elif character == '*':
            result_stack.append(result_stack.pop() * result_stack.pop())
        elif character == '/':
            first_pop, second_pop = result_stack.pop(), result_stack.pop()
            result_stack.append(int(second_pop/first_pop))
        elif character == '-':
            first_pop, second_pop = result_stack.pop(), result_stack.pop()
            result_stack.append(second_pop - first_pop)
        else:
            result_stack.append(int(character))
    
    return result_stack.pop()



print(evalRPN(["1","2","+","3","*","4","-"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))