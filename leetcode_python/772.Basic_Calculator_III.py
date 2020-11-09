#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def calculate(self, s: str) -> int:
        """
        think it as multiple string of basic calculator II
        
        (2+6* 3+5- (3*14/7+2)*5)+3
        
        1. (3*14/7+2)  -> sum1
        2. (2+6* 3+5- sum *5) -> sum2 
        3. sum2 + 3 
        
        what we need is a function eval() to calculate +-*/ without ()
        
        since the return eval() might be negative, it could be
        
        2+-6*-3+5--3*-14
        ->
        [2, -6*-3, 5, -(-3*-4)]
        
        """
        s = s.replace(' ', '')
        stack = []
        string = ''
        
        for char in s:
            if char == '(':
                stack.append(string)
                string = ''
            elif char == ')':
                string = stack.pop() + str(self.eval(string))
            else:
                string += char
                
        return self.eval(string)
    
    
    def eval(self, s):
        print(s)
        stack = []
        num = 0
        sign = '+'
        negative = 1
        
        s += ' '
        
        for i, char in enumerate(s):
            if char.isdigit():
                num = num*10 + int(char)
            else:
                # the only different with basic calculator II is this to add negative to num
                if char == '-' and (i == 0 or not s[i-1].isdigit()):  
                    negative = -1
                    continue
                num *= negative
                negative = 1
                if sign == '+' or sign == '-':
                    temp = num if sign == '+' else -num
                    stack.append(temp)
                elif sign == '*':
                    stack[-1] *= num
                else:
                    temp_sign = -1 if stack[-1] < 0 else 1
                    stack[-1] = temp_sign * (abs(stack[-1])//num)
                num = 0
                sign = char
                
        return sum(stack)
        
        