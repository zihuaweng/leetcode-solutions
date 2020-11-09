# https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        [0,1,3,5,6,8,12,17]
         0 1 2 3 4 5  6  7
                      |  
                      
        [0,1,2,3,4,8,9,11]
         0 1 2 3 4 5 6  7
               |
                   |
        
        need to record fail in order to save time
        """
        failed = set()
        stones_set = set(stones)
        
        def dfs(num, jump):
            if num == stones[-1]: return True
            if num not in stones_set: return False
            if (num, jump) in failed: return False

            if jump > 1:
                if dfs(num+jump-1, jump-1): return True
            if jump > 0:
                if dfs(num+jump, jump): return True
            if dfs(num+jump+1, jump+1): return True

            failed.add((num, jump))
            return False
    
    
        return dfs(0, 0)
        