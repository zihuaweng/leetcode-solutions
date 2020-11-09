#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/reorganize-string/

# 思路是使用heap
# 每次需要pop 前面两个，这里的写法比较巧妙

class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = collections.Counter(S)
        heap = []
        for char, c in counter.items():
            heapq.heappush(heap, (-c, char))

        pre_char, pre_c = '', 0
        res = ''
        while heap:
            c, char = heapq.heappop(heap)
            c += 1
            res += char
            if pre_c < 0:
                heapq.heappush(heap, (pre_c, pre_char))
            pre_char, pre_c = char, c

        if len(res) == len(S):
            return res
        else:
            return ''