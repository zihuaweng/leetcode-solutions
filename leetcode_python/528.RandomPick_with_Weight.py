#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/random-pick-with-weight/

class Solution:
    
    """
    w = 1 2 3 2 1 4 2
    -> [1][2,3][4,5,6][7,8][9][10,11,12,13][14,15]
    r = random.int(1, 15) -> eg 10
    
    we can create multiple small trunks, and get the random number r to find the value
    say, we have 10, it should be in [9,10,11,12] which is the truck with index 5, so return arr[5]
    
    optimization:
    use the upper bound and binary search to get number
    w = 1 2 3 2 1 4 2
    -> [1][2,3][4,5,6][7,8][9][10,11,12,13][14,15]
    -> 1, 3, 6, 8, 9, 13, 15
    
    r = random.int(1, 15) -> eg 10
    
    we get the upper bound, the first number on the right that is bigger or equal to target, for 10, get 13, that is arr[5]
    """

    def __init__(self, w: List[int]):
        self.arr = []
        s = 0
        for i in w:
            s += i
            self.arr.append(s)
        self.w = w

    def pickIndex(self) -> int:
        seed = random.randint(1, self.arr[-1])
        # index = bisect.bisect_left(self.arr, seed)   
        l = 0
        r = len(self.w)
        while l < r:
            mid = (l+r)//2
            if self.arr[mid] < seed:
                l = mid + 1
            else:
                r = mid
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()