# https://leetcode.com/problems/design-a-stack-with-increment-operation/


class CustomStack:
    """
    xxxxxxxxx i
         2
      2     5
    999777555      
      
    """
    
    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack: 
            return -1
        
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
            
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if len(self.inc) > 0:
            idx = min(k-1, len(self.inc)-1)
            self.inc[idx] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)