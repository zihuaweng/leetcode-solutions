# https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        dfs 
        start : first row
        end : last row
        
        store col in cols_set
        
        """
        cols = set()
        left_diagonal = set()
        right_diagonal = set()
        return self.dfs(n, 0, cols, left_diagonal, right_diagonal)
    
    def dfs(self, n, row, cols, left_diagonal, right_diagonal):
        if row == n:
            return 1
        
        count = 0
        
        for col in range(n):
            left = col+row
            right = n+row-col-1
            if col in cols or left in left_diagonal or right in right_diagonal:
                continue
                
            cols.add(col)
            left_diagonal.add(left)   # n*2-1
            right_diagonal.add(right)   
            cur_row = '.'*col + 'Q' + '.'*(n-col-1)

            count += self.dfs(n, row+1, cols, left_diagonal, right_diagonal)

            cols.remove(col)
            left_diagonal.remove(left)
            right_diagonal.remove(right)
    
        return count

                
                
                
    