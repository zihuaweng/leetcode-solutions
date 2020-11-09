#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 1231. Divide Chocolate
# Capacity To Ship Packages In N Days
# Koko Eating Bananas
# Minimize Max Distance to Gas Station
# Split Array Largest Sum


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        """
        [3,6,7,11] 8
        
        - try : k in 1 - sum(piles)   binary search O(logn)
            k = 1:  hours > 8   k ++
            k = sum, hours < 8  k --
        
        - lo = 1, hi = sum(piles)
        - calculate the hours it take Koko to finish the bana
            - if hours > H:  increase k, lo = k + 1
            - if hours < H:  decrease k, hi = k
            - if hours = H:  decrease k, hi = k
        """
        lo = 1
        hi = sum(piles)
        
        while lo < hi:
            mid = (lo+hi)//2
            hours = self.get_hours(piles, mid)
            # print(lo, hi, mid, hours, mid)
            if hours > H:
                lo = mid + 1
            else:
                hi = mid
        return lo
            
            
    def get_hours(self, piles, target):
        hours = 0
        for p in piles:
            hours += p // target
            if p % target > 0:
                hours += 1
        return hours 