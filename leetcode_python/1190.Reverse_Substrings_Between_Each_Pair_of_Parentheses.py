class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        (u(love)i)
        
        string: evol
        stack: u
        
        left: add string to stack, string = ''
        right: reverse, and string = stack.pop() + string
        
        """
        string = ''
        stack = []
        
        for char in s:
            if char == '(':
                stack.append(string)
                string = ''
            elif char == ')':
                string = stack.pop() + string[::-1]
            else:
                string += char
                
        return string
        