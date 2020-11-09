#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.d = {}
        self.queue = collections.deque()
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        while self.queue and self.d[self.queue[0]] > 1:
            self.queue.popleft()
        return -1 if not self.queue else self.queue[0]

    def add(self, value: int) -> None:
        self.d[value] = self.d.get(value, 0) + 1
        self.queue.append(value)