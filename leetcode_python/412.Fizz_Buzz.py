#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append('FizzBuzz')
            elif i % 5 == 0:
                res.append('Buzz')
            elif i % 3 == 0:
                res.append('Fizz')
            else:
                res.append(str(i))

        return res

# 不用%
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        fizz = 0
        buzz = 0
        for i in range(1, n + 1):
            fizz += 1
            buzz += 1
            if fizz == 3 and buzz == 5:
                res.append('FizzBuzz')
                fizz = 0
                buzz = 0
            elif fizz == 3:
                res.append('Fizz')
                fizz = 0
            elif buzz == 5:
                res.append('Buzz')
                buzz = 0
            else:
                res.append(str(i))

        return res