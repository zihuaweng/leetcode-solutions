#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/141768/Detailed-explanation-O(NlogN)

# 所有wage需要满足一样的比率，worker里面最高的比率才能让所有人都能满足最低wage
# 只要找到这几个worker，quality加起来，乘以这个比例
# 所以可以按照比率排序，因为比例越高，有可能得到结果很大，所以从低到高排序
# 达到了K个，quality加起来，乘以这个比例，得到当前最低值
# 当然有可能最高比例的人反而省钱，所以用heap从头到尾计算一遍，保留最低结果

# Time complexity: O(nlogn) [排序 + heap]
# Space complexity: O()

import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted([float(w / q), q] for w, q in zip(wage, quality))
        res = float('inf')
        q_sum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            q_sum += q
            if len(heap) > K:
                q_sum += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, q_sum * r)

        return res
