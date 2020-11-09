# https://leetcode.com/problems/trapping-rain-water-ii/

# The idea is to find the min of the boarder. We use heap to record the boarder


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m = len(heightMap)
        n = len(heightMap[0])
        seen = [[0] * n for _ in range(m)]
        heap = []

        # first add boundary into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    seen[i][j] = 1    # mark as visit

        res = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            # find the unvisited cell
            for x, y in ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and seen[x][y] == 0:
                    res += max(0, height - heightMap[x][y])
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y))       # the hight should the the last heigh case we need to know the boundary
                    seen[x][y] = 1
        return res