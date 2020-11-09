# https://leetcode.com/problems/min-stack/
# 记得要保留一个list_min的列表，记录list_1每个index对应的一个最小值，这样可以直接拿到需要的最小值，不用去计算。


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list_1 = []
        self.list_min = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list_1.append(x)
        if self.list_min:
            if self.list_min[-1] > x:
                self.list_min.append(x)
            else:
                self.list_min.append(self.list_min[-1])
        else:
            self.list_min.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.list_1.pop()
        self.list_min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.list_1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.list_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()