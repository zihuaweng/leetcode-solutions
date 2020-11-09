#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/satisfiability-of-equality-equations/
# 可以使用dfs，首先第一步构建一个==的图，然后看！=的，如果可以相连的证明false，不相连就证明true

# Time complexity: O(n)
# Space complexity: O(n)

# 另一个方法是find union，速度空间完胜上面
# https://leetcode.com/problems/satisfiability-of-equality-equations/discuss/234486/JavaC%2B%2BPython-Easy-Union-Find
# https://www.hackerearth.com/practice/notes/disjoint-set-union-union-find/

# Time complexity: O(n)
# Space complexity: O(n)

import collections


class Solution:
    def equationsPossible(self, equations) -> bool:
        nums = collections.defaultdict(set)

        def dfs(u, v, vis):
            if u in nums[v]:
                return True
            else:
                for i in nums[v]:
                    if i not in vis:
                        vis.append(v)
                        if dfs(u, i, vis):
                            return True
            return False

        for i in equations:
            if i[1] == '=':
                nums[i[0]].add(i[3])
                nums[i[3]].add(i[0])

        for i in equations:
            if i[1] == '!':
                if i[0] == i[3]:
                    return False
                if dfs(i[0], i[3], []):
                    return False
        return True


    def equationsPossible_2(self, equations: List[str]) -> bool:
        '''使用find union的方法可以很快找到小群里面的root'''
        chars = [i for i in 'qwertyuiopasdfghjklzxcvbnm']
        fu = {a: a for a in chars}

        def find_union(x):
            if x != fu[x]:
                fu[x] = find_union(fu[x])
            return fu[x]

        for a, e, _, b in equations:
            if e == '=':
                fu[find_union(a)] = find_union(b)

        for a, e, _, b in equations:
            if e == '!':
                if find_union(a) == find_union(b):
                    return False
        return True