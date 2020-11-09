#https://leetcode.com/problems/jump-game-iii/

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
        dfs + seen
        each node: i+arr[i] or i-arr[i]
        stop: out of boundary
            reach arr[i] = 0
        """
        return self.dfs(arr, start, set())
    
    def dfs(self, arr, i, seen):
        if i in seen or i < 0 or i >= len(arr):
            return False
        if arr[i] == 0:
            return True
        
        seen.add(i)
        
        if self.dfs(arr, i-arr[i], seen):
            return True
        if self.dfs(arr, i+arr[i], seen):
            return True
        
        return False
        