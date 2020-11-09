class Solution:
    def reverseWords(self, s: str) -> str:
        """
        "hello world"
        
        "dlrow olleh"
               l
                    r
        
        
        1. reverse the whole string
        2. if l == ' ', move l and r
        3. if r != ' ' r++
        4. find a valid word, reverse it, add to the result
        5. move l = r
        6. add the last word if l < r and l != ' '
        """
        s = self.reverse_string(s)
        l = 0
        r = 0
        res = ''
        
        while r < len(s):
            if s[l] == ' ':
                l += 1
                r += 1
            elif s[r] != ' ':
                r += 1
            else:
                temp = self.reverse_string(s[l:r])
                res += temp + ' '
                l = r
                
        if (l < r and s[l] != ' '):
            temp = self.reverse_string(s[l:r])
            res += temp + ' '
        
        return res[:-1]
        
    def reverse_string(self, s):
        s = list(s)
        l = 0
        r = len(s)-1
        while (l < r):
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
            
        return ''.join(s)
    