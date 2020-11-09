#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/power-of-three/
# 把数字改成任意primer都可行
# 例如找到power two
# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 1:
            while n % 3 == 0:
                n //= 3

        return n == 1

# loga c/loga b=logb c

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n>0 and (math.log10(n) / math.log10(3)) % 1 == 0


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_pow = math.pow(3, int(math.log(1<<31) / math.log(3)))
        # print(max_pow)   1162261467
        return n>0 and max_pow%n == 0