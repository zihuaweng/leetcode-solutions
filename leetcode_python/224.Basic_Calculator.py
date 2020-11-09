#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 不可以使用772的方法，太慢
# https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s):
        """
        1+(4+5+2)-3+(6+8)
                |
        sign_stack: 1
        num_stack: 1
        
        num = 2
        sign = 1
        
        cur_sum = 11   (+sign*num)  
        when we find '(':  add sign to sign_stack and num to num_stack 
        when we find ')':  cur_sum * sign_stack.pop() + num_stack.pop()
        """
        res, num, sign, stack = 0, 0, 1, []
        for ss in s:
            if ss.isdigit():
                num = 10*num + int(ss)
            elif ss in ["-", "+"]:
                res += sign*num
                num = 0
                sign = [-1, 1][ss=="+"]
            elif ss == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif ss == ")":
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        # remove the space and correct negative integers.
        s = s.replace(' ', '')

        numstack, opstack = [], []
        i = 0
        s += '+'
        while i < len(s):
            if s[i] == '(':
                opstack.append(s[i])
                i += 1
            elif s[i].isdigit():
                tmp_num = ''
                while i < len(s) and s[i].isdigit():
                    tmp_num += s[i]
                    i += 1
                numstack.append(int(tmp_num))
            else:
                while opstack and opstack[-1] != '(':
                    num2 = numstack.pop(-1)
                    num1 = numstack.pop(-1)
                    tmp_res = self.helper(num1, num2, opstack.pop(-1))
                    numstack.append(tmp_res)

                if s[i] == ')':
                    opstack.pop(-1)
                else:
                    opstack.append(s[i])
                i += 1
        return numstack[0]

    def helper(self, n1, n2, op):
        if op == '+':
            return n1 + n2
        if op == '-':
            return n1 - n2