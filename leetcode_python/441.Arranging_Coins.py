# https://leetcode.com/problems/arranging-coins/


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(sqrt(2 * n + 0.25) - 0.5)


class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        while n >= i + 1:
            i += 1
            n -= i
        return i