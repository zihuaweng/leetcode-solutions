# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """

        P   A   H   N
        A P L S I I G
        Y   I   R


        [P A H N]
        [A P L S I I G]
        [Y I R]


        0 -> numRows-1.   top to bottom  (row+1)
        numRows-1 - > 0,   bottom to top (row-1)
        
        corner case:
            numRows = 1: return string
            numRows >> len(s): return string
            
        time O(n)
        space O(n)
        """
        if numRows == 1 or numRows > len(s):
            return s
        
        res = [[] for _ in range(numRows)]
        delta = -1
        row = 0
        for c in s:
            res[row].append(c)
            if row == 0 or row == numRows-1:
                delta *= -1
            row += delta
        return ''.join([''.join(arr) for arr in res])

    
