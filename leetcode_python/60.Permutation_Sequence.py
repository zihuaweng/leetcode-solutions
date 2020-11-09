#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/permutation-sequence/
# 每个后面的排序都是factorial（n-1

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [i for i in range(1, n + 1)]
        res = ""
        k -= 1

        mod = math.factorial(n)    # 这里是把factorial统一放外面减少计算
        # 也可以用
        # mod = reduce(operator.mul, numbers)

        while n > 0:
            mod //= n
            n -= 1
            index, k = divmod(k, mod)
            res += str(numbers.pop(index))

        return res