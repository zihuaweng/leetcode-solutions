#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/valid-number

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()

        e_exists = False
        num_exists = False
        point_exists = False
        num_after_e = False

        for i in range(len(s)):
            c = s[i]
            if c <= '9' and c >= '0':
                num_exists = True
                num_after_e = True
            elif c == 'e':  #
                if e_exists or not num_exists:  # e不可以出现两次，而且前面一定要有数字
                    return False
                e_exists = True
                num_after_e = False  # e后面一定需要有数字，下次遇到数字就可以改变回来，这里意思是如果e结尾了，那么num_after_e肯定会是false
            elif c == '+' or c == '-':
                if i != 0 and s[i - 1] != 'e':  # 符号要不在开头，要不出现在e后面
                    return False
            elif c == '.':
                if e_exists or point_exists:  # 前面出现e不允许，也不能出现多个.
                    return False
                point_exists = True
            else:
                return False

        return num_after_e and num_exists
