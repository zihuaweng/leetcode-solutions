#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # [1,1,1,2,2,3]
        # 1:3
        # 2:2
        # 3:1

        counter = collections.Counter(nums)
        heap = []
        for n, c in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (c, n))
            elif c > heap[0][0]:
                heapq.heapreplace(heap, (c, n))

        return [n for _, n in heap]

# bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # [1,1,1,2,2,3]
        # 1:3
        # 2:2
        # 3:1

        counter = collections.Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for n, c in counter.items():
            bucket[c].append(n)

        res = []
        i = len(nums)
        # print(bucket)
        while len(res) < k and i >= 1:
            if bucket[i]:
                res.extend(bucket[i])
            i -= 1

        return res