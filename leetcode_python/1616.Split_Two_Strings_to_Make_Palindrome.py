# https://leetcode.com/problems/split-two-strings-to-make-palindrome/

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        """
        i -> go from start of a prefix
        j -> go from end of b surfix
        
        xx[xxx]xx     need to check [xxx] or [yyy] is palindrome
        |i
               j|
        yy[yyy]yy 
        
        do the same thing for a surfix and b prefix
        
        time O(n)
        space O(1)
        """
        i = 0 
        j = len(a)-1
        
        while i < j and a[i] == b[j]:
            i += 1
            j -= 1
            
        if self.is_pa(a, i, j):
            return True
        if self.is_pa(b, i, j):
            return True
        
        i = 0 
        j = len(a)-1
        
        while i < j and b[i] == a[j]:
            i += 1
            j -= 1
            
        if self.is_pa(a, i, j):
            return True
        if self.is_pa(b, i, j):
            return True
        
        return False
    
    def is_pa(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        