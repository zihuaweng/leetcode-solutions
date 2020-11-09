#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/shortest-distance-to-target-color/

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:

    #     [1, 1, 2, 1, 3, 2, 2, 3, 3]
    # counter      1：[0,1,3]
    #              2:[2,5,6]
    #              3:[4,7,8]
    # binary search

        if not colors:
            return []

        index = collections.defaultdict(list)
        for i, j in enumerate(colors):
            index[j].append(i)

        print(index)

        res = []
        for i, char in queries:
            if char in index:
                idx = bisect.bisect_left(index[char], i)
                if idx == 0:
                    res.append(abs(index[char][0] - i))
                elif idx >= len(index[char]):
                    res.append(abs(index[char][-1] - i))
                else:
                    temp = min(abs(index[char][idx] - i), abs(index[char][idx - 1] - i))
                    res.append(temp)
            else:
                res.append(-1)
        return res