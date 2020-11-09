# https://leetcode.com/problems/valid-parentheses/
# 设置一个stack，每次判断stack最后一个元素是否和新入的元素匹配，匹配pop，否则return false

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if last == '(' and c == ')':
                    continue
                if last == '{' and c == '}':
                    continue
                if last == '[' and c == ']':
                    continue
                return False

        return not stack


class Solution:
    def isValid(self, s: str) -> bool:
        check = {'(': ')', '[':']', '{':'}'}
        stack = []
        for n in s:
            if n in check:
                stack.append(n)
            else:
                if stack and n == check[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return not stack