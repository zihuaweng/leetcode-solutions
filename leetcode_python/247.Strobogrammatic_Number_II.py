#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/strobogrammatic-number-ii/

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n & 1:
            r = ['0', '1', '8']
        else:
            r = ['']
        for i in range(n >> 1):
            new_list = []
            for j in r:
                if i != (n >> 1) - 1:
                    new_list.append('0' + j + '0')
                new_list.append('1' + j + '1')
                new_list.append('6' + j + '9')
                new_list.append('8' + j + '8')
                new_list.append('9' + j + '6')
            r = new_list

        return r


class Solution:
    def findStrobogrammatic(self, l: int) -> List[str]:
        return self.helper(l, l)

    def helper(self, l, n):
        res = []
        if l == 1:
            return ['0', '1', '8']
        if l == 0:
            return ['']
        for s in self.helper(l - 2, n):
            if l != n:
                res.append('0' + s + '0')
            res.append('1' + s + '1')
            res.append('6' + s + '9')
            res.append('8' + s + '8')
            res.append('9' + s + '6')
        return res



