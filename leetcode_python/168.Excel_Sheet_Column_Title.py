#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def convertToTitle(self, n: int) -> str:
        l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ''
        while n > 0:
            res = l[(n - 1) % 26] + res

            n = (n - 1) // 26

        return res


class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        
        while n > 0:
            num = (n-1) % 26
            res += chr(ord('A')+num)
            n = (n-1) // 26
            
        return res[::-1]