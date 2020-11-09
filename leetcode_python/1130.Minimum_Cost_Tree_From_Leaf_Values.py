#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

# Time complexity: O()
# Space complexity: O(n^3)
# dp or dfs

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        d = {}

        def dfs(i, j):
            if i + 1 == j:
                return 0
            if (i, j) not in d:
                d[(i, j)] = float("inf")
                for k in range(i + 1, j):
                    d[(i, j)] = min(d[(i, j)], dfs(i, k) + dfs(k, j) + max(arr[i:k]) * max(arr[k:j]))
            return d[(i, j)]

        return dfs(0, len(arr))


# Time complexity: O()
# Space complexity: O(n)
# dp or dfs
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O(N)-Time-and-Space

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float("inf")]
        res = 0
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)

        while len(stack) > 2:
            res += stack.pop() * stack[-1]

        return res


map(lambda w, word_list: word_list.count(w), unique_words[0], itertools.repeat(non_stop_words[0],len(unique_words[0])))