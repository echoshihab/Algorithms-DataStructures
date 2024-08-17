'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
     
    
    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.min) == 0 or self.min[len(self.min) - 1] >= val:
            self.min.append(val)

    def pop(self) -> None:
        item = self.stack.pop()
        if (item == self.min[len(self.min) - 1]):
            self.min.pop()

    
    def top(self):
        return self.stack[len(self.stack) - 1]


    def getMin(self) -> int:
        return self.min[len(self.min) - 1]
    
    def print(self):
        print(self.stack)
        print(self.min)

    


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)

minStack.print()


print(minStack.getMin()) #return -3
minStack.pop()
print(minStack.top())   # return 0
print(minStack.getMin()) # return -2


