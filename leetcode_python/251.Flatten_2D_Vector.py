class Vector2D:

    def __init__(self, v: List[List[int]]):
        
        def it(v):
            for line in v:
                for val in line:
                    self.size -= 1
                    yield val
                    
        self.iter = it(v)
        self.size = sum(len(a) for a in v)
            
    def next(self) -> int:
        return next(self.iter)

    def hasNext(self) -> bool:
        return self.size > 0


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()