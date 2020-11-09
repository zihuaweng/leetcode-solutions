#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, ele):
        if ele.count == self.count:
            return self.word > ele.word
        return self.count < ele.count

    def __eq__(self, ele):
        return self.count == ele.count and self.word == ele.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        c = collections.Counter(words)
        for word, count in c.items():
            heapq.heappush(heap, (Element(count, word), word))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res[::-1]


