class MyStack:


    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()
        self.count = 0 # can also do deque().count()

    def push(self, x: int) -> None:
        # add to a stack, increment count
        stack = self.q1 or self.q2
        stack.append(x)
        self.count += 1
        
    def pop(self) -> int:
        # move all except 1 to other stack, decrement count, return last element
        # fullStack = self.q1 if len(self.q1) > 0 else self.q2
        # emptyStack = self.q1 if len(self.q1) == 0 else self.q2
        fullStack = self.q1 if max(len(self.q1), len(self.q2)) == len(self.q1) else self.q2
        emptyStack = self.q1 if min(len(self.q1), len(self.q2)) == len(self.q1) else self.q2
        while len(fullStack) != 1:
            emptyStack.append(fullStack.popleft())
        self.count -= 1
        return fullStack.popleft()
        
    def top(self) -> int:
        # move all except 1 to other stack, store ptr to last element, move last element, return ptr
        # fullStack = self.q1 if len(self.q1) > 0 else self.q2
        # emptyStack = self.q1 if len(self.q1) == 0 else self.q2
        fullStack = self.q1 if max(len(self.q1), len(self.q2)) == len(self.q1) else self.q2
        emptyStack = self.q1 if min(len(self.q1), len(self.q2)) == len(self.q1) else self.q2
        while len(fullStack) != 1:
            emptyStack.append(fullStack.popleft())
        temp = fullStack.popleft()
        emptyStack.append(temp)
        return temp

    def empty(self) -> bool:
        return self.count == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()