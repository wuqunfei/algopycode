# Design a stack that supports push, pop, top, and retrieving the minimum 
# element in constant time. 
# 
#  Implement the MinStack class: 
# 
#  
#  MinStack() initializes the stack object. 
#  void push(int val) pushes the element val onto the stack. 
#  void pop() removes the element on the top of the stack. 
#  int top() gets the top element of the stack. 
#  int getMin() retrieves the minimum element in the stack. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# Output
# [null,null,null,null,-3,null,0,-2]
# 
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= val <= 2³¹ - 1 
#  Methods pop, top and getMin operations will always be called on non-empty 
# stacks. 
#  At most 3 * 10⁴ calls will be made to push, pop, top, and getMin. 
#  
#  Related Topics Stack Design 👍 6046 👎 534


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque


class MinStack:

    def __init__(self):
        self.deque_data = deque()
        self.deque_mini = deque()

    def push(self, val: int) -> None:
        self.deque_data.append(val)
        if len(self.deque_mini) == 0 or val <= self.deque_mini[-1]:
            self.deque_mini.append(val)

    def pop(self) -> None:
        val = self.deque_data.pop()
        if val == self.deque_mini[-1]:
            self.deque_mini.pop()

    def top(self) -> int:
        return self.deque_data[-1]

    def getMin(self) -> int:
        return self.deque_mini[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(-2)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
