#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_val = max(counter.values()) 
        space = (max_val-1) * (n+1)
        for val in counter.values():
            if val == max_val:
                space += 1
                
        return max(space, len(tasks))
