# https://leetcode.com/problems/shortest-distance-from-all-buildings/

# We can start from buildings, so the complexity will be O(B*M*N) (B: # of buildings)
# insteading of O(E*M*N) (E: # of empty places). We might assume that empty place is way more than buildings.

# reach records how many buildings current empty space can reach
# dist records the total distance of current empty space to all other visited buildings


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        m = len(grid)
        n = len(grid[0])
        reach = [[0] * n for _ in range(m)]
        dist = [[0] * n for _ in range(m)]

        def bfs(i, j, cnt):
            queue = collections.deque([(i, j, 0)])
            while queue:
                x, y, step = queue.popleft()
                for _x, _y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nx, ny = x + _x, y + _y
                    # The next candidates are empty space (grid[nx][ny] == 0)
                    # and are able to reach all previous visited buildings
                    # (reach[nx][ny] == cnt).
                    # Otherwise, we can stop bfs immediately if we cannot reach
                    # all buildings.
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0 and reach[nx][ny] == cnt:  # only the empty space that can reach all previous visited buildings is able to visited coming buildings.
                        dist[nx][ny] += step + 1
                        reach[nx][ny] += 1
                        queue.append((nx, ny, step + 1))

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j, cnt)    # here we record the count of buildings
                    cnt += 1

        print(dist)
        print(reach)
        print(grid)
        res = float("inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach[i][j] == cnt:
                    res = min(res, dist[i][j])

        return res if res < float("inf") else -1