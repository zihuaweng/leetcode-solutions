class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        maintain i, j , i is the left pointer, j is the right pointer
        a b c a b c
        |   |
          |   |  if i == 1 and j == 3 is valid, then i <= 1 and j==3 is also valid, we need to add i+1 number to res
        """
        i = 0
        res = 0
        d = {c:0 for c in 'abc'}
        
        for j, val in enumerate(s):
            d[val] += 1
            while all(d.values()):
                d[s[i]] -= 1
                i += 1
            res += i
            
        return res
        
        