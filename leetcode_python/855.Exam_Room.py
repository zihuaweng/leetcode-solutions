#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/exam-room/

# Time complexity: O(n)
# Space complexity: O(n)

class ExamRoom:

    def __init__(self, N: int):
        self.seats = []
        self.last = N - 1

    def seat(self) -> int:
        # print(self.seats)
        if not self.seats:
            self.seats.append(0)
            return 0
        else:
            dis = self.seats[0]
            index = 0
            for i in range(len(self.seats) - 1):
                temp = (self.seats[i + 1] - self.seats[i]) // 2
                if temp > dis:
                    dis = temp
                    index = (self.seats[i + 1] + self.seats[i]) // 2
            if (self.last - self.seats[-1]) > dis:
                index = self.last
            bisect.insort(self.seats, index)
            return index

    def leave(self, p: int) -> None:
        self.seats.remove(p)
        return

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)