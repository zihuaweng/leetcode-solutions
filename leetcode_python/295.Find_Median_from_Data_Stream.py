#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/find-median-from-data-stream/


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large = []  # the larger half of the list, min heap
        self.small = []  # the smaller half of the list, max heap (invert min-heap)

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        # print(self.large)
        # print(self.small)
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0] - self.small[0]) / 2


class MedianFinder:
    """
    1. brute force: insert number to list
    1
    1 2
    1 2 3
    1 2 2 3.
       
            1. find the loaction to insert number using binary search: O(logn)
            2. insert the number: O(n)
        O(n)
        
    2. 
        1. #left == #right or #left + 1== #right
            left is sorted descending  : max_heap  
            right is sorted ascending  : min_heap  
        2. compare new num to left first and right first to decide the num could fit to which group,add num to the group   O(log(n/2))
            1. only check the first num of each group, use heap
            2. if num < left_first : add to left       
            3. else : add to right    
            
        
        3. set back to #left == #right or #left + 1== #right, O(log(n/2))
            if #left + 2 == #right: 
                add right pop() to left
            if #left == #right + 1: 
                add left pop() to right
            
        4. return median  O(1)
            if #left == #right: return avg(left_first, right_fist)
            if #left + 1 == #right: return right_first

        
    O(log(n))

    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l_heap = []   #max_heap
        self.r_heap = []   #min_heap

    def addNum(self, num: int) -> None:
        if len(self.l_heap) != 0 and num < -self.l_heap[0]:
            heapq.heappush(self.l_heap, -num)
        else:
            heapq.heappush(self.r_heap, num)
            
        # set back to #left == #right or #left + 1== #right
        if len(self.l_heap) == len(self.r_heap) + 1:
            heapq.heappush(self.r_heap, -heapq.heappop(self.l_heap))
        if len(self.l_heap) + 2 == len(self.r_heap):
            heapq.heappush(self.l_heap, -heapq.heappop(self.r_heap))
    def findMedian(self) -> float:
        if len(self.l_heap) == len(self.r_heap):
            return (self.r_heap[0]-self.l_heap[0]) / 2.0
        else:
            return self.r_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()