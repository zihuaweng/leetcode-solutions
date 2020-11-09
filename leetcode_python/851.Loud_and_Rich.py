#!/usr/bin/env python3
# coding: utf-8

# 这个题目有点难懂，看下面的视频解释
# https://www.youtube.com/watch?v=JRecqHkvGs4&feature=youtu.be

# Time complexity: O(richer.length)
# Space complexity: O(N)

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        ans = [-1] * len(quiet)
        out_nodes = collections.defaultdict(list)
        for i, j in richer:
            out_nodes[j].append(i)

        def dfs(i):
            if ans[i] >= 0:
                return
            ans[i] = i
            for j in out_nodes[i]:
                dfs(j)
                if quiet[ans[j]] < quiet[ans[i]]:
                    ans[i] = ans[j]

        for i in range(len(quiet)):
            dfs(i)
        return ans