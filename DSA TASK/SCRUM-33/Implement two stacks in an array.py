class TwoStacks:
    def __init__(self, n): 
        # Initialize two stacks in a single array of size n
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = n

    # Method to push an element into the first stack
    def push1(self, x):
        # Check if there is space available to push an element into the first stack
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x
        else:
            raise Exception("Stack Overflow")
    
    # Method to push an element into the second stack
    def push2(self, x):
        # Check if there is space available to push an element into the second stack
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x
        else:
            raise Exception("Stack Overflow")
    
    # Method to pop an element from the first stack and return it
    def pop1(self):
        # Check if the first stack is empty
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            return -1
    
    # Method to pop an element from the second stack and return it
    def pop2(self):
        # Check if the second stack is empty
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            return -1

# Example usage:
if __name__ == "__main__":
    # Initialize two stacks in an array of size 10
    ts = TwoStacks(10)
    
    # Perform operations as per the input
    ts.push1(2)
    ts.push1(3)
    ts.push2(4)
    
    print(ts.pop1())  # Output: 3
    print(ts.pop2())  # Output: 4
    print(ts.pop2())  # Output: -1
