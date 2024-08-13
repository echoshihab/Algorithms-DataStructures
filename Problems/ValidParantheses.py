'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''

# o(n) space and time complexity
def isValid(s: str) -> bool:

    brackets = {"(" : ")", "{": "}", "[": "]"}
    stack = []

    if len(s) % 2 == 1: return False

    for item in s:
        if item in brackets:
            stack.append(item)
        elif len(stack) == 0 or brackets[stack.pop()] != item:
            return False
    
    return len(stack) == 0


