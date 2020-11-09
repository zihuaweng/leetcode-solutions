# https://leetcode.com/problems/number-of-squareful-arrays/

class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        A.sort()
        used = [False] * len(A)
        
        return self.dfs(A, [], used)
        
    def dfs(self, arr, temp, used):
        # print(temp, used)
        if len(temp) == len(arr):
            return 1
        
        c = 0
        
        for i in range(len(arr)):
            if used[i]: continue
            if i > 0 and arr[i] == arr[i-1] and not used[i-1]: continue
            if temp and not self.is_square(temp[-1], arr[i]): continue
                
            used[i] = True
            c += self.dfs(arr, temp+[arr[i]], used)
            used[i] = False
            
        return c
        
        
    def is_square(self, x, y):
        s = int((x+y) ** 0.5)
        return s*s == x+y
    
    