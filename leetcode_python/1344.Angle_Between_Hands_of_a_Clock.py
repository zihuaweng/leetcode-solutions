# https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        degree = abs(hour*30 + 0.5*minutes - 6*minutes)
        return min(degree, 360-degree)