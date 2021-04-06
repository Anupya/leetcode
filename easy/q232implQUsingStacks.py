# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        
        # move all elements from stack1 to stack2
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1[-1]) #last element in stack1 is first out
            self.stack1.pop()
        
        self.stack1.append(x)
        
        # move back all elements from stack2 to stack1
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()
            
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack1) == 0:
            return "Q is empty"
        x = self.stack1[-1]
        self.stack1.pop()
        return x

    
    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack1[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack1) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()