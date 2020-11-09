#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class KthLargest:

    #     [4,5,8,2]   3

    #     [4,5,8]
    #     [4,5,8]  4
    #     [5,5,8]  5
    #     [10,5,8] 5
    #     [10,9,8] 8
    #     [10,9,8] 8

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[:k]
        heapq.heapify(self.heap)

        for n in nums[k:]:
            heapq.heappushpop(self.heap, n)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)