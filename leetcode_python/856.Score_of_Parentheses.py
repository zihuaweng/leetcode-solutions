class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        
        """
        stack to store value instead of ")" or "("
        
        """
        stack = []
        cur = 0
        for c in S:
            if c == '(':
                stack.append(cur)
                cur = 0
            else:
                if cur != 0:
                    cur *= 2
                else:
                    cur = 1
                cur += stack.pop()
                
        return cur