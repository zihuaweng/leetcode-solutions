# https://leetcode.com/problems/android-unlock-patterns/

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        """
        1, 3, 7, 9 are symmetric, we can calculate and * 4
        2, 4, 6, 8 are symmetric, we can calculate and * 4
        
        each key has left, right, up, down and 4 corner which is too much to calculate
        what we can do is to use skip instead.
        for example, from 1, 3, we can't skip 2, we can only go from 1 to 3 is 2 is visisted.
        
        use dfs to find all the paths
        """
        skips = [[0] * 10 for _ in range(10)]
        
        skips[1][3] = skips[3][1] = 2
        skips[4][6] = skips[6][4] = 5
        skips[7][9] = skips[9][7] = 8
        skips[1][7] = skips[7][1] = 4
        skips[2][8] = skips[8][2] = 5
        skips[3][9] = skips[9][3] = 6
        skips[1][9] = skips[9][1] = skips[3][7] = skips[7][3] = 5
        
        count = 0
        seen = [False] * 10
        seen[0] = True
        for i in range(m, n+1):
            count += self.dfs(1, seen, i, skips) * 4 # 1, 3, 7, 9 are symmetric, we can calculate and * 4
            count += self.dfs(2, seen, i, skips) * 4 # 2, 4, 6, 8 are symmetric, we can calculate and * 4
            count += self.dfs(5, seen, i, skips)
            
        return count
        
    def dfs(self, i, seen, remain, skips):
        if remain == 1:
            return 1
        seen[i] = True
        
        count = 0
        for j in range(1, 10):
            if not seen[j] and seen[skips[i][j]]:
                count += self.dfs(j, seen, remain-1, skips)
                
        seen[i] = False
        return count
                
        