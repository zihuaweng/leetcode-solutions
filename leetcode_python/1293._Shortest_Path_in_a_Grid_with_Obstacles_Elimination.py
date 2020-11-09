# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

class Solution:
    def shortestPath(self, grid: List[List[int]], K: int) -> int:
        """
        bfs + mo
        
        start: (0,0), k, step=0
        stop: k < 0 || (i,j) == (m-1, n-1)
        
        """
        m = len(grid)
        n = len(grid[0])
        
        queue = collections.deque([(0,0,K,0)])
        seen = set()
        
        while queue:
            i, j, k, steps = queue.popleft()
            
            if (i,j) == (m-1, n-1):
                return steps
            
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i,j+1)]:
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 1 and k > 0 and (x,y,k-1) not in seen:
                        seen.add((x,y,k-1))
                        queue.append((x, y, k-1, steps+1))
                    if grid[x][y] == 0 and (x,y,k) not in seen:
                        seen.add((x,y,k))
                        queue.append((x, y, k, steps+1))   
                    
        return  -1
                        
        