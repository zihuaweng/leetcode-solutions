#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))

        for j in range(len(num2) - 1, -1, -1):
            for i in range(len(num1) - 1, -1, -1):
                first = ord(num1[i]) - ord('0')
                second = ord(num2[j]) - ord('0')
                product = first * second + res[i + j + 1]
                res[i + j + 1] = product % 10
                res[i + j] += product // 10

        i = 0
        while i < len(res) - 1 and res[i] == 0:
            i += 1

        return ''.join(map(str, res[i:]))

