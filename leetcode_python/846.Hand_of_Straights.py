#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/hand-of-straights/

# Time complexity: O(nlogn)
# Space complexity: O()

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if W == 1:
            return True
        if len(hand) % W != 0:
            return False
        c = collections.Counter(hand)
        heap = list(c.keys())
        heapq.heapify(heap)
        while heap:
            cur = heap[0]
            c[cur] -= 1
            for i in range(1, W):
                if c[cur + i] <= 0:
                    return False
                c[cur + i] -= 1
            while heap and c[heap[0]] == 0:
                heapq.heappop(heap)
        return True



