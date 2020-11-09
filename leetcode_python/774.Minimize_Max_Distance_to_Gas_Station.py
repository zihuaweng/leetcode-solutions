#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/minimize-max-distance-to-gas-station/

# 1231. Divide Chocolate
# Capacity To Ship Packages In N Days
# Koko Eating Bananas
# Minimize Max Distance to Gas Station
# Split Array Largest Sum

class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        
        def valid(mid):
            c = 0
            for a, b in zip(stations, stations[1:]):
                c += math.ceil((b-a)/mid)-1
            if c > K:
                return False
            else:
                return True
        
        i = 0
        j = stations[-1]-stations[0]
        while j - i > 1e-6:
            mid = (i+j) / 2
            if valid(mid):
                j = mid
            else:
                i = mid
                
        return i