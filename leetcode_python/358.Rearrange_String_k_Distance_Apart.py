#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/rearrange-string-k-distance-apart/

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        res = ''
        if k == 0:
            return s

        counter = collections.Counter(s)
        heap = []
        for i, j in counter.items():
            heap.append((-j, i))
        heapq.heapify(heap)

        while len(res) < len(s):
            q = []
            if not heap:
                return ''
            for _ in range(k):
                if len(res) == len(s):
                    return res
                if not heap:
                    return ''
                count, char = heapq.heappop(heap)
                res += char
                if count < -1:
                    q.append((count + 1, char))
            while q:
                heapq.heappush(heap, q.pop())

        return res

