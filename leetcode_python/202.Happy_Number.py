#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        while n != 1:
            temp = 0
            while n > 0:
                temp += (n%10)**2
                n = n // 10
            if temp in seen:
                return False
            else:
                seen.add(temp)
                n = temp
        return True


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            temp = 0
            while n > 0:
                temp += (n % 10) ** 2
                n = n // 10
            return temp

        if n == 1:
            return True
        fast = get_next(n)
        slow = n
        while fast != slow:
            slow = get_next(slow)
            fast = get_next(fast)
            if fast == 1:
                return True
            fast = get_next(fast)
            if fast == 1:
                return True
        return False

