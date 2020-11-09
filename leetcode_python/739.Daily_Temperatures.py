#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# stack

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        [73, 74, 75, 71, 69, 72, 76, 73]

        1    1       2   1
        75, 2 | 72 5 |    
        """
        
        stack = []
        res = [0] * len(T)
        
        for i, val in enumerate(T):
            while stack and T[stack[-1]] < val:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res