#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(nm)
# Space complexity: O(n+m)


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        """
        brute force

        1. calculate dist between each bike and person, put them in the list    O(n*n)
        2. sort the list    O(nlogn)
        3. go throught the list, save the bike-person pair and make token bikes and people to visited. O(n)

        O(n*n)

        超时
        1. calculate dist between each bike and person, put them in the list.  O(n*n)
        2. put dist to a heap, (dist, bike, person)  O(logn)
        3. go throught the list, save the bike-person pair and make token bikes and people to visited. O(n)


        bucket sort
        it's O(M * N) time and O(M * N)
        """
        n = len(workers)
        m = len(bikes)
        seen_b = [0] * m
        res = [-1] * n
        buckets = [[] for _ in range(2001)]
        
        for i in range(n):
            for j in range(m):
                w = workers[i]
                b = bikes[j]
                dist = self.get_dist(w, b)
                buckets[dist].append((i,j))
                
        for idx in range(2001):
            for i, j in buckets[idx]:
                if res[i] == -1 and seen_b[j] == 0:
                    res[i] = j
                    seen_b[j] = 1
                    
        return res
            
            
    def get_dist(self, worker, bike):
        dist = abs(worker[0]-bike[0]) + abs(worker[1]-bike[1])
        return dist