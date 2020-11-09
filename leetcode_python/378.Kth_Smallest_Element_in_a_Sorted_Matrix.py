# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        matrix = [
           [ 1,  5,  9],
           [10, 11, 13],
           [12, 13, 15]
        ]
        if matrix[i][j] is the cur smallest, we need to check matrix[i+1][j] and matrix[i][j+1]
        but if matrix[i][j] is not the cur smallest, we don't need to check its neighbors.
        
        use a heap to store the candidates
        when one num pop out, check if it is the kth num
            if not, add the one on the right and below to the heap
        """
        heap = [(matrix[0][0],0,0)]
        matrix[0][0] = '#'
        m = len(matrix)
        n = len(matrix[0])
        
        while heap:
            val, i, j = heapq.heappop(heap)
            k -= 1
            if k == 0:
                return val
            
            if i+1 < m and matrix[i+1][j] != '#':
                heapq.heappush(heap, (matrix[i+1][j], i+1, j))
                matrix[i+1][j] = '#'
            if j+1 < n and matrix[i][j+1] != '#':
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
                matrix[i][j+1] = '#'
                
        return -1
                


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        binary search
        
        min: matrix[0][0]
        max: matrix[-1][-1]
        we need to search the kth num
        
        if get_smaller() < k:
            move left = mid + 1
        if get_smaller() >= k:
            move right = mid
            
        get_smaller() can start from left corner
        """
        lo = matrix[0][0]
        hi = matrix[-1][-1]
        
        while lo < hi:
            mid = (lo + hi) // 2
            target = self.get_smaller(matrix, mid)
            if target < k:
                lo = mid + 1
            else:
                hi = mid
                
        return lo
    
    def get_smaller(self, matrix, m):
        rows = len(matrix)
        cols = len(matrix[0])
        
        r = rows-1
        c = 0
        count = 0
        
        while r >= 0 and c < cols:
            if matrix[r][c] <= m:
                count += r+1
                c += 1
            else:
                r -= 1
        
        return count
            
            
        
            
            
        