#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(NlogK)
# Space complexity: O()

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []
        heap = [(math.sqrt(x ** 2 + y ** 2), idx) for idx, (x, y) in enumerate(points)]
        heapq.heapify(heap)
        res = []
        for i in range(K):
            cur = heapq.heappop(heap)
            res.append(points[cur[1]])

        return res


# 另一种写法
class Solution2:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        # 0 0 0 1
        # 1 0 0 0
        # 0 0 0 0
        # 0 0 * 0

        heap = []
        for idx, point in enumerate(points):
            x, y = point
            dist = x * x + y * y
            heapq.heappush(heap, (-temp, idx))
            if len(heap) > K:
                heapq.heappop(heap)
        
        # print(heap)
        res = []
        for dist, idx in heap:
            res.append(points[idx])

        return res


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return heapq.nsmallest(K, points, key=lambda x: x[0]**2+x[1]**2)