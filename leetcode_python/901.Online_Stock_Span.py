#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# similar questions
# https://leetcode.com/problems/online-stock-span/discuss/168311/C%2B%2BJavaPython-O(1)
# 求出当前数字前面连续的当前数小的值
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


class StockSpanner:
    def __init__(self):
        self.stack = [(-1, float('inf'))]
        self.index = 0
        
    def next(self, price: int) -> int:
        while self.stack[-1][1] <= price:
            self.stack.pop()
        res = self.index - self.stack[-1][0]
        self.stack.append((self.index, price))
        self.index += 1
        return res