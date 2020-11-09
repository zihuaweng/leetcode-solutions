# 与spiral matrix I一样

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        up = left = 0
        down = right = n-1
        res = [[0] * n for _ in range(n)]
        num = 1
        
        while num <= n*n:
            for i in range(left, right+1):
                res[up][i] = num
                num += 1
            up += 1
                
            for i in range(up, down+1):
                res[i][right] = num
                num += 1
            right -= 1
            
            if num <= n*n:   # 这里可以省略，因为是正方形，但是保留代码可以运行m*n的矩阵
                for i in range(right, left-1, -1):
                    res[down][i] = num
                    num += 1
                down -= 1
                
            if num <= n*n:
                for i in range(down, up-1, -1):
                    res[i][left] = num
                    num += 1
                left += 1
            
        return res